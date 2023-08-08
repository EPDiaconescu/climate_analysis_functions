
def prdistrib(num_bins, bin_bnds, fld=np.array([])):
    import numpy as np
    nr_fld = np.zeros((num_bins,1))
    prTot_fld = np.zeros((num_bins,1))
    b = bin_bnds[0]
    step = fld[fld < b]
    nr_fld[0] = step.shape[0]
    prTot_fld[0] = np.sum(step)
    for s in range(0,num_bins-2):
        b1 = bin_bnds[s]
        b2 = bin_bnds[s+1]
        step = fld[fld < b2]
        step = step[step >= b1]
        nr_fld[s+1] = step.shape[0]
        prTot_fld[s+1] = np.sum(step)
    stepf = fld[fld >= b2]
    nr_fld[s+2] = stepf.shape[0]
    prTot_fld[s+2] = np.sum(stepf)
    return nr_fld, prTot_fld

#Example: nr_fld1, prTot_fld1 = prdistrib(num_bins, bin_bnds, yyc)