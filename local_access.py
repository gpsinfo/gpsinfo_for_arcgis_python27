#import sys
#sys.path.append('c:/temp/gpsinfo_Python27')
import gpsinfo


service = gpsinfo.Service("file:\\\\C:\\test\\GPS_INFO_PSI_TESTSERVICE\\gpsinfoWMTSCapabilities.xml")
layer = gpsinfo.Layer(service, 'DGM_1M_UPPER_AUSTRIA')

#Bounding Box Abfrage:
layer.exportToAsc(61932.1,292975.8, 62421.9,293468.7,'c:/temp/export.asc')

#Punktabfrage:
print('Lokaler Zugriff: Elevation = ' + str(layer.value('interpolate', 61932.1,292975.8)))



