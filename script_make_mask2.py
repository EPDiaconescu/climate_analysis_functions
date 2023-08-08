
import numpy as np
from matplotlib import path
from netCDF4 import Dataset
from scipy import *

def make_mask(coords_lon, coords_lat, lon_W,lon_E,lat_S,lat_N,nr_pointsX,nr_pointsY,output):
    """
    AUTHOR: EMILIA PAULA DIACONESCU
    date: august 2017
    Function that:
    - do a mask over a region of the glob starting from a list of longitudes and latitudes that define a polygon around the region
    - save the mask in netCDF using a regular grid defined by lon_W,lon_E,lat_S,lat_N,nr_points,output
    coords_lon = list of longitudes for the polygon around the region
    coords_lat = list of latitudes for the polygon around the region
    lon_W=the smallest longitude of the regular grid
    lon_E=the greatest longitude of the regular grid
    lat_S=the smallest latitude of the regular grid
    lat_N=the greatest latitude of the regular grid
    nr_pointsX= number of points of the regular grid for longitudes
    nr_pointsY= number of points of the regular grid for latitudes
    output=the path and name of the netCDF file for the mask
    """

    polyListx = coords_lon
    polyListy =coords_lat
    polyList = list(zip(list(polyListx),list(polyListy)))
    p = path.Path(polyList)
    lons=np.linspace(lon_W,lon_E,nr_pointsX)
    lats=np.linspace(lat_S,lat_N,nr_pointsY)
    X, Y = np.meshgrid(lons, lats)
    points = np.array((X.flatten(), Y.flatten())).T
    mask = p.contains_points(points).reshape(X.shape)
    data=np.ones(mask.shape)
    mask2D = np.ma.masked_where(mask != True, data)
    fill_value = np.nan
    mask2D = np.ma.filled(mask2D, fill_value)	

    lats_out = lats
    lons_out = lons
    nlats = nr_pointsY
    nlons = nr_pointsX

    var1_out = mask2D

    ncfile = Dataset(output, 'w')

    ncfile.createDimension('lat',nlats)
    ncfile.createDimension('lon',nlons)

    lats = ncfile.createVariable('lat',dtype('float64').char,('lat',))
    lons = ncfile.createVariable('lon',dtype('float64').char,('lon',))

    lats.units = 'degrees_north'
    lons.units = 'degrees_east'

    lats[:] = lats_out
    lons[:] = lons_out

    # create the pressure and temperature variables
    var1 = ncfile.createVariable('mask',dtype('float64').char,('lat','lon'))
    var1.units = 'steps'
    var1[:] = var1_out

    ncfile.close()

    return mask2D, X, Y

output='D:/NowWorking/test_mask.nc'
coords_lon=[-137.6,-120,-110,-98,-76,-60,-60,-60,-145,-142,-137.6]
coords_lat=[57,58,60,62,62,59.5,68,84,84,57,57]
lon_W,lon_E=(-150,-50)
lat_S,lat_N=(55,85)
nr_pointsX=200
nr_pointsY=100

mask2D, X, Y=make_mask(coords_lon, coords_lat, lon_W,lon_E,lat_S,lat_N,nr_pointsX,nr_pointsY,output)

print('the mask mask2D(X,Y) saved in '+output)