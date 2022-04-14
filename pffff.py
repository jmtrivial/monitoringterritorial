import rasterio
from owslib.wms import WebMapService
from io import BytesIO
from rasterio.plot import show



# https://wfs.craig.fr/ortho?service=WMS&version=1.3.0&request=GetMap&width=500&height=300&styles=&layers=ortho_irc&format=image/png&crs=EPSG:2154&bbox=6389750.000000,624750.000000,6635750.000000,966550.000000

url = 'http://wms.craig.fr/ortho/?service=WMS&version=1.3.0'
wms = WebMapService(url)

x1new= 6389750.000000
x2new = 6635750.000000
y1new = 624750.000000
y2new = 966550.000000

layer= 'ortho_irc'


img = wms.getmap(layers = [layer], srs = 'EPSG:2154', bbox = [x1new,y1new,x2new,y2new] , size = (500, 300), format= 'image/png')

with rasterio.open(BytesIO(img.read())) as r:
    thing = r.read()
    show(thing)

