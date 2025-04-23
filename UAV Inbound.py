#To start with:
    #Set out a location for delivery - University of Leicester Campus, diff buildings
    #Some parameters to deal with, multiple delivery locations as well as a
    #warehouse for picking up items and a warehouse for returning items
    #maximum capacity of the drones being - 2 items(for the moment ignore dimensions)
    # need to include time and awareness.

#Further goals:
    #Drone working completely independtly, recieve a delivery task and collect/drop-off as applicable
    #Different types of packages and a limited stock
    


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL
from PIL import Image

fig, ax = plt.subplots()

atlas_data = [['Kookaburra',
  -35.27667,
  149.1097,
  'Australian National Botaniacl Gardens, Canberra',
  '2000-08-14',
  'Aves',
  'Coraciiformes',
  'Alcedinidae',
  'Dacelo',
  'Dacelo novaeguineae',
  'False'],
 ['White-faced heron',
  -35.272244105599064,
  149.12580246473127,
  'Sullivans Creek--Turner Parkland',
  '2016-08-09',
  'Aves',
  'Ciconiiformes',
  'Ardeidae',
  'Egretta',
  'Egretta novaehollandiae',
  'False'],
 ['Australian King-parrot',
  -35.274386,
  149.112636,
  'CSIRO (Black Mountain)',
  '2014-10-20',
  'Aves',
  'Psittaciformes',
  'Psittacidae',
  'Alisterus',
  'Alisterus scapularis',
  'False'],
 ['Eastern Spinebill',
  -35.27719917903922,
  149.10937031732462,
  'Australian National Botanic Gardens',
  '2000-09-08',
  'Aves',
  'Passeriformes',
  'Meliphagidae',
  'Acanthorhynchus',
  'Acanthorhynchus tenuirostris',
  'False'],
 ['Crimson Rosella',
  -35.2780499,
  149.11015749999999,
  'Australian National Botanic Gardens',
  '2003-08-08',
  'Aves',
  'Psittaciformes',
  'Psittacidae',
  'Platycercus',
  'Platycercus elegans',
  'False'],
 ['Australian Raven',
  -35.27856893080605,
  149.10974594347084,
  'Australian National Botanic Gardens',
  '2018-03-18',
  'Aves',
  'Passeriformes',
  'Corvidae',
  'Corvus',
  'Corvus coronoides',
  'False'],
 ['Australian King-parrot',
  -35.2780499,
  149.11015749999999,
  'Australian National Botanic Gardens',
  '2012-07-24',
  'Aves',
  'Psittaciformes',
  'Psittacidae',
  'Alisterus',
  'Alisterus scapularis',
  'False']]

def mapping_data(atlas_data):
    x, y = [], []
    for i in range(len(atlas_data)):
        x.append(atlas_data[i][1])
        y.append(atlas_data[i][2])

    return x, y

y, x = mapping_data(atlas_data)

ax.scatter(x, y, edgecolors='red', linewidths=2, zorder=2)
ax.imshow(mpimg.imread('https://paste.pics/PWTAU'), extent=(149.105, 149.130, -35.29, -35.27), zorder=1)
im = Image.open(r'C:\Users\jjpw1\OneDrive - University of Leicester\Final Year Project\Leicestermap.png')
  
im.show()  
plt.show()




