#import sys
#sys.path.append('c:/temp/gpsinfo_Python27')
import gpsinfo


service = gpsinfo.Service('https://raw.githubusercontent.com/maegger/GPS_INFO_PSI_TESTSERVICE/master/gpsinfoWMTSCapabilities.xml')
layer = gpsinfo.Layer(service, 'DGM_1M_UPPER_AUSTRIA')



#Punktabfrage:
print('Elevation = ' + str(layer.value('nearest', 60151.5000000000000000,291789.5000000000000000 )))

#Bounding Box Abfrage:
layer.exportToAsc(60251.5000000000000000,291889.5000000000000000, 60356.5000000000000000,291894.5000000000000000,'c:/temp/ausgabe.asc')






