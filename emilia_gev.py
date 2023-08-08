
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import abs
from scipy.stats import genextreme, kstest
import scipy.special
import scipy as _sp


def returnLevBlockMax(data,rp,outputImg='None'):
    """ Estimate the parameters for the GEV by maximum likelihood
    and compute the return levels for one samples of anual maxima and a series of return periods.

    Parameters
    ----------
    data : a pandas series of anual maxima over a period of years.
    rp : serie of return periods

    Returns
    -------
    ksSt, p1: Kolmogorov-Smirnov statistic between data and the fitted GEV and the coresponding p-val
    DK, p2  : Kuiper statistic between data and the fitted GEV and the coresponding p-val
    retLev      : series with the return levels coresponding to rp

    """
    # fit GEV distribution to data
    shp, loc, scl = genextreme.fit(data)
    ksSt=kstest(data, 'genextreme', genextreme.fit(data))
    # Generate random numbers for the GEV
    r = genextreme.rvs(shp, loc, scl, size=1000)
    # compute quantiles
    x=(pd.DataFrame(r)).quantile(np.linspace(0.0, 1.0, num=201))
    y=data.quantile(np.linspace(0.0, 1.0, num=201))
    # compute the return levels
    retLev = [genextreme.ppf([1.0 - (1.0 / tt)], shp, loc, scl)[0] for tt in rp]

    if outputImg!='None':
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        valmin=round(x.min()-(x.max()-x.min())/4)
        valmax=round(x.max()+(x.max()-x.min())/4)
        ax1.scatter(x, y, s=60, marker="o", edgecolor="r", c='red')
        plt.plot(np.array([valmin, valmax]),np.array([valmin, valmax]) , 'k--')
        plt.xlim([valmin, valmax])
        plt.ylim([valmin, valmax])
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        ax1.set_ylabel('Quantiles in observations',fontsize=16)
        ax1.set_xlabel('Quantiles from GEV',fontsize=16)
        plt.legend(loc=1, fontsize=16)
        plt.tight_layout()
        plt.savefig(outputImg)
        fig.clf()


    return ksSt, shp, loc, scl, retLev


def quagev(F,para):
    U = para[0]
    A = para[1]
    G = para[2]
    if A <= 0:
        print("Parameters Invalid")
        return
    if F <= 0 or F >= 1:
        if F == 0 and G < 0:
            QUAGEV = U+A/G
        elif F == 1 and G > 0:
            QUAGEV = U+A/G
        else:
            print("F Value Invalid")
            return


        print("F Value Invalid")
        return
    else:
        Y = -_sp.log(-_sp.log(F))
        if G != 0:
            Y = (1-_sp.exp(-G*Y))/G
        QUAGEV = U+A*Y
        return(QUAGEV)

def comb(N,k,exact=1):
    if exact:
        if (k > N) or (N < 0) or (k < 0):
            return 0
        val = 1
        for j in xrange(min(k, N-k)):
            val = (val*(N-j))//(j+1)
        return val
    else:
        from scipy import _special
        k,N = _sp.asarray(k), _sp.asarray(N)
        lgam = _special.gammaln
        cond = (k <= N) & (N >= 0) & (k >= 0)
        sv = _special.errprint(0)
        vals = _sp.exp(lgam(N+1) - lgam(N-k+1) - lgam(k+1))
        sv = _special.errprint(sv)
        return _sp.where(cond, vals, 0.0)


def samlmu(x,nmom=5):
    x = sorted(x)
    n = len(x)
    ##Calculate first order
    ##Pretty efficient, no loops
    coefl1 = 1.0/comb(n,1)
    suml1 = sum(x)
    l1 = coefl1*suml1

    if nmom == 1:
        ret = l1
        return(ret)

    ##Calculate Second order

    #comb terms appear elsewhere, this will decrease calc time
    #for nmom > 2, and shouldn't decrease time for nmom == 2
    #comb1 = comb(i-1,1)
    #comb2 = comb(n-i,1)
    comb1 = []
    comb2 = []
    for i in range(1,n+1):
        comb1.append(comb(i-1,1))
        comb2.append(comb(n-i,1))

    coefl2 = 0.5 * 1.0/comb(n,2)
    xtrans = []
    for i in range(1,n+1):
        coeftemp = comb1[i-1]-comb2[i-1]
        xtrans.append(coeftemp*x[i-1])

    l2 = coefl2 * sum(xtrans)

    if nmom  ==2:
        ret = [l1,l2]
        return(ret)

    ##Calculate Third order
    #comb terms appear elsewhere, this will decrease calc time
    #for nmom > 2, and shouldn't decrease time for nmom == 2
    #comb3 = comb(i-1,2)
    #comb4 = comb(n-i,2)
    comb3 = []
    comb4 = []
    for i in range(1,n+1):
        comb3.append(comb(i-1,2))
        comb4.append(comb(n-i,2))

    coefl3 = 1.0/3 * 1.0/comb(n,3)
    xtrans = []
    for i in range(1,n+1):
        coeftemp = (comb3[i-1]-
                    2*comb1[i-1]*comb2[i-1] +
                    comb4[i-1])
        xtrans.append(coeftemp*x[i-1])

    l3 = coefl3 *sum(xtrans) /l2

    if nmom  ==3:
        ret = [l1,l2,l3]
        return(ret)

    ##Calculate Fourth order
    #comb5 = comb(i-1,3)
    #comb6 = comb(n-i,3)
    comb5 = []
    comb6 = []
    for i in range(1,n+1):
        comb5.append(comb(i-1,3))
        comb6.append(comb(n-i,3))

    coefl4 = 1.0/4 * 1.0/comb(n,4)
    xtrans = []
    for i in range(1,n+1):
        coeftemp = (comb5[i-1]-
                    3*comb3[i-1]*comb2[i-1] +
                    3*comb1[i-1]*comb4[i-1] -
                    comb6[i-1])
        xtrans.append(coeftemp*x[i-1])

    l4 = coefl4 *sum(xtrans)/l2

    if nmom  ==4:
        ret = [l1,l2,l3,l4]
        return(ret)

    ##Calculate Fifth order
    coefl5 = 1.0/5 * 1.0/comb(n,5)
    xtrans = []
    for i in range(1,n+1):
        coeftemp = (comb(i-1,4)-
                    4*comb5[i-1]*comb2[i-1] +
                    6*comb3[i-1]*comb4[i-1] -
                    4*comb1[i-1]*comb6[i-1] +
                    comb(n-i,4))
        xtrans.append(coeftemp*x[i-1])

    l5 = coefl5 *sum(xtrans)/l2

    if nmom ==5:
        ret = [l1,l2,l3,l4,l5]
        return(ret)


def pelgev(xmom):
    SMALL = 1e-5
    eps = 1e-6
    maxit = 20
    EU =0.57721566
    DL2 = _sp.log(2)
    DL3 = _sp.log(3)
    A0 =  0.28377530
    A1 = -1.21096399
    A2 = -2.50728214
    A3 = -1.13455566
    A4 = -0.07138022
    B1 =  2.06189696
    B2 =  1.31912239
    B3 =  0.25077104
    C1 =  1.59921491
    C2 = -0.48832213
    C3 =  0.01573152
    D1 = -0.64363929
    D2 =  0.08985247

    T3 = xmom[2]
    if xmom[1]<= 0 or abs(T3)>= 1:
        print("L-Moments Invalid")
        return
    if T3<= 0:
        G=(A0+T3*(A1+T3*(A2+T3*(A3+T3*A4))))/(1+T3*(B1+T3*(B2+T3*B3)))
        if T3>= -0.8:
            para3 = G
            GAM = _sp.exp(scipy.special.gammaln(1+G))
            para2=xmom[1]*G/(GAM*(1-2**(-G)))
            para1=xmom[0]-para2*(1-GAM)/G
            para = [para1,para2,para3]
            return(para)

        if T3 <= -0.97:
            G = 1-_sp.log(1+T3)/DL2

        T0=(T3+3)*0.5
        for IT in range(1,maxit):
            X2=2**(-G)
            X3=3**(-G)
            XX2=1-X2
            XX3=1-X3
            T=XX3/XX2
            DERIV=(XX2*X3*DL3-XX3*X2*DL2)/(XX2**2)
            GOLD=G
            G=G-(T-T0)/DERIV
            if abs(G-GOLD) <= eps*G:
                para3 = G
                GAM = _sp.exp(scipy.special.gammaln(1+G))
                para2=xmom[1]*G/(GAM*(1-2**(-G)))
                para1=xmom[0]-para2*(1-GAM)/G
                para = [para1,para2,para3]
                return(para)

        print("Iteration has not converged")

    Z=1-T3
    G=(-1+Z*(C1+Z*(C2+Z*C3)))/(1+Z*(D1+Z*D2))
    if abs(G)<SMALL:
        para2 = xmom[1]/DL2
        para1 = xmom[0]-EU*para2
        para = [para1,para2,0]
        return(para)
    else:
        para3 = G
        GAM = _sp.exp(scipy.special.gammaln(1+G))
        para2=xmom[1]*G/(GAM*(1-2**(-G)))
        para1=xmom[0]-para2*(1-GAM)/G
        para = [para1,para2,para3]
        return(para)


def returnLevBlockMaxLM(data,rp,outputImg='None'):
    """ Estimate the parameters for the GEV using L-moments
    and compute the return levels for one samples of anual maxima and a series of return periods.

    Parameters
    ----------
    data : a pandas series of anual maxima over a period of years.
    rp : serie of return periods

    Returns
    -------
    ksSt, p1: Kolmogorov-Smirnov statistic between data and the fitted GEV and the coresponding p-val
    DK, p2  : Kuiper statistic between data and the fitted GEV and the coresponding p-val
    retLev      : series with the return levels coresponding to rp

    """
    # fit GEV distribution to data
    loc, scl, shp = pelgev(samlmu(data,3))
    ksSt=kstest(data, 'genextreme', (shp, loc, scl))
    r=[quagev(k,(loc, scl, shp)) for k in np.linspace(0.0, 1.0, num=201)]
    x=pd.DataFrame(r)
    x.index=np.linspace(0.0, 1.0, num=201)
    y=data.quantile(np.linspace(0.0, 1.0, num=201))
    # compute the return levels
    retLev = [genextreme.ppf([1.0 - (1.0 / tt)], shp, loc, scl)[0] for tt in rp]

    if outputImg!='None':
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        valmin=round(x.min()-(x.max()-x.min())/4)
        valmax=round(x.max()+(x.max()-x.min())/4)
        ax1.scatter(x, y, s=60, marker="o", edgecolor="b", c='blue')
        plt.plot(np.array([valmin, valmax]),np.array([valmin, valmax]) , 'k--')
        plt.xlim([valmin, valmax])
        plt.ylim([valmin, valmax])
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        ax1.set_ylabel('Quantiles in observations',fontsize=16)
        ax1.set_xlabel('Quantiles from GEV',fontsize=16)
        plt.legend(loc=1, fontsize=16)
        plt.tight_layout()
        plt.savefig(outputImg)
        fig.clf()


    return ksSt, shp, loc, scl, retLev

