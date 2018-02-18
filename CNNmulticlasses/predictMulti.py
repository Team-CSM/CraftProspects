import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from PIL import Image
import image_slicer

img_width, img_height = 64, 64
model_path = 'model.h5'
model_weights_path = 'weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

def main():
    IMAGE = 'test.jpg'
    location = './' + IMAGE.split('.')[0] + '_' + 'slices'

    if not os.path.exists(location):
        slice(2025, IMAGE, location)

    imgstr = []

    # Add all slices to the imgstr
    for root, dirs, filenames in os.walk(location):
        for f in filenames:
            if (f.startswith('.') == False):
                imgstr.append(location + '/' + f)

    print("imgstr: ", len(imgstr))

    class_to_name = ["clear_primary", "cloudy", "mine", "slash_burn"]

    # Getting predictions for all the slices from the model
    predict(imgstr, class_to_name)

    outloc = './outslices'
    if not os.path.exists(outloc):
    # Finally splitting the input image into 9 slices, with set ratio to be input to game.
        slice(9, IMAGE, outloc)
        
        print("resizing...")
        for root, dirs, filenames in os.walk(outloc):
            for f in filenames:
                im = Image.open(outloc + '/' + f)
                nx, ny = im.size
                im = im.resize((int(nx*1.4), ny), Image.BICUBIC)
                im.save(outloc + '/' + f)


def slice(number, IMAGE, location):
    # slice image for stream and add to the slices folder
    os.makedirs(location)
    print("slicing...")
    tiles = image_slicer.slice(IMAGE, number, save=False)
    image_slicer.save_tiles(tiles, directory=location + '/', prefix='slice')

def predict(imgstr, class_to_name):
    print("predicting...")
    for image in imgstr:
        x = load_img(image, target_size=(img_width,img_height))

        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        # normalise
        x = x/255
        
        predictions = model.predict(x) #predictions in each class
        pred = np.argmax(predictions[0]) #winner index

        if (max(predictions[0]) > 0.5):
            out1 = class_to_name[pred]

            #write coordinates to log files to help out with input to game
            f = open(out1+".log", "a")
            f.write(image[image.rfind('/')+7:-4].replace("_", ",") + "\n")
            f.close() 

main()



