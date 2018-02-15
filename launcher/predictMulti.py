import os
import sys
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from PIL import Image
import image_slicer
import subprocess

img_width, img_height = 48, 48
model_path = 'model.h5'
model_weights_path = 'weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)
sliceSize = 5
class_to_name = ["burns", "cloud", "mines"]
path = "Asset1/"


filePath = sys.argv[1]
filename = filePath[filePath.rfind("/")+1:-4]

# filePath = "testImg.jpg"
# filename = filePath[filePath.rfind("/")+1:-4]

# create slices folder if it doesn't exist
# slice image for stream and add to the slices folder
if os.path.exists('./slices'):
    subprocess.call(["rm", "-rf", "slices/"])

os.makedirs('./slices')
print("slicing...")
tiles = image_slicer.slice(filePath, sliceSize, save=False)
image_slicer.save_tiles(tiles, directory='slices/', prefix='slice')


imgstr = []
location = "./slices/"


for root, dirs, filenames in os.walk(location):
    for f in filenames:
        if (f.startswith('.') == False):
            imgstr.append(location + f)

print("imgstr: ", len(imgstr))

for image in imgstr:
    x = load_img(image, target_size=(img_width,img_height))

    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    x = x/255
    
    predictions = model.predict(x) #predictions in each class
    pred = np.argmax(predictions[0]) #winner index

    out1 = class_to_name[pred]

    #write coordinates to txt files to help out with input to game
    f = open(path+filename+"_"+out1+".txt", "w")
    f.write(image[image.rfind('/')+7:-4].replace("_", ",") + "\n")
    f.close() 

    # print("predictions: ", predictions)
    # print("img: ", image[image.rfind('/')+1:])

    # print("prediction = " + out1)


    # print("----------------------")


subprocess.call(["rm", "-rf", "slices/"])


