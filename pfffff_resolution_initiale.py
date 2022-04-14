import wget
from osgeo import gdal
import rasterio

# installer le paquet libgdal-dev (debian)

# https://drive.opendata.craig.fr/s/opendata?path=%2Fortho-irc%2F2019_puy-de-dome_20cm
# on récupère le dallage

# 63-2019-0706-6519-LA93-0M20-IRC-E100.tif

def nom_fichiers():
    centerx = 706
    centery = 6519
    rayon = 2

    fichiers = []
    for x in range(centerx - rayon, centerx + rayon):
        for y in range(centery - rayon, centery + rayon):
            fichiers.append("63-2019-{0:04d}-{1:04d}-LA93-0M20-IRC-E100.tif".format(x, y))

    return fichiers

def download():
    url = "https://drive.opendata.craig.fr/s/opendata/download?path=%2Fortho-irc%2F2019_puy-de-dome_20cm%2Fdalles&files="

    # téléchargement de la donnée
    for nom_fichier in nom_fichiers():
        print(nom_fichier)
        wget.download(url + nom_fichier, out="data")

def create_virtual_raster():

    filepaths = [ "data/" + f for f in nom_fichiers()]
    vrt_path = 'data/temp.vrt'  # path to vrt to build
    gdal.BuildVRT(vrt_path, filepaths)

with rasterio.open('data/temp.vrt') as raster:
    pass  # do stuff
