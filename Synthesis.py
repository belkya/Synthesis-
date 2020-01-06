#import required libraries
import rasterio
from rasterio.plot import show
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np


#import bands as separate 1 band raster
filename1 = input ("Filename1-Bnd4: ")
band4 = rasterio.open(filename1) #red
filename2 = input ("Filename2-Bnd5: ")
band5 = rasterio.open(filename2) #nir

#number of raster rows
print("Band4-Image-Height:")
print(band4.height)

#number of raster column
print("Band4-Image-Width:")
print(band4.width)

#plot band 
plot.show(band4)
plot.show(band5)

#type of raster byte
print("Type-of-Raster-Byte:")
print(band4.dtypes[0])

#raster sytem of reference
print(band4.crs)

#raster transform parameters
print(band4.transform)

#raster values as matrix array
print(band4.read(1))

#multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(band4, ax=ax1, cmap='Blues') #red
plot.show(band5, ax=ax2, cmap='Blues') #nir
fig.tight_layout()

#generate nir and red objects as arrays in float64 format
red = band4.read(1).astype('float64')
nir = band5.read(1).astype('float64')

nir

#Allow division of one in raster
np.seterr(divide='ignore', invalid='ignore')

#ndvi filters
check = np.logical_or ( red > 0, nir > 0 )

#calculating ndvi
ndvi = np.where ( check,  (nir - red ) / ( nir + red ), -999 )

#ndvi value
print("NDVI-Values:")
print(ndvi)

#Mean Value
print("Mean-NDVI-Value:")
print(ndvi.mean())

#STD Value
print("NDVI-STD")
print(ndvi.std())

#export ndvi image
ndviImage = rasterio.open(r"C:\Users\Cain Butler\Documents\ndvi.tiff",'w',driver='Gtiff',
                          width=band4.width, 
                          height = band4.height, 
                          count=1, crs=band4.crs, 
                          transform=band4.transform, 
                          dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()

#plot ndvi
ndvi = rasterio.open(r"C:\Users\Cain Butler\Documents\ndvi.tiff")
fig = plt.figure(figsize=(18,12))
plot.show(ndvi)
