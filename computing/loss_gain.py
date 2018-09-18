import tensorflow as tf
import numpy as np
import scipy.sparse as sparse
DTYPE=tf.float32

#def scipy2tf_max(stoich_spmtx):
#    coo=stoich_spmtx.tocoo()
#    indices=np.mat([coo.row,coo.col]).transpose()
#    return tf.SparseTensor(indices,coo.data,coo.shape),np.amax(coo.data)

def reactants2spvec_spmtx(num_chems, stoich_coo):
    """
    Generate a sparse matrix which transforms reactants
    array into a sparse matrix in vector form with the
    same shape as stoich matrix
    transform_spmtxs*reactants -> vec (casted to matrix)== stoich_mtx (all ones, only reactant side) .*reactants (broadcasted)
    :param num_chems: number of reactants (chemicals)
    :param stoich_coo: stoich matrix in COO form (scipy.sparse) (num_eqn*num_chem)
    :return: transform_spmtx
    """
    rows=stoich_coo.row
    cols=stoich_coo.col
    n=len(rows)
    transform_spmtx=sparse.dok_matrix((n, num_chems), np.int8)
    for i in range(n):
        if stoich_coo[rows[i],cols[i]]>0:#Only reactants are considered in [A]^a * [B]^b for a A + b B =c C + d D
            chem_ind=cols[i]
            transform_spmtx[i,chem_ind]=1
    coo=transform_spmtx.tocoo()
    sortedind=np.lexsort((coo.row,coo.col))
    indices=np.mat([coo.row[sortedind],coo.col[sortedind]]).transpose()
    return tf.SparseTensor(indices,coo.data[sortedind],coo.shape)

def norm_seq(rows,cols,vals):
    """
    :param rows: sorted rows [0 0 0 1 1 1 1]
    :param cols: partitioned by rows and sorted
    :param vals: value of sparse matrix
    :return: normed cols [1 5 9 1 3 8] -> [0 1 2 0 1 2]
    """
    n=len(cols)
    lastrow=-1
    newcol=0
    for i in range(n):
        col=cols[i]
        row=rows[i]
        stoich=vals[i]
        if stoich>0:
            if row!=lastrow:
                newcol=0
            else:
                newcol+=1
            lastrow=row
            yield newcol

def condense_spmtx(stoich_coo):
    """
    condense column index of stoich_mtx shaped sparse matrix into a dense matrix
    :param stoich_coo: HAVE TO BE SORTED
    :return: column indexes for COO format
    """
    rows=stoich_coo.row
    cols=stoich_coo.col
    normed_cols=norm_seq(rows,cols)
    return normed_cols

#def gen_rate_values():


def gen_loss_gain(num_chems, num_eqns, max_reactants, stoich_mtx):
    """

    :param num_chems:
    :param num_eqns:
    :param max_reactants:
    :param stoich_mtx: num_eqn*num_chem
    :return:
    """
    reactants=tf.placeholder(DTYPE, (num_chems,), "reactants")
    rate_values=tf.placeholder(DTYPE, (num_eqns,), "rate_values")
    coo=stoich_mtx.tocoo()
    sortedind_row=np.lexsort((coo.row,coo.col))
    sortedind_col=np.lexsort((coo.col,coo.row))
    coo_row=sparse.coo_matrix((coo.data[sortedind_row],(coo.row[sortedind_row],coo.col[sortedind_row])))
    coo_col=sparse.coo_matrix((coo.data[sortedind_col],(coo.row[sortedind_col],coo.col[sortedind_col])))
    indices_row=np.mat([coo_row.row,coo_row.col]).transpose()
    indices_col=np.mat([coo_col.row,coo_col.col]).transpose()
    stoich_tfmtx=tf.SparseTensor(indices_row,coo_row.data,coo_row.shape)
    stoich_tfmtx_col=tf.SparseTensor(indices_col,coo_col.data,coo_col.shape)
    broadcast_spmtx=reactants2spvec_spmtx(num_chems, coo_row)
    reactants_spmtxvec=tf.sparse_tensor_dense_matmul(broadcast_spmtx,reactants,name="reactants_spmtxvec")
    powed_reactants_spmtxvec=tf.pow(reactants_spmtxvec,stoich_tfmtx.values)
    normed_cols=norm_seq(coo_row.row,coo_row.col,coo_row.data)
    normed_indices=np.mat([coo_row.row,normed_cols]).transpose()
    condensed_powed_reactants_tfmtx=tf.sparse_to_dense(sparse_indices=normed_indices,
                                                       output_shape=(num_eqns,max_reactants),
                                                       sparse_values=powed_reactants_spmtxvec,
                                                       default_value=1,
                                                       name="Condensed powed reactants"
                                                       )
    reactants_prod=tf.reduce_prod(condensed_powed_reactants_tfmtx,axis=1,name="reactants prod")#Along rows
    reactants_rate_prod=tf.multiply(reactants_prod,rate_values)
    dydt=tf.sparse_tensor_dense_matmul(stoich_tfmtx_col,reactants_rate_prod,adjoint_a=True,name="dydt")
    # (((stoich_tfmtx_col: num_eqn*num_chem)^T: num_chem*num_eqn)* (reactants_rate_prod:num_eqn): num_chem) -> dydt
    #for adjoint_a=True, sparse matrix have to be sorted according to (col,row)
    return dydt