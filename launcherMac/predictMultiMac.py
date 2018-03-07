import os, sys, subprocess, image_slicer
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from PIL import Image

img_width, img_height = 64, 64
model_path = 'model.h5'
model_weights_path = 'weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

class_to_name = ["clear", "cloudy", "mine", "slash"]



# print ("imgPath: ", imgPath)
# print ("dirPath: ", dirPath)


def main():

    imgPath = sys.argv[1] # python predictMulti.py ./players_money/orig.jpg
    dirPath = imgPath[:imgPath.rfind('/')+1]

    IMAGE = imgPath
    # location = dirPath + IMAGE.split('.')[0] + '_' + 'slices'
    locationSlices = dirPath + 'slices'

    if not os.path.exists(locationSlices):
        os.makedirs(locationSlices)
        slice(900, IMAGE, locationSlices)

    imgstr = []

    # Add all slices to the imgstr
    for root, dirs, filenames in os.walk(locationSlices):
        for f in filenames:
            if (f.startswith('.') == False):
                imgstr.append(locationSlices + '/' + f)

    print("imgstr: ", len(imgstr))



    # Getting predictions for all the slices from the model
    predict(imgstr, class_to_name, dirPath)

    # outloc = dirPath
    # if not os.path.exists(outloc):
    # Finally splitting the input image into 9 slices, with set ratio to be input to game.
    slice(9, IMAGE, dirPath)
    
    print("resizing...")
    for root, dirs, filenames in os.walk(dirPath):
        for f in filenames:
            if f[-3:]==".png":
                im = Image.open(dirPath + f)
                nx, ny = im.size
                im = im.resize((int(nx*1.4), ny), Image.BICUBIC)
                im.save(dirPath + f)

    subprocess.call(["rm","-r",locationSlices]) #cleanup= delete the thousands of slices
    # os.system("rm -r " + locationSlices)

def slice(number, IMAGE, location):
    # slice image for stream and add to the slices folder
    
    print("slicing...")
    tiles = image_slicer.slice(IMAGE, number, save=False)
    image_slicer.save_tiles(tiles, directory=location, prefix='slice')
    # image_slicer.save_tiles(tiles, directory=location)


def predict(imgstr, class_to_name, dirPath):
    print("predicting...")
    for image in imgstr:
        x = load_img(image, target_size=(img_width,img_height))

        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        x = x/255 # normalise

        
        predictions = model.predict(x) #predictions in each class
        pred = np.argmax(predictions[0]) #winner index

        if (max(predictions[0]) > 0.5):
            out1 = class_to_name[pred]

            #write coordinates to log files to help out with input to game
            f = open(dirPath+out1+".txt", "a")
            f.write(image[image.rfind('/')+7:-4].replace("_", ",") + "_")
            f.close() 


if __name__ == '__main__':
    main()