import wget

# https://drive.opendata.craig.fr/s/opendata?path=%2Fortho-irc%2F2019_puy-de-dome_20cm
# on récupère le dallage

# 63-2019-0706-6519-LA93-0M20-IRC-E100.tif

url = "https://drive.opendata.craig.fr/s/opendata/download?path=%2Fortho-irc%2F2019_puy-de-dome_20cm%2Fdalles&files="

centerx = 706
centery = 6519
rayon = 2

for x in range(centerx - rayon, centerx + rayon):
    for y in range(centery - rayon, centery + rayon):
        nom_fichier = "63-2019-{0:04d}-{1:04d}-LA93-0M20-IRC-E100.tif".format(x, y)
        print(nom_fichier)
        wget.download(url + nom_fichier, out="data")
