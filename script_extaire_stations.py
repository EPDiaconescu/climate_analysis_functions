
from netCDF4 import Dataset
import numpy as np
import pandas as pd
from scipy import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from shapely.geometry import Polygon,Point, MultiPoint


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


def extract_stations(df_st, coords_lon,coords_lat):
	lonsSt00=np.array(df_st.iloc[-2,:], dtype=float)
	latsSt00=np.array(df_st.iloc[-1,:], dtype=float)
	lonsSt, latsSt, zst = lon_lat_to_cartesian(lonsSt00,latsSt00)
	
	xt, yt, zt = lon_lat_to_cartesian(coords_lon,coords_lat)
	coords = zip(xt,yt)
	poly = MultiPoint(coords).convex_hull
	for i in range(0,lonsSt.shape[0]):
		point = Point(lonsSt[i],latsSt[i])
		if poly.contains(point)==False:
			lonsSt00[i]=nan
	new_lons0=lonsSt00[np.isfinite(lonsSt00)]
	new_lats0=latsSt00[np.isfinite(lonsSt00)]
	new_ec0=np.array((df_st.columns.tolist()))[np.isfinite(lonsSt00)]
	new_df=df_st[new_ec0]

	return new_lons0, new_lats0, new_ec0, new_df


	
domeniu='ArcB'
input_obs= 'D:/NowWorking/newProjet_2017/data_stations/validYY_stations/validYY_prsn_ECstations2/'
input_st= 'D:/NowWorking/newProjet_2017/data_stations/'

df_a=np.loadtxt(input_st+'stations_id.txt', dtype=str, skiprows=0)
df_a_lat=np.loadtxt(input_st+'stations_lat.txt', dtype=float, skiprows=0)
df_a_lon=np.loadtxt(input_st+'stations_lon.txt', dtype=float, skiprows=0)
df_st=pd.DataFrame(np.vstack([df_a_lon,df_a_lat]))
df_st.index=['lon', 'lat']
df_st.columns=df_a

coords_lon=[-137.6,-120,-110,-98,-76,-60,-60,-60,-145,-142,-137.6]
coords_lat=[57,58,60,62,62,59.5,68,84,84,57,57]
	
new_lons,new_lats,new_ec, new_df=extract_stations(df_st, coords_lon,coords_lat)

fig1 = plt.figure(figsize=(11,8.5))
plt.subplots_adjust(left=0.02,right=0.98,top=0.90,bottom=0.10,wspace=0.05,hspace=0.05)
width = 6000000; height=4000000; lon_0 = -92; lat_0 = 75
m = Basemap(resolution='l',width=width,height=height,projection='aeqd', lat_0=lat_0,lon_0=lon_0)

m.drawcoastlines()
m.drawcountries(linewidth=1)
m.drawmeridians(np.arange(-180,180,20), linewidth=0.2)
m.drawparallels(np.arange(40,90,10),linewidth=0.2)
x0, y0 = m(np.array(df_st.iloc[-2,:]), np.array(df_st.iloc[-1,:]))
x, y = m(new_lons,new_lats)
m.plot(x0, y0, 'bo', markersize=18, lw = 0, markeredgecolor='w' )
m.plot(x, y, 'ro', markersize=10, lw = 0, markeredgecolor='w' )
plt.show()