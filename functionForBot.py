import random
from datetime import datetime

def getStringPhotos(lstPhotos):
    indexLvL = random.randint(0, (len(lstPhotos) - 1))
    stringPhoto = lstPhotos[indexLvL]
    lstPhotos.remove(stringPhoto)
    return stringPhoto

def backUpData(dictPhotos):
    datetimeNow = str(datetime.now()).split()
    d = datetimeNow[0]
    f = open('backUpData/backUpCopy({}).txt'.format(d), 'w')
    for key, value in dictPhotos.items():
        f.write('{}->{}\n'.format(key, value))
    f.close()