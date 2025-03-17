__author__ = 'emiliapauladiaconescu'



import pandas as pd
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import vstack, hstack
from pylab import  xticks, yticks

# Define the shapes of the triangles
def get_triB(xoff=0, yoff=0):
    verts = [(0.0 + xoff, 0.0 + yoff),
        (1.0 + xoff, 0.0 + yoff),
        (1.0 + xoff, 1.0 + yoff),
        (0.0 + xoff, 0.0 + yoff)]
    p = mpath.Path(verts, [mpath.Path.MOVETO] + (len(verts)-1)*[mpath.Path.LINETO])
    return p

def get_triH(xoff=0, yoff=0):
    verts = [(0.0 + xoff, 0.0 + yoff),
        (1.0 + xoff, 1.0 + yoff),
        (0.0 + xoff, 1.0 + yoff),
        (0.0 + xoff, 0.0 + yoff)]
    p = mpath.Path(verts, [mpath.Path.MOVETO] + (len(verts)-1)*[mpath.Path.LINETO])
    return p

# Define the shapes of the triangles
def get_triB2(xoff=0, yoff=0):
    verts = [(0.0 + xoff, 0.0 + yoff),
        (2.0 + xoff, 0.0 + yoff),
        (2.0 + xoff, 2.0 + yoff),
        (0.0 + xoff, 0.0 + yoff)]
    p = mpath.Path(verts, [mpath.Path.MOVETO] + (len(verts)-1)*[mpath.Path.LINETO])
    return p

def get_triH2(xoff=0, yoff=0):
    verts = [(0.0 + xoff, 0.0 + yoff),
        (2.0 + xoff, 2.0 + yoff),
        (0.0 + xoff, 2.0 + yoff),
        (0.0 + xoff, 0.0 + yoff)]
    p = mpath.Path(verts, [mpath.Path.MOVETO] + (len(verts)-1)*[mpath.Path.LINETO])
    return p

domeniu='ARCcordex'
periode='1980to2004'
ValnrYY='15'
statistique='sptpAnom'
extrems='ALL'

input= 'D:/NowWorking/newProjet/results/domARC_CORDEX_b/KuiperPerkins_anom2_sptp_ref/KuiperPerkinsVal/'
input2= 'D:/NowWorking/newProjet/results/domARC_CORDEX_b/KuiperPerkinsALL_anom_sptp_ref/KuiperPerkinsVal/'
output='D:/NowWorking/newProjet/results/domARC_CORDEX_b/performanceKuiperPerkinsALL_Anom2_ref_C/'

ax_var=['tasAnualMean','HDD17', 'GDD5', 'SU15','TXx_K','TX90_K','TX90p','FD','TNn_K','TN10_K', 'TN10p','prAnualMean', 'pr1mm','rx1day','rx5days','PrTotPc_GTp95','PrCum_GTp95','PrTotPc_GTp99', 'PrCum_GTp99']
ax_var2=['tas','HDD17', 'GDD5', 'SU15','TXx_K','TX90_K','TX90p','FD','TNn_K','TN10_K', 'TN10p','pr', 'pr1mm','rx1day','rx5days','PrTotPc_GTp99','PrCum_GTp95','PrTotPc_GTp99', 'PrCum_GTp99']

ax_ox=['Mean Tmean','HDD', 'GDD','SU15', 'TXx', 'TX90', 'TX90p','FD','TNn', 'TN10', 'TN10p','Mean Pr', 'R1mm','RX1day','RX5day','R95p','R95pTOT', 'R99p','R99pTOT']
ax_ox2=['Mean Tmean','HDD', 'GDD','SU15', 'TXx', 'TX90', 'TX90p','FD','TNn', 'TN10', 'TN10p','Mean Pr', 'R1mm','Rx1day','Rx5day','R95p','R95pTOT', 'R99p', 'R99pTOT', ' ','All T', 'All Pr']

ax_oySS=['All T', 'All Pr']
ax_oxSS=['Combined reanalyses', 'Combined simulations']
ax_oy=['NRCan', 'GMFD', 'CFSR', 'MERRA','JRA-55','ERAI', 'SMHI-RCA4SN-MPI-ESM-LR', 'SMHI-RCA4-MPI-ESM-LR','SMHI-RCA4SN-EC-EARTH',
       'SMHI-RCA4-EC-EARTH','SMHI-RCA4-NorESM1-M', 'SMHI-RCA4-CanESM2','UQAM-CRCM5NA-CanESM2','UQAM-CRCM5NA-MPI-ESM-LR ',
       'UQAM-CRCM5-MPI-ESM-LR',  'CCCma-CanRCM4-CanESM2', 'CCCma-CanRCM4-CanESM2-022','AWI-HIRHAM5-MPI-ESM-LR']
ax_oy2=['NRCan', 'GMFD', 'CFSR', 'MERRA','JRA-55','ERAI', 'SMHI-RCA4SN-MPI-ESM-LR', 'SMHI-RCA4-MPI-ESM-LR','SMHI-RCA4SN-EC-EARTH',
       'SMHI-RCA4-EC-EARTH','SMHI-RCA4-NorESM1-M', 'SMHI-RCA4-CanESM2','UQAM-CRCM5NA-CanESM2','UQAM-CRCM5NA-MPI-ESM-LR ',
       'UQAM-CRCM5-MPI-ESM-LR',  'CCCma-CanRCM4-CanESM2', 'CCCma-CanRCM4-CanESM2-022','AWI-HIRHAM5-MPI-ESM-LR', '', 'Combined reanalyses', 'Combined simulations']

arrK = np.zeros(18)
arrP = np.zeros(18)

for varName in ax_var:
       matricea1=input+varName+'AnualMean_KuiperPerkinsMatrix_'+domeniu+'_'+ValnrYY+'noYY_'+periode+'_'+statistique+'.csv'
       df_mat0 = pd.read_csv(matricea1, sep=',')
       tab1=df_mat0.iloc[:7,:]
       tab2=tab1.append(df_mat0.iloc[18,:])
       tab3=tab2.append(df_mat0.iloc[17,:])
       tab4=tab3.append(df_mat0.iloc[16,:])
       tab5=tab4.append(df_mat0.iloc[15,:])
       tab6=tab5.append(df_mat0.iloc[14,:])
       tab7=tab6.append(df_mat0.iloc[13,:])
       tab8=tab7.append(df_mat0.iloc[12,:])
       tab9=tab8.append(df_mat0.iloc[11,:])
       tab10=tab9.append(df_mat0.iloc[10,:])
       tab11=tab10.append(df_mat0.iloc[9,:])
       tab12=tab11.append(df_mat0.iloc[8,:])
       df_mat1=tab12.append(df_mat0.iloc[7,:])

       Dval1=np.array(df_mat1.iloc[1:,1])
       Pval1=np.array(df_mat1.iloc[1:,2])
       arrK = vstack((arrK, Dval1))
       arrP = vstack((arrP, Pval1))


Rt_K=arrK[1:,:]
Rb_P=arrP[1:,:]

Rt_KT=(Rt_K[:11,:]).mean(axis=0)
Rt_KPr=(Rt_K[11:,:]).mean(axis=0)
Rt_KSS=vstack((Rt_KT,Rt_KPr))

Rb_PT=(Rb_P[:11,:]).mean(axis=0)
Rb_PPr=(Rb_P[11:,:]).mean(axis=0)
Rb_PSS=vstack((Rb_PT,Rb_PPr))


arrKss = np.zeros(2)
arrPss = np.zeros(2)

for varName in ax_var2:
       matricea2=input2+varName+'AnualMean_KuiperPerkinsMatrix_'+domeniu+'_'+ValnrYY+'noYY_'+periode+'_'+statistique+'.csv'
       df_mat2 = pd.read_csv(matricea2, sep=',')
       Dval2=np.array(df_mat2.iloc[:,1])
       Pval2=np.array(df_mat2.iloc[:,2])
       arrKss = vstack((arrKss, Dval2))
       arrPss = vstack((arrPss, Pval2))

Rt_ss=arrKss[1:,:]
Rb_ss=arrPss[1:,:]


cgbvr1 = mpl.colors.ListedColormap (['Ivory',
                                     (1.0, 1.0, 0.64485258602905671),
                                     (1.0, 1.0, 0.2897051720581133),
                                     (1.0, 0.70931353118904128, 0.0),
                                     (1.0, 0.47254921004871014, 0.0),
                                     (1.0, 0.23578488890837906, 0.0),
                                     (0.99902049706244078, 0.0, 0.0),
                                     (0.75194423975600444, 0.0, 0.0),
                                     (0.51516282650400291, 0.0, 0.0),
                                     (0.2783814132520015, 0.0, 0.0)])
cgbvr1 = mpl.colors.ListedColormap (['Ivory',
                                     (0.99260284550049727, 0.81413303683785831, 0.73837756269118371),
                                     (0.98823529481887817, 0.70685122854569382, 0.60101501310572902),
                                     (0.98823529481887817, 0.58579010542701271, 0.46223760562784533),
                                     (0.98572856678682219, 0.47227990475355408, 0.34678970540271087),
                                     (0.96733564208535583, 0.34918877716157948, 0.24775087471101798),
                                     (0.92562860881581022, 0.22006920532268637, 0.16770473324200685),
                                     (0.81933103729696832, 0.11672433851396335, 0.12341407283264048),
                                     (0.71309498057645904, 0.074463668757793949, 0.096255288141615256),
                                     (0.57936180070334786, 0.042445213537590176, 0.073617841317957525)])

shapes_B = [get_triB(xoff=x, yoff=y) for i in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0] for j in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0] for x,y in [(i, j)]]
shapes_H = [get_triH(xoff=x, yoff=y) for i in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0] for j in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0] for x,y in [(i, j)]]

shapes_B2 = [get_triB(xoff=x+20, yoff=y) for i in [0.0, 1.0] for j in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0] for x,y in [(i, j)]]
shapes_H2 = [get_triH(xoff=x+20, yoff=y) for i in [0.0, 1.0] for j in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0] for x,y in [(i, j)]]

shapes_B3 = [get_triB(xoff=x, yoff=y+19) for i in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0] for j in [0.0, 1.0] for x,y in [(i, j)]]
shapes_H3 = [get_triH(xoff=x, yoff=y+19) for i in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0] for j in [0.0, 1.0] for x,y in [(i, j)]]


A_2=[(1.0, 1.0, 0.9411764705882353, 1.0),
 (0.99717031927669753, 0.92618224200080423, 0.82362169448067157),
 (0.99215686321258545, 0.81522492450826312, 0.60281432586557726, 1.0),
 (0.99215686321258545, 0.74140716650906735, 0.5260438575464137, 1.0),
 (0.98965013518052947, 0.61802385975332819, 0.40985776314548417, 1.0),
 (0.96984237011741192, 0.4963475778991101, 0.32496733069419859, 1.0),
 (0.92950404111076801, 0.37896194370353925, 0.26911189196740881, 1.0),
 (0.85863899343154015, 0.22246828552554634, 0.14805075201918097, 1.0),
 (0.76452135198256554, 0.083414073142350886, 0.053871587941459576, 1.0),
 (0.6451826349192975, 0.0, 0.0, 1.0)]
A_2_av=[(1.0, 1.0, 0.9411764705882353, 1.0),
        (1.0, 1.0, 0.6448525860290567, 1.0),
      (1.0, 1.0, 0.2897051720581133, 1.0),
      (1.0, 0.7093135311890413, 0.0, 1.0),
      (1.0, 0.47254921004871014, 0.0, 1.0),
      (1.0, 0.23578488890837906, 0.0, 1.0),
      (0.9990204970624408, 0.0, 0.0, 1.0),
      (0.7519442397560044, 0.0, 0.0, 1.0),
      (0.5151628265040029, 0.0, 0.0, 1.0),
      (0.2783814132520015, 0.0, 0.0, 1.0)]

cgbvr2 = mpl.colors.ListedColormap (A_2)

####figure ###################
W_B=Rb_P.flatten()
W_H=Rt_K.flatten()

W_B2=Rb_PSS.flatten()
W_H2=Rt_KSS.flatten()

W_B3=Rb_ss.flatten()
W_H3=Rt_ss.flatten()


cmap=cgbvr2

colors_B = cgbvr2(W_B*2)
colors_H = cgbvr2(W_H*2)

colors_B2 = cgbvr2(W_B2*2)
colors_H2 = cgbvr2(W_H2*2)

colors_B3 = cgbvr2(W_B3*2)
colors_H3 = cgbvr2(W_H3*2)

fig, ax = plt.subplots(figsize=(24,22), subplot_kw={'aspect': 1.0})

coll_B = mpl.collections.PathCollection(shapes_B, facecolor=colors_B, linewidth=0.5)
coll_H = mpl.collections.PathCollection(shapes_H, facecolor=colors_H, linewidth=0.5)

coll_B2 = mpl.collections.PathCollection(shapes_B2, facecolor=colors_B2, linewidth=0.5)
coll_H2 = mpl.collections.PathCollection(shapes_H2, facecolor=colors_H2, linewidth=0.5)

coll_B3 = mpl.collections.PathCollection(shapes_B3, facecolor=colors_B3, linewidth=0.5)
coll_H3 = mpl.collections.PathCollection(shapes_H3, facecolor=colors_H3, linewidth=0.5)

ax.add_collection(coll_B)
ax.add_collection(coll_H)

ax.add_collection(coll_B2)
ax.add_collection(coll_H2)

ax.add_collection(coll_B3)
ax.add_collection(coll_H3)

ha = ['right', 'center', 'left']

yticks(np.arange(0,21)+0.5,ax_oy2, size=28)
xticks(np.arange(0,23)+0.5,ax_ox2, rotation=40,  ha=ha[0],size=28)

bounds = np.linspace(0,1, 11)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

ax2 = fig.add_axes([0.18, -0.04, 0.64, 0.04])
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,spacing='proportional', ticks=bounds, boundaries=bounds, format='%1.1f', orientation='horizontal' )

labels = ['0', '0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50' ]
ax2.set_xticklabels(labels, size =28)

ax.autoscale_view()
plt.savefig(output+'KuiperPerkinsPerformanceD_ALL_'+domeniu+'_'+periode+'_'+statistique+'_C.png', bbox_inches='tight', pad_inches=0.05)
fig.savefig(output+'KuiperPerkinsPerformanceD_ALL_'+domeniu+'_'+periode+'_'+statistique+'_C.svg', format='svg', dpi=1200)

# ###########################
cgbvr2 = mpl.colors.ListedColormap (A_2_av)
cmap=cgbvr2

colors_B = cgbvr2(W_B*2)
colors_H = cgbvr2(W_H*2)

colors_B2 = cgbvr2(W_B2*2)
colors_H2 = cgbvr2(W_H2*2)

colors_B3 = cgbvr2(W_B3*2)
colors_H3 = cgbvr2(W_H3*2)

fig, ax = plt.subplots(figsize=(24,22), subplot_kw={'aspect': 1.0})

coll_B = mpl.collections.PathCollection(shapes_B, facecolor=colors_B, linewidth=0.5)
coll_H = mpl.collections.PathCollection(shapes_H, facecolor=colors_H, linewidth=0.5)

coll_B2 = mpl.collections.PathCollection(shapes_B2, facecolor=colors_B2, linewidth=0.5)
coll_H2 = mpl.collections.PathCollection(shapes_H2, facecolor=colors_H2, linewidth=0.5)

coll_B3 = mpl.collections.PathCollection(shapes_B3, facecolor=colors_B3, linewidth=0.5)
coll_H3 = mpl.collections.PathCollection(shapes_H3, facecolor=colors_H3, linewidth=0.5)

ax.add_collection(coll_B)
ax.add_collection(coll_H)

ax.add_collection(coll_B2)
ax.add_collection(coll_H2)

ax.add_collection(coll_B3)
ax.add_collection(coll_H3)

ha = ['right', 'center', 'left']

yticks(np.arange(0,21)+0.5,ax_oy2, size=28)
xticks(np.arange(0,23)+0.5,ax_ox2, rotation=40,  ha=ha[0],size=28)

bounds = np.linspace(0,1, 11)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

ax2 = fig.add_axes([0.18, -0.04, 0.64, 0.04])
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,spacing='proportional', ticks=bounds, boundaries=bounds, format='%1.1f', orientation='horizontal' )

labels = ['0', '0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50' ]
ax2.set_xticklabels(labels, size =28)

ax.autoscale_view()
plt.savefig(output+'KuiperPerkinsPerformanceD_ALL_'+domeniu+'_'+periode+'_'+statistique+'_A.png', bbox_inches='tight', pad_inches=0.05)
fig.savefig(output+'KuiperPerkinsPerformanceD_ALL_'+domeniu+'_'+periode+'_'+statistique+'_A.svg', format='svg', dpi=1200)

# #######################
cgbvr2 = mpl.colors.ListedColormap ([(1.0, 1.0, 0.9411764705882353, 1.0),
                                     (1.0, 0.97736255421357998, 0.78202231210820816),
                                     (0.99607843160629272, 0.87017301811891445, 0.52599771653904637),
                                     (0.99607843160629272, 0.77863899819991167, 0.33111881298177381),
                                     (0.99607843160629272, 0.66083815939286172, 0.21454825816201228),
                                     (0.97061130509657023, 0.54199155826194612, 0.13107266876043058),
                                     (0.91515571439967436, 0.42758939301266391, 0.072618226345409362),
                                     (0.82066898416070377, 0.32129182149382196, 0.019469435677370604),
                                     (0.68862746953964238, 0.24562861124674479, 0.012210688918975053),
                                     (0.54431374435331303, 0.18754325631786795, 0.017870050778283793)])

cmap=cgbvr2

colors_B = cgbvr2(W_B*2)
colors_H = cgbvr2(W_H*2)

colors_B2 = cgbvr2(W_B2*2)
colors_H2 = cgbvr2(W_H2*2)

colors_B3 = cgbvr2(W_B3*2)
colors_H3 = cgbvr2(W_H3*2)

fig, ax = plt.subplots(figsize=(24,22), subplot_kw={'aspect': 1.0})

coll_B = mpl.collections.PathCollection(shapes_B, facecolor=colors_B, linewidth=0.5)
coll_H = mpl.collections.PathCollection(shapes_H, facecolor=colors_H, linewidth=0.5)

coll_B2 = mpl.collections.PathCollection(shapes_B2, facecolor=colors_B2, linewidth=0.5)
coll_H2 = mpl.collections.PathCollection(shapes_H2, facecolor=colors_H2, linewidth=0.5)

coll_B3 = mpl.collections.PathCollection(shapes_B3, facecolor=colors_B3, linewidth=0.5)
coll_H3 = mpl.collections.PathCollection(shapes_H3, facecolor=colors_H3, linewidth=0.5)

ax.add_collection(coll_B)
ax.add_collection(coll_H)

ax.add_collection(coll_B2)
ax.add_collection(coll_H2)

ax.add_collection(coll_B3)
ax.add_collection(coll_H3)

ha = ['right', 'center', 'left']

yticks(np.arange(0,21)+0.5,ax_oy2, size=28)
xticks(np.arange(0,23)+0.5,ax_ox2, rotation=40,  ha=ha[0],size=28)

bounds = np.linspace(0,1, 11)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

ax2 = fig.add_axes([0.18, -0.04, 0.64, 0.04])
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,spacing='proportional', ticks=bounds, boundaries=bounds, format='%1.1f', orientation='horizontal' )

labels = ['0', '0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50' ]
ax2.set_xticklabels(labels, size =28)

ax.autoscale_view()
plt.savefig(output+'KuiperPerkinsPerformanceD_ALL_'+domeniu+'_'+periode+'_'+statistique+'_B.png', bbox_inches='tight', pad_inches=0.05)
fig.savefig(output+'KuiperPerkinsPerformanceD_ALL_'+domeniu+'_'+periode+'_'+statistique+'_B.svg', format='svg', dpi=1200)

# #######################

cgbvr2 = mpl.colors.ListedColormap ([[0.1398846663096372, 0.27690888619890397, 0.61514804293127623],
                                    [0.0, 0.4549019607843137, 0.7372549019607844],
                                    [0.0, 0.6666666666666666, 0.8862745098039215],
                                    [0.6039215686274509, 0.8509803921568627, 0.9333333333333333],
                                    [0.9490196078431372, 0.9333333333333333, 0.7725490196078432],
                                    [0.9764705882352941, 0.8470588235294118, 0.6588235294117647],
                                    [0.9607843137254902, 0.6941176470588235, 0.5450980392156862],
                                    [0.9372549019607843, 0.5215686274509804, 0.47843137254901963],
                                    [0.8470588235294118, 0.3215686274509804, 0.34509803921568627],
                                    [0.6862745098039216, 0.20784313725490197, 0.2784313725490196]])
cmap=cgbvr2

colors_B = cgbvr2(W_B*2)
colors_H = cgbvr2(W_H*2)

colors_B2 = cgbvr2(W_B2*2)
colors_H2 = cgbvr2(W_H2*2)

colors_B3 = cgbvr2(W_B3*2)
colors_H3 = cgbvr2(W_H3*2)

fig, ax = plt.subplots(figsize=(24,22), subplot_kw={'aspect': 1.0})

coll_B = mpl.collections.PathCollection(shapes_B, facecolor=colors_B, linewidth=0.5)
coll_H = mpl.collections.PathCollection(shapes_H, facecolor=colors_H, linewidth=0.5)

coll_B2 = mpl.collections.PathCollection(shapes_B2, facecolor=colors_B2, linewidth=0.5)
coll_H2 = mpl.collections.PathCollection(shapes_H2, facecolor=colors_H2, linewidth=0.5)

coll_B3 = mpl.collections.PathCollection(shapes_B3, facecolor=colors_B3, linewidth=0.5)
coll_H3 = mpl.collections.PathCollection(shapes_H3, facecolor=colors_H3, linewidth=0.5)

ax.add_collection(coll_B)
ax.add_collection(coll_H)

ax.add_collection(coll_B2)
ax.add_collection(coll_H2)

ax.add_collection(coll_B3)
ax.add_collection(coll_H3)

ha = ['right', 'center', 'left']

yticks(np.arange(0,21)+0.5,ax_oy2, size=28)
xticks(np.arange(0,23)+0.5,ax_ox2, rotation=40,  ha=ha[0],size=28)

bounds = np.linspace(0,1, 11)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

ax2 = fig.add_axes([0.18, -0.04, 0.64, 0.04])
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,spacing='proportional', ticks=bounds, boundaries=bounds, format='%1.1f', orientation='horizontal' )

labels = ['0', '0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50' ]
ax2.set_xticklabels(labels, size =28)

ax.autoscale_view()
plt.savefig(output+'KuiperPerkinsPerformanceD_ALL_'+domeniu+'_'+periode+'_'+statistique+'_D.png', bbox_inches='tight', pad_inches=0.05)
fig.savefig(output+'KuiperPerkinsPerformanceD_ALL_'+domeniu+'_'+periode+'_'+statistique+'_D.svg', format='svg', dpi=1200)
