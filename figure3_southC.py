import matplotlib.path as mpath
import matplotlib.pyplot as plt
import matplotlib as mpl
from pylab import  xticks, yticks
import numpy as np
from scipy import vstack, hstack
from netCDF4 import Dataset


# files botom
my_file0 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_daymetVSanusplin_can__011Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file0, 'r')
rx1day_0 = f.variables['rx1day'][:]
cdd_0 = f.variables['cdd'][:]
cwd_0 = f.variables['cwd'][:]
r1mm_0 = f.variables['rr1mm'][:]
mean_0 = f.variables['pr'][:]
pc90_0 = f.variables['pc90'][:]
pc95_0 = f.variables['pc95'][:]
pc99_0 = f.variables['pc99'][:]
f.close()

my_file1 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_narrVSanusplin_can__RegularNARR_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file1, 'r')
rx1day_1 = f.variables['rx1day'][:]
cdd_1 = f.variables['cdd'][:]
cwd_1 = f.variables['cwd'][:]
r1mm_1 = f.variables['rr1mm'][:]
mean_1 = f.variables['pr'][:]
pc90_1 = f.variables['pc90'][:]
pc95_1 = f.variables['pc95'][:]
pc99_1 = f.variables['pc99'][:]
f.close()

my_file2 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_merraVSanusplin_can__MERRA_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file2, 'r')
rx1day_2 = f.variables['rx1day'][:]
cdd_2 = f.variables['cdd'][:]
cwd_2 = f.variables['cwd'][:]
r1mm_2 = f.variables['rr1mm'][:]
mean_2 = f.variables['pr'][:]
pc90_2 = f.variables['pc90'][:]
pc95_2 = f.variables['pc95'][:]
pc99_2 = f.variables['pc99'][:]
f.close()

my_file3 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_eraIntVSanusplin_can__ERAInt_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file3, 'r')
rx1day_3 = f.variables['rx1day'][:]
cdd_3 = f.variables['cdd'][:]
cwd_3 = f.variables['cwd'][:]
r1mm_3 = f.variables['rr1mm'][:]
mean_3 = f.variables['pr'][:]
pc90_3 = f.variables['pc90'][:]
pc95_3 = f.variables['pc95'][:]
pc99_3 = f.variables['pc99'][:]
f.close()

my_file4 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_ncepR2VSanusplin_can__NCEP_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file4, 'r')
rx1day_4 = f.variables['rx1day'][:]
cdd_4 = f.variables['cdd'][:]
cwd_4 = f.variables['cwd'][:]
r1mm_4 = f.variables['rr1mm'][:]
mean_4 = f.variables['pr'][:]
pc90_4 = f.variables['pc90'][:]
pc95_4 = f.variables['pc95'][:]
pc99_4 = f.variables['pc99'][:]
f.close()

my_file5 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_crcm5VSanusplin_can__044Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file5, 'r')
rx1day_5 = f.variables['rx1day'][:]
cdd_5 = f.variables['cdd'][:]
cwd_5 = f.variables['cwd'][:]
r1mm_5 = f.variables['rr1mm'][:]
mean_5 = f.variables['pr'][:]
pc90_5 = f.variables['pc90'][:]
pc95_5 = f.variables['pc95'][:]
pc99_5 = f.variables['pc99'][:]
f.close()

my_file6 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_canRCM4VSanusplin_can__044Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file6, 'r')
rx1day_6 = f.variables['rx1day'][:]
cdd_6 = f.variables['cdd'][:]
cwd_6 = f.variables['cwd'][:]
r1mm_6 = f.variables['rr1mm'][:]
mean_6 = f.variables['pr'][:]
pc90_6 = f.variables['pc90'][:]
pc95_6 = f.variables['pc95'][:]
pc99_6 = f.variables['pc99'][:]
f.close()


my_file7 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_canRCM4v2VSanusplin_can__044Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file7, 'r')
rx1day_7 = f.variables['rx1day'][:]
cdd_7 = f.variables['cdd'][:]
cwd_7 = f.variables['cwd'][:]
r1mm_7 = f.variables['rr1mm'][:]
mean_7 = f.variables['pr'][:]
pc90_7 = f.variables['pc90'][:]
pc95_7 = f.variables['pc95'][:]
pc99_7 = f.variables['pc99'][:]
f.close()


my_file8 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_canRCM4v3VSanusplin_can__044Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file8, 'r')
rx1day_8 = f.variables['rx1day'][:]
cdd_8 = f.variables['cdd'][:]
cwd_8 = f.variables['cwd'][:]
r1mm_8 = f.variables['rr1mm'][:]
mean_8 = f.variables['pr'][:]
pc90_8 = f.variables['pc90'][:]
pc95_8 = f.variables['pc95'][:]
pc99_8 = f.variables['pc99'][:]
f.close()


my_file9 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_crcm424_50kmVSanusplin_can__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file9, 'r')
rx1day_9 = f.variables['rx1day'][:]
cdd_9 = f.variables['cdd'][:]
cwd_9 = f.variables['cwd'][:]
r1mm_9 = f.variables['rr1mm'][:]
mean_9 = f.variables['pr'][:]
pc90_9 = f.variables['pc90'][:]
pc95_9 = f.variables['pc95'][:]
pc99_9 = f.variables['pc99'][:]
f.close()


my_file10 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_crcm420_50kmVSanusplin_can__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file10, 'r')
rx1day_10 = f.variables['rx1day'][:]
cdd_10 = f.variables['cdd'][:]
cwd_10 = f.variables['cwd'][:]
r1mm_10 = f.variables['rr1mm'][:]
mean_10 = f.variables['pr'][:]
pc90_10 = f.variables['pc90'][:]
pc95_10 = f.variables['pc95'][:]
pc99_10 = f.variables['pc99'][:]
f.close()


my_file11 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_ecp2VSanusplin_can__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file11, 'r')
rx1day_11 = f.variables['rx1day'][:]
cdd_11 = f.variables['cdd'][:]
cwd_11 = f.variables['cwd'][:]
r1mm_11 = f.variables['rr1mm'][:]
mean_11 = f.variables['pr'][:]
pc90_11 = f.variables['pc90'][:]
pc95_11 = f.variables['pc95'][:]
pc99_11 = f.variables['pc99'][:]
f.close()


my_file12 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_hrm3VSanusplin_can__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file12, 'r')
rx1day_12 = f.variables['rx1day'][:]
cdd_12 = f.variables['cdd'][:]
cwd_12 = f.variables['cwd'][:]
r1mm_12 = f.variables['rr1mm'][:]
mean_12 = f.variables['pr'][:]
pc90_12 = f.variables['pc90'][:]
pc95_12 = f.variables['pc95'][:]
pc99_12 = f.variables['pc99'][:]
f.close()


my_file13 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_mm5iVSanusplin_can__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file13, 'r')
rx1day_13 = f.variables['rx1day'][:]
cdd_13 = f.variables['cdd'][:]
cwd_13 = f.variables['cwd'][:]
r1mm_13 = f.variables['rr1mm'][:]
mean_13 = f.variables['pr'][:]
pc90_13 = f.variables['pc90'][:]
pc95_13 = f.variables['pc95'][:]
pc99_13 = f.variables['pc99'][:]
f.close()


my_file14 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_rcm3VSanusplin_can__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file14, 'r')
rx1day_14 = f.variables['rx1day'][:]
cdd_14 = f.variables['cdd'][:]
cwd_14 = f.variables['cwd'][:]
r1mm_14 = f.variables['rr1mm'][:]
mean_14 = f.variables['pr'][:]
pc90_14 = f.variables['pc90'][:]
pc95_14 = f.variables['pc95'][:]
pc99_14 = f.variables['pc99'][:]
f.close()


my_file15 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_wrfpVSanusplin_can__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file15, 'r')
rx1day_15 = f.variables['rx1day'][:]
cdd_15 = f.variables['cdd'][:]
cwd_15 = f.variables['cwd'][:]
r1mm_15 = f.variables['rr1mm'][:]
mean_15 = f.variables['pr'][:]
pc90_15 = f.variables['pc90'][:]
pc95_15 = f.variables['pc95'][:]
pc99_15 = f.variables['pc99'][:]
f.close()


Rb0_pc99 = hstack((pc99_0.ravel(),pc99_1.ravel(),pc99_2.ravel(),pc99_3.ravel(),pc99_4.ravel(),pc99_5.ravel(),pc99_6.ravel(),pc99_7.ravel(),pc99_8.ravel(),pc99_9.ravel(),pc99_10.ravel(),pc99_11.ravel(),pc99_12.ravel(),pc99_13.ravel(),pc99_14.ravel(),pc99_15.ravel()))
Rb0_pc95 = hstack((pc95_0.ravel(),pc95_1.ravel(),pc95_2.ravel(),pc95_3.ravel(),pc95_4.ravel(),pc95_5.ravel(),pc95_6.ravel(),pc95_7.ravel(),pc95_8.ravel(),pc95_9.ravel(),pc95_10.ravel(),pc95_11.ravel(),pc95_12.ravel(),pc95_13.ravel(),pc95_14.ravel(),pc95_15.ravel()))
Rb0_pc90 = hstack((pc90_0.ravel(),pc90_1.ravel(),pc90_2.ravel(),pc90_3.ravel(),pc90_4.ravel(),pc90_5.ravel(),pc90_6.ravel(),pc90_7.ravel(),pc90_8.ravel(),pc90_9.ravel(),pc90_10.ravel(),pc90_11.ravel(),pc90_12.ravel(),pc90_13.ravel(),pc90_14.ravel(),pc90_15.ravel()))

Rb0_rx1day = hstack((rx1day_0.ravel(),rx1day_1.ravel(),rx1day_2.ravel(),rx1day_3.ravel(),rx1day_4.ravel(),rx1day_5.ravel(),rx1day_6.ravel(),rx1day_7.ravel(),rx1day_8.ravel(),rx1day_9.ravel(),rx1day_10.ravel(),rx1day_11.ravel(),rx1day_12.ravel(),rx1day_13.ravel(),rx1day_14.ravel(),rx1day_15.ravel()))
Rb0_cdd = hstack((cdd_0.ravel(),cdd_1.ravel(),cdd_2.ravel(),cdd_3.ravel(),cdd_4.ravel(),cdd_5.ravel(),cdd_6.ravel(),cdd_7.ravel(),cdd_8.ravel(),cdd_9.ravel(),cdd_10.ravel(),cdd_11.ravel(),cdd_12.ravel(),cdd_13.ravel(),cdd_14.ravel(),cdd_15.ravel()))
Rb0_cwd = hstack((cwd_0.ravel(),cwd_1.ravel(),cwd_2.ravel(),cwd_3.ravel(),cwd_4.ravel(),cwd_5.ravel(),cwd_6.ravel(),cwd_7.ravel(),cwd_8.ravel(),cwd_9.ravel(),cwd_10.ravel(),cwd_11.ravel(),cwd_12.ravel(),cwd_13.ravel(),cwd_14.ravel(),cwd_15.ravel()))
Rb0_r1mm = hstack((r1mm_0.ravel(),r1mm_1.ravel(),r1mm_2.ravel(),r1mm_3.ravel(),r1mm_4.ravel(),r1mm_5.ravel(),r1mm_6.ravel(),r1mm_7.ravel(),r1mm_8.ravel(),r1mm_9.ravel(),r1mm_10.ravel(),r1mm_11.ravel(),r1mm_12.ravel(),r1mm_13.ravel(),r1mm_14.ravel(),r1mm_15.ravel()))
Rb0_mean = hstack((mean_0.ravel(),mean_1.ravel(),mean_2.ravel(),mean_3.ravel(),mean_4.ravel(),mean_5.ravel(),mean_6.ravel(),mean_7.ravel(),mean_8.ravel(),mean_9.ravel(),mean_10.ravel(),mean_11.ravel(),mean_12.ravel(),mean_13.ravel(),mean_14.ravel(),mean_15.ravel()))


# files haut
my_file0 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSanusplin/corrCoef_ALL_daymetVSanusplin_can__011Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file0, 'r')
rx1day_0 = f.variables['rx1day'][:]
cdd_0 = f.variables['cdd'][:]
cwd_0 = f.variables['cwd'][:]
r1mm_0 = f.variables['rr1mm'][:]
mean_0 = f.variables['pr'][:]
pc90_0 = f.variables['pc90'][:]
pc95_0 = f.variables['pc95'][:]
pc99_0 = f.variables['pc99'][:]
f.close()


my_file1 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_narrVSdaymet__RegularNARR_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file1, 'r')
rx1day_1 = f.variables['rx1day'][:]
cdd_1 = f.variables['cdd'][:]
cwd_1 = f.variables['cwd'][:]
r1mm_1 = f.variables['rr1mm'][:]
mean_1 = f.variables['pr'][:]
pc90_1 = f.variables['pc90'][:]
pc95_1 = f.variables['pc95'][:]
pc99_1 = f.variables['pc99'][:]
f.close()

my_file2 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_merraVSdaymet__MERRA_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file2, 'r')
rx1day_2 = f.variables['rx1day'][:]
cdd_2 = f.variables['cdd'][:]
cwd_2 = f.variables['cwd'][:]
r1mm_2 = f.variables['rr1mm'][:]
mean_2 = f.variables['pr'][:]
pc90_2 = f.variables['pc90'][:]
pc95_2 = f.variables['pc95'][:]
pc99_2 = f.variables['pc99'][:]
f.close()

my_file3 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_eraIntVSdaymet__ERAInt_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file3, 'r')
rx1day_3 = f.variables['rx1day'][:]
cdd_3 = f.variables['cdd'][:]
cwd_3 = f.variables['cwd'][:]
r1mm_3 = f.variables['rr1mm'][:]
mean_3 = f.variables['pr'][:]
pc90_3 = f.variables['pc90'][:]
pc95_3 = f.variables['pc95'][:]
pc99_3 = f.variables['pc99'][:]
f.close()

my_file4 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_ncepR2VSdaymet__NCEP_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file4, 'r')
rx1day_4 = f.variables['rx1day'][:]
cdd_4 = f.variables['cdd'][:]
cwd_4 = f.variables['cwd'][:]
r1mm_4 = f.variables['rr1mm'][:]
mean_4 = f.variables['pr'][:]
pc90_4 = f.variables['pc90'][:]
pc95_4 = f.variables['pc95'][:]
pc99_4 = f.variables['pc99'][:]
f.close()

my_file5 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_crcm5VSdaymet__044Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file5, 'r')
rx1day_5 = f.variables['rx1day'][:]
cdd_5 = f.variables['cdd'][:]
cwd_5 = f.variables['cwd'][:]
r1mm_5 = f.variables['rr1mm'][:]
mean_5 = f.variables['pr'][:]
pc90_5 = f.variables['pc90'][:]
pc95_5 = f.variables['pc95'][:]
pc99_5 = f.variables['pc99'][:]
f.close()

my_file6 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_canRCM4VSdaymet__044Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file6, 'r')
rx1day_6 = f.variables['rx1day'][:]
cdd_6 = f.variables['cdd'][:]
cwd_6 = f.variables['cwd'][:]
r1mm_6 = f.variables['rr1mm'][:]
mean_6 = f.variables['pr'][:]
pc90_6 = f.variables['pc90'][:]
pc95_6 = f.variables['pc95'][:]
pc99_6 = f.variables['pc99'][:]
f.close()


my_file7 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_canRCM4v2VSdaymet__044Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file7, 'r')
rx1day_7 = f.variables['rx1day'][:]
cdd_7 = f.variables['cdd'][:]
cwd_7 = f.variables['cwd'][:]
r1mm_7 = f.variables['rr1mm'][:]
mean_7 = f.variables['pr'][:]
pc90_7 = f.variables['pc90'][:]
pc95_7 = f.variables['pc95'][:]
pc99_7 = f.variables['pc99'][:]
f.close()


my_file8 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_canRCM4v3VSdaymet__044Regular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file8, 'r')
rx1day_8 = f.variables['rx1day'][:]
cdd_8 = f.variables['cdd'][:]
cwd_8 = f.variables['cwd'][:]
r1mm_8 = f.variables['rr1mm'][:]
mean_8 = f.variables['pr'][:]
pc90_8 = f.variables['pc90'][:]
pc95_8 = f.variables['pc95'][:]
pc99_8 = f.variables['pc99'][:]
f.close()


my_file9 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_crcm424_50kmVSdaymet__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file9, 'r')
rx1day_9 = f.variables['rx1day'][:]
cdd_9 = f.variables['cdd'][:]
cwd_9 = f.variables['cwd'][:]
r1mm_9 = f.variables['rr1mm'][:]
mean_9 = f.variables['pr'][:]
pc90_9 = f.variables['pc90'][:]
pc95_9 = f.variables['pc95'][:]
pc99_9 = f.variables['pc99'][:]
f.close()


my_file10 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_crcm420_50kmVSdaymet__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file10, 'r')
rx1day_10 = f.variables['rx1day'][:]
cdd_10 = f.variables['cdd'][:]
cwd_10 = f.variables['cwd'][:]
r1mm_10 = f.variables['rr1mm'][:]
mean_10 = f.variables['pr'][:]
pc90_10 = f.variables['pc90'][:]
pc95_10 = f.variables['pc95'][:]
pc99_10 = f.variables['pc99'][:]
f.close()


my_file11 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_ecp2VSdaymet__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file11, 'r')
rx1day_11 = f.variables['rx1day'][:]
cdd_11 = f.variables['cdd'][:]
cwd_11 = f.variables['cwd'][:]
r1mm_11 = f.variables['rr1mm'][:]
mean_11 = f.variables['pr'][:]
pc90_11 = f.variables['pc90'][:]
pc95_11 = f.variables['pc95'][:]
pc99_11 = f.variables['pc99'][:]
f.close()


my_file12 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_hrm3VSdaymet__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file12, 'r')
rx1day_12 = f.variables['rx1day'][:]
cdd_12 = f.variables['cdd'][:]
cwd_12 = f.variables['cwd'][:]
r1mm_12 = f.variables['rr1mm'][:]
mean_12 = f.variables['pr'][:]
pc90_12 = f.variables['pc90'][:]
pc95_12 = f.variables['pc95'][:]
pc99_12 = f.variables['pc99'][:]
f.close()


my_file13 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_mm5iVSdaymet__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file13, 'r')
rx1day_13 = f.variables['rx1day'][:]
cdd_13 = f.variables['cdd'][:]
cwd_13 = f.variables['cwd'][:]
r1mm_13 = f.variables['rr1mm'][:]
mean_13 = f.variables['pr'][:]
pc90_13 = f.variables['pc90'][:]
pc95_13 = f.variables['pc95'][:]
pc99_13 = f.variables['pc99'][:]
f.close()


my_file14 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_rcm3VSdaymet__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file14, 'r')
rx1day_14 = f.variables['rx1day'][:]
cdd_14 = f.variables['cdd'][:]
cwd_14 = f.variables['cwd'][:]
r1mm_14 = f.variables['rr1mm'][:]
mean_14 = f.variables['pr'][:]
pc90_14 = f.variables['pc90'][:]
pc95_14 = f.variables['pc95'][:]
pc99_14 = f.variables['pc99'][:]
f.close()


my_file15 = '/Volumes/Emilia/NApaperV2/climat1989to2004/corcoef_SouthCanadaVSdaymet/corrCoef_ALL_wrfpVSdaymet__NARCCAPRegular_DJF_1989to2004mean_SouthCanada.nc'
f = Dataset(my_file15, 'r')
rx1day_15 = f.variables['rx1day'][:]
cdd_15 = f.variables['cdd'][:]
cwd_15 = f.variables['cwd'][:]
r1mm_15 = f.variables['rr1mm'][:]
mean_15 = f.variables['pr'][:]
pc90_15 = f.variables['pc90'][:]
pc95_15 = f.variables['pc95'][:]
pc99_15 = f.variables['pc99'][:]
f.close()

Rh0_pc99 = hstack((pc99_0.ravel(),pc99_1.ravel(),pc99_2.ravel(),pc99_3.ravel(),pc99_4.ravel(),pc99_5.ravel(),pc99_6.ravel(),pc99_7.ravel(),pc99_8.ravel(),pc99_9.ravel(),pc99_10.ravel(),pc99_11.ravel(),pc99_12.ravel(),pc99_13.ravel(),pc99_14.ravel(),pc99_15.ravel()))
Rh0_pc95 = hstack((pc95_0.ravel(),pc95_1.ravel(),pc95_2.ravel(),pc95_3.ravel(),pc95_4.ravel(),pc95_5.ravel(),pc95_6.ravel(),pc95_7.ravel(),pc95_8.ravel(),pc95_9.ravel(),pc95_10.ravel(),pc95_11.ravel(),pc95_12.ravel(),pc95_13.ravel(),pc95_14.ravel(),pc95_15.ravel()))
Rh0_pc90 = hstack((pc90_0.ravel(),pc90_1.ravel(),pc90_2.ravel(),pc90_3.ravel(),pc90_4.ravel(),pc90_5.ravel(),pc90_6.ravel(),pc90_7.ravel(),pc90_8.ravel(),pc90_9.ravel(),pc90_10.ravel(),pc90_11.ravel(),pc90_12.ravel(),pc90_13.ravel(),pc90_14.ravel(),pc90_15.ravel()))

Rh0_rx1day = hstack((rx1day_0.ravel(),rx1day_1.ravel(),rx1day_2.ravel(),rx1day_3.ravel(),rx1day_4.ravel(),rx1day_5.ravel(),rx1day_6.ravel(),rx1day_7.ravel(),rx1day_8.ravel(),rx1day_9.ravel(),rx1day_10.ravel(),rx1day_11.ravel(),rx1day_12.ravel(),rx1day_13.ravel(),rx1day_14.ravel(),rx1day_15.ravel()))
Rh0_cdd = hstack((cdd_0.ravel(),cdd_1.ravel(),cdd_2.ravel(),cdd_3.ravel(),cdd_4.ravel(),cdd_5.ravel(),cdd_6.ravel(),cdd_7.ravel(),cdd_8.ravel(),cdd_9.ravel(),cdd_10.ravel(),cdd_11.ravel(),cdd_12.ravel(),cdd_13.ravel(),cdd_14.ravel(),cdd_15.ravel()))
Rh0_cwd = hstack((cwd_0.ravel(),cwd_1.ravel(),cwd_2.ravel(),cwd_3.ravel(),cwd_4.ravel(),cwd_5.ravel(),cwd_6.ravel(),cwd_7.ravel(),cwd_8.ravel(),cwd_9.ravel(),cwd_10.ravel(),cwd_11.ravel(),cwd_12.ravel(),cwd_13.ravel(),cwd_14.ravel(),cwd_15.ravel()))
Rh0_r1mm = hstack((r1mm_0.ravel(),r1mm_1.ravel(),r1mm_2.ravel(),r1mm_3.ravel(),r1mm_4.ravel(),r1mm_5.ravel(),r1mm_6.ravel(),r1mm_7.ravel(),r1mm_8.ravel(),r1mm_9.ravel(),r1mm_10.ravel(),r1mm_11.ravel(),r1mm_12.ravel(),r1mm_13.ravel(),r1mm_14.ravel(),r1mm_15.ravel()))
Rh0_mean = hstack((mean_0.ravel(),mean_1.ravel(),mean_2.ravel(),mean_3.ravel(),mean_4.ravel(),mean_5.ravel(),mean_6.ravel(),mean_7.ravel(),mean_8.ravel(),mean_9.ravel(),mean_10.ravel(),mean_11.ravel(),mean_12.ravel(),mean_13.ravel(),mean_14.ravel(),mean_15.ravel()))

Rb_pc90 = Rb0_pc90
Rb_pc95 = Rb0_pc95
Rb_pc99 = Rb0_pc99
Rb_rx1day = Rb0_rx1day
Rb_cdd = Rb0_cdd
Rb_cwd = Rb0_cwd
Rb_r1mm = Rb0_r1mm
Rb_mean = Rb0_mean

Rh_pc90 = Rh0_pc90
Rh_pc95 = Rh0_pc95
Rh_pc99 = Rh0_pc99
Rh_rx1day = Rh0_rx1day
Rh_cdd = Rh0_cdd
Rh_cwd = Rh0_cwd
Rh_r1mm = Rh0_r1mm
Rh_mean = Rh0_mean



W_B = hstack((Rb_pc90,Rb_pc95,Rb_pc99,Rb_rx1day,Rb_cdd,Rb_cwd,Rb_r1mm,Rb_mean))
W_H = hstack((Rh_pc90,Rh_pc95,Rh_pc99,Rh_rx1day,Rh_cdd,Rh_cwd,Rh_r1mm,Rh_mean))


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

shapes_B = [get_triB(xoff=x, yoff=y) for j in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0] for i in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0] for x,y in [(i, j)]]
shapes_H = [get_triH(xoff=x, yoff=y) for j in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0] for i in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0] for x,y in [(i, j)]]

shapes_BB = [get_triB2(xoff=x-0.5, yoff=y-0.5) for j in [4.0] for i in [17.0] for x,y in [(i, j)]]
shapes_HH = [get_triH2(xoff=x-0.5, yoff=y-0.5) for j in [4.0] for i in [17.0] for x,y in [(i, j)]]

# define the colors to use to fill the triangles
#cgbvr = mpl.colors.ListedColormap ([[1., 1., .8], [.8, 1., .2], [.6, 1., 0.],  [0., 1., 0.],  [0., .6, 0.], [.6, 1., 1.], [0., 1., 1.], [0., .6, 1.],  [0., 0., 1.], [0., 0., .4] ])
#cgbvr =mpl.colors.ListedColormap ([[0., 0., .2],[0., 0., .2], [0., 0., 0.2],[0., 0., 0.2],[0., 0., 0.2],[0., 0., 0.2], [0., 0., 0.2],[0., 0., 0.2], [0., 0., 0.2],[0., 0., 0.2],[0., 0., .2],[0., 0., .4], [0., 0., 1.],[0., .6, 1.],[.6, 1., 1.],[0., .6, 0.], [0., 1., 0.],[.6, 1., 0.], [.8, 1., .2],[1., 1., .8]])
cgbvr = mpl.colors.ListedColormap (['DarkRed','FireBrick','Crimson', 'LightCoral','LIGHTPink', 'Lavender', 'LightSkyBlue', 'DodgerBlue', 'Blue','Navy'])


cmap=cgbvr

colors_B = cgbvr(W_B)
colors_H = cgbvr(W_H)

# begin the plot
fig, ax = plt.subplots(figsize=(18,8), subplot_kw={'aspect': 1.0})

coll_B = mpl.collections.PathCollection(shapes_B, facecolor=colors_B, linewidth=1)
coll_H = mpl.collections.PathCollection(shapes_H, facecolor=colors_H, linewidth=1)
coll_BB = mpl.collections.PathCollection(shapes_BB, facecolor='white', linewidth=1)
coll_HH = mpl.collections.PathCollection(shapes_HH, facecolor='white', linewidth=1)

ax.add_collection(coll_B)
ax.add_collection(coll_H)
ax.add_collection(coll_BB)
ax.add_collection(coll_HH)

#ax.set_title('R computed over South Canada', size=18)
yticks(np.arange(0,8)+0.5,['90th percentile','95th percentile','99th percentile','RX1day', 'CDD', 'CWD','R1mm','DJF-mean'], size=14)
xticks(np.arange(0,16)+0.5,['Observations','NARR','MERRA','ERA-Interim','NCEP-R2','CRCM5 0.44','CanRCM4 0.44', 'CanRCM4v2 0.44', 'CanRCM4v3 0.44', 'CRCM4.2.4', 'CRCM4.2.0', 'ECP2','HRM3','MM5I','RCM3','WRFP'], rotation=90, size=14)

# define the bins of colorbar and normalize
#bounds = np.linspace(0,1, 11)
#norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# create a second axes for the colorbar
##ax2 = fig.add_axes([0.95, 0.1, 0.03, 0.8]) # pour vertical colorbar
#ax2 = fig.add_axes([0.0, -0.2, 1, 0.05])
##cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], boundaries=bounds, format='%1.2f', orientation='horizontal')
#cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds, boundaries=bounds, format='%1.2f', orientation='horizontal')

##ax2.set_xlabel('NRMSD', size=12 )


ax.autoscale_view()
plt.savefig('/Volumes/Emilia/pythonL/images_examples/Fig3_southCanada_DJF.png', bbox_inches='tight', pad_inches=0.5)

plt.show()