import os
# for fn in os.listdir('photos'):
#      if os.path.isfile(fn):
#         print (fn)
#      else:
#          print (fn)
listPhotosLight = [fn for fn in os.listdir('photos/light')]
listPhotosHard = [fn for fn in os.listdir('photos/hard')]
listPhotosMedium = [fn for fn in os.listdir('photos/medium')]
