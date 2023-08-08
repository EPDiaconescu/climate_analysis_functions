
import numpy as np
from matplotlib import path
from netCDF4 import Dataset
from scipy import *

def extract_contur(mask2D, X, Y):
    """
    AUTHOR: EMILIA PAULA DIACONESCU
    date: august 2017
    Function that extrare the lon and lat for the points situated on the contur of a 2D mask on a uniform grid
    mask2D=masked array
    X=a 2D uniform grid with longitudes
    Y=a 2D uniform grid with latitudes
    """

    X1=np.ma.array(X,mask=mask2D.mask)
    Y1=np.ma.array(Y,mask=mask2D.mask)
    minC=np.array(Y1.min(axis=0))
    maxC=np.array(Y1.max(axis=0))
    valLon=np.append(X[0,:],X[0,:][::-1])
    valLat=np.append(minC,maxC[::-1])
    valLatF=valLat[valLat<=90.0]
    valLonF=valLon[valLat<=90.0]
    return valLatF, valLonF


input='mask_NQ.nc'

nc = Dataset(input)
latsM = nc.variables['latitude'][:]
lonsM = nc.variables['longitude'][:]
mask2Da = nc.variables['mask_qc'][:].squeeze()
X, Y = np.meshgrid(lonsM, latsM)
lonsM = lonsM - 360
nc.close()

coords_lat, coords_lon=extract_contur(mask2Da, X, Y)
