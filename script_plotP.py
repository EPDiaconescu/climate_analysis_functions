

from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib  as mpl
from matplotlib.colors import Normalize
from scipy import *


def mf1(data):
    return (float('{:.1f}'.format(data)))

def mf2(data):
    return (float('{:.2f}'.format(data)))

def plotP(inCentral,lonCentral,latCentral,lonMask,latMask,levels,tCentral,txtLabel,imgout):
    colors = mpl.colors.ListedColormap ([(0.0, 0.070588235294117674, 0.28627450980392155),
                                        (0.0, 0.14117647058823535, 0.4274509803921569),
                                        (0.0, 0.21176470588235285, 0.47450980392156861),
                                        (0.0, 0.35882352941176465, 0.5725490196078431),
                                        (0.0, 0.42941176470588238, 0.61960784313725492),
                                        (0.14117647058823524, 0.57058823529411762, 0.71372549019607845),
                                        (0.26013072828451794, 0.65098041296005249, 0.80000001192092896),
                                        (0.34117648005485535, 0.72156864404678345, 0.81568628549575806),
                                        (0.52941177090009051, 0.81777778863906858, 0.75294119119644165),
                                        (0.70588237047195435, 0.88496732711791992, 0.73071897029876709),
                                        (0.83137255907058716, 0.93411765098571775, 0.80705883502960207),
                                        [ 1.        ,  1.0,  1.0],
                                        [ 0.99607843,  0.87843137,  0.82352941],
                                        [0.99, 0.8, 0.7],
                                        [ 0.98823529,  0.73333333,  0.63137255],
                                        [ 0.98823529,  0.57254902,  0.44705882],
                                        [ 0.98431373,  0.41568627,  0.29019608],
                                        [ 0.9372549 ,  0.23137255,  0.17254902],
                                        [ 0.79607843,  0.09411765,  0.11372549],
                                        [ 0.64705882,  0.05882353,  0.08235294],
                                        [0.5, 0., 0.06],
                                        [ 0.40392157,  0.        ,  0.05098039],
                                        [0.2783814132520015, 0.0, 0.0]])

    norm = mpl.colors.BoundaryNorm(levels, len(levels)-1)
    f = plt.figure(figsize=(10,7))
    m = Basemap(resolution='l',llcrnrlon=-130.0,llcrnrlat=40.0,urcrnrlon=-22.00,urcrnrlat=55.0,projection='cass',lat_0=63,lon_0=-105.)
    m.drawcountries(linewidth=0.5,color=[0.4,0.4,0.4])
    m.drawcoastlines(linewidth=0.5,color=[0.4,0.4,0.4])
    m.drawlsmask(land_color='0.8', ocean_color=(0.77647059,  0.85882353,  0.9372549), lakes=True)
    x,y = m(lonCentral,latCentral)
    xS,yS = m(lonMask,latMask)
    im=m.pcolormesh(x,y,inCentral,cmap=colors, latlon=False,norm=norm)
    plt.title(tCentral, size=18)
    m.plot(xS,yS, 'k|', markersize=4)
    c = plt.colorbar(im, fraction=0.046, pad=0.04, orientation='vertical', extend='both',extendfrac='auto')
    c.set_label(txtLabel, size=14)
    c.set_ticks(levels)
    font_size = 12 # Adjust as appropriate.
    c.ax.set_xticklabels(levels)
    c.ax.tick_params(labelsize=font_size)
    f.savefig(imgout, dpi=400)
    plt.close()



mask='D:/NowWorking/newProjet_2017/results_Canada/mask_Canada_grilleAgMERRA.nc'
setData='Canada'
rcp='rcp45'
periode='2040to2064'
#periode='2076to2100'

input= 'D:/NowWorking/newProjet_2017/data_models/delta_'+rcp+'_Ensemble_Canada2_AgMERRA_nn/'
nc = Dataset(mask)
latsM = nc.variables['latitude'][:]
lonsM = nc.variables['longitude'][:]
dataM = nc.variables['tas'][:].squeeze()
lonsM, latsM = np.meshgrid(lonsM, latsM)
lonsM = lonsM - 360
nc.close()

list_var=['CDD18', 'DebutSC','DSDmax','EDCSC2','FD' ,'FDD', 'Fhiv','FinSC','frsn_anual','GDD5','HDD17', 'ID','LonSC',
          'NGD', 'pc95Aalld', 'pc99Aalld', 'pr1mm', 'pr1mmRainW1', 'pr1mmSnow', 'pr_djfMean', 'pr_jjaMean', 'prAnualMean',
          'prNr_p95Wet', 'prNr_p99Wet','prsnAnualMean','prsnTot_anual','prTot_anual','prTotRainW',
          'R95pWet', 'R99pWet', 'rl_10yy','rl_20yy','rl_2yy','rl_5yy','rx1day', 'rx1daySnow','rx5day',
          'SCD','SDCSC','SDmax','SED', 'SSD', 'SSL','SU10', 'SU15', 'SU25','tas_djfMean','tas_jjaMean','tasAnualMean',
          'TDD','TN10_anual','TN10p', 'TN90_anual', 'TN90p', 'TNn', 'TNx', 'TR5','TR10', 'TR20','TX10_anual', 'TX10p',
          'TX90_anual', 'TX90p', 'TXn', 'TXx']

for varName in list_var:
    if varName=='CDD18' and \
       varName=='FDD' and \
       varName=='GDD5' and \
       varName=='TDD' and \
       varName=='HDD17':
        units=' [degree days]'
    elif varName=='tas_djfMean' and \
       varName=='tas_jjaMean' and \
       varName=='tasAnualMean' and \
       varName=='TN10_anual' and \
       varName=='TN90_anual' and \
       varName=='TNn' and \
       varName=='TNx' and \
       varName=='TX10_anual' and \
       varName=='TX90_anual' and \
       varName=='TXn' and \
       varName=='TXx':
        units=' [$^\circ$C]'
    elif varName=='frsn_anual':
        units='  '
    elif varName=='TN10p' and \
       varName=='TX10p' and \
       varName=='TX90p' and \
       varName=='TX90p':
        units=' [%]'
    elif varName=='prsnTot_anual' and \
       varName=='prTot_anual' and \
       varName=='R95pWet' and \
       varName=='R99pWet' and \
       varName=='prNrPc_p99Wet' and \
       varName=='prTotRainW':
        units=' [mm]'
    elif varName=='pc95Aalld' and \
       varName=='pc99Aalld' and \
       varName=='pr_djfMean' and \
       varName=='R99pWet' and \
       varName=='pr_jjaMean' and \
       varName=='prAnualMean' and \
       varName=='prsnAnualMean' and \
       varName=='R95pTotWet' and \
       varName=='R99pTotWet' and \
       varName=='rx1daySnow' and \
       varName=='rx1day' and \
       varName=='rl_2yy' and \
       varName=='rl_5yy' and \
       varName=='rl_20yy' and \
       varName=='rl_10yy' and \
       varName=='rx5day':
        units=' [mm/day]'
    else:
        units=' [days]'

    txtLabel='  '
    output='D:/NowWorking/newProjet_2017/results_Canada/imades_delta_mediane/'+varName+'_'+setData+'_'+rcp+'_delta_Mediane_'+periode+'.png'

    #####################################################################################################

    nc = Dataset(input+'AllVar_Canada_mediane_'+rcp+'_delta_'+periode+'Mean_CORDEX.nc')
    lats0 = nc.variables['latitude'][:]
    lons0 = nc.variables['longitude'][:]
    lons0, lats0 = np.meshgrid(lons0, lats0)
    data0 = nc.variables[varName][:].squeeze()
    data0=data0
    lons0 = lons0 - 360
    nc.close()


    nc = Dataset(input+'AllVar_sig90Models_delta_'+periode+'_'+rcp+'_Canada_mk.nc')
    latsS = nc.variables['latitude'][:]
    lonsS = nc.variables['longitude'][:]
    dataS = nc.variables[varName][:].squeeze()
    lonsS = lonsS - 360
    nc.close()

    fill_value = 1.0
    dataS = np.ma.filled(dataS, fill_value)

    dataI=dataS[0,:]
    dataNew=np.array([dataI[2*k] for k in range((dataI.shape[0])/2)])
    for i in [2*k for k in range(1,(dataS.shape[0])/2)]:
        dataI=dataS[i,:]
        dataNew0=np.array([dataI[2*k] for k in range((dataI.shape[0])/2)])
        dataNew=np.vstack((dataNew,dataNew0))

    Xnew = np.array([lonsS[2*k] for k in range((lonsS.shape[0])/2)])
    Ynew = np.array([latsS[2*k] for k in range((latsS.shape[0])/2)])
    Xnew, Ynew = np.meshgrid(Xnew, Ynew)

    for i in range(0,32):
        for j in [2*k for k in range(1,(dataNew.shape[1])/2)]:
            dataNew[i,j]=1.0

    m=dataNew==1.0
    lonsSS=ma.array(Xnew,mask=m)
    latsSS=ma.array(Ynew,mask=m)

    val1=np.max([abs(np.min(data0+dataM)),abs(np.max(data0+dataM))])

    if val1<1.0:
        valExt=mf2(val1)
        pasul=mf2(valExt/12)
        lev1=(((np.arange(pasul/2.0,25*pasul/2.0,pasul))*(-1))[::-1])
        lev2=np.arange(pasul/2.0,25*pasul/2.0,pasul)
        clevs=np.append(lev1,lev2)
    elif val1<12.0:
        valExt=mf1(val1)
        pasul=mf1(valExt/12)
        lev1=(((np.arange(pasul/2.0,25*pasul/2.0,pasul))*(-1))[::-1])
        lev2=np.arange(pasul/2.0,25*pasul/2.0,pasul)
        clevs=np.append(lev1,lev2)
    else:
        valExt=np.int(val1)
        pasul=valExt/12
        lev1=(((np.arange(pasul/2.0,25*pasul/2.0,pasul))*(-1))[::-1])
        lev2=np.arange(pasul/2.0,25*pasul/2.0,pasul)
        clevs=np.append(lev1,lev2)

    norm = mpl.colors.BoundaryNorm(clevs, len(clevs)-1)

    plotP(data0+dataM,lons0-0.11,lats0+0.11,lonsSS,latsSS,clevs,txtLabel,' ',output)


print('FINISH')
#####################################################################################################

