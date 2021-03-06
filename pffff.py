import rasterio
from owslib.wms import WebMapService
from io import BytesIO
from rasterio.plot import show


# on a pris l'info ici : http://wms.craig.fr/ortho?language=fra&request=GetMetadata&layer=ortho_irc
# https://wfs.craig.fr/ortho?service=WMS&version=1.3.0&request=GetMap&width=500&height=300&styles=&layers=ortho_irc&format=image/png&crs=EPSG:2154&bbox=6389750.000000,624750.000000,6635750.000000,966550.000000

url = 'http://wms.craig.fr/ortho/?service=WMS&version=1.3.0'
wms = WebMapService(url)

# retrouver une coordonnée
# http://epsg.io/map#srs=2154&x=706506.76&y=6518979.77&z=10&layer=streets
centrex = 706506.76
centrey = 6518979.77
rayon = 200

x1new= centrex - rayon
x2new = centrex + rayon
y1new = centrey - rayon
y2new = centrey + rayon

layer= 'ortho_irc'

# nombre de pixels par mètre
resolution = 5

img = wms.getmap(layers = [layer], srs = 'EPSG:2154', bbox = [x1new,y1new,x2new,y2new] , size = (2 * rayon * resolution, 2 * rayon * resolution), format= 'image/png')

with rasterio.open(BytesIO(img.read())) as r:
    thing = r.read()
    show(thing)

