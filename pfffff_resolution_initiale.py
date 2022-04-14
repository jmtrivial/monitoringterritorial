import wget
from osgeo import gdal
import rasterio
from rasterio.plot import show
from rasterio import windows
import os
import random

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
    # à adapter pour récupérer ausi l'ortho
    url = "https://drive.opendata.craig.fr/s/opendata/download?path=%2Fortho-irc%2F2019_puy-de-dome_20cm%2Fdalles&files="

    # téléchargement de la donnée
    for nom_fichier in nom_fichiers():
        print(nom_fichier)
        wget.download(url + nom_fichier, out="data")

def create_virtual_raster():

    filepaths = [ "data/" + f for f in nom_fichiers()]
    vrt_path = 'data/temp.vrt'  # path to vrt to build
    gdal.BuildVRT(vrt_path, filepaths)

def visualiser_le_virtuel():
    with rasterio.open('data/temp.vrt') as raster:
        show(raster)



def fabriquer_vignettes_regulieres():
    # avec rasterio, il faudrait le faire à la main
    # https://gis.stackexchange.com/questions/285499/how-to-split-multiband-image-into-image-tiles-using-rasterio
    tuilex = 256
    tuiley = 256

    # en ligne de commande, on peut lancer:
    os.system("gdal_retile.py data/temp.vrt -ps 256 256 -targetDir data/tiles/")


# principe:
# - on calcule l'emprise de la donnée
# - on la diminue de la moitié de la taille des tuiles
# - on tire au hasard une coordonnée dans l'emprise
# - on tire au hasard un angle
# - on calcule la vignette correspondante

size_vignette = 256 # pixels

with rasterio.open('data/temp.vrt') as raster:
    maxx = raster.meta['width']
    maxy = raster.meta['height']
    offsetx = random.randint(size_vignette, maxx - size_vignette)
    offsety = random.randint(size_vignette, maxy - size_vignette)
    
    # voir https://gis.stackexchange.com/questions/285499/how-to-split-multiband-image-into-image-tiles-using-rasterio
    window = windows.Window(col_off=offsetx, row_off=offsety, width=size_vignette, height=size_vignette)
    transform = windows.transform(window, raster.transform)

    show(raster.read(window=window))

    # ça fonctionne. À vérifier: que cette fenêtre puisse être utilsée aussi sur une autre image en geotiff qui n'aurait pas les mêmes 
    # projections et bornes

