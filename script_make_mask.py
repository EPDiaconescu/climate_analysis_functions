
from netCDF4 import Dataset
import numpy as np
from scipy import *
from shapely.geometry import Point, MultiPoint


def make_mask(coords_lon,coords_lat, lon_W,lon_E,lat_S,lat_N,nr_pointsX,nr_pointsY,output):
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

    def lon_lat_to_cartesian(lon, lat, R = 1):
        """
        calculates lon, lat coordinates of a point on a sphere with
        radius R
        """
        lon_r = np.radians(lon)
        lat_r = np.radians(lat)

        x =  R * np.cos(lat_r) * np.cos(lon_r)
        y = R * np.cos(lat_r) * np.sin(lon_r)
        z = R * np.sin(lat_r)
        return x,y,z

    X,Y = np.meshgrid(np.linspace(lon_W,lon_E,nr_pointsX), np.linspace(lat_S,lat_N,nr_pointsY))
    lonsSt00=X.flatten()
    latsSt00=Y.flatten()
    points_0=np.append([lonsSt00], [latsSt00], axis=0)

    xt, yt, zt = lon_lat_to_cartesian(coords_lon,coords_lat)
    coords = zip(xt,yt)
    poly = MultiPoint(coords).convex_hull
    lonsSt, latsSt, zst = lon_lat_to_cartesian(lonsSt00,latsSt00)

    for i in range(0,lonsSt.shape[0]):
        point = Point(lonsSt[i],latsSt[i])
        if poly.contains(point)==False:
            lonsSt00[i]=nan

    mask=lonsSt00-lonsSt00+1
    mask2D=mask.reshape(nr_pointsX,nr_pointsY)

    # open a new netCDF file for writing.
    lats_out = np.linspace(lat_S,lat_N,nr_pointsY)
    lons_out = np.linspace(lon_W,lon_E,nr_pointsX)
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

