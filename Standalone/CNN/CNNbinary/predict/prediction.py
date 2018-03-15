from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from PIL import Image, ImageDraw, ImageFont

#pip install image_slicer
import image_slicer
import os, errno

# For usage, change MODEL_LOCATION to = "<.H5 OR CSV FILE PATH>"
MODEL_LOCATION = ""
size = 150, 150

# Since binary classification, only 2 class names required. 
class_to_name = ["clear_primary", "cloudy"]

def slice_image(image, num_slice):
    """Given an image and number of slices, creates a directory called slices relative to this file, and stores the images there."""
    tiles = image_slicer.slice(image, num_slice, save=False)
    if not os.path.exists('slices/'):
        os.makedirs('slices/')
    image_slicer.save_tiles(tiles, directory='slices/', prefix='slice')

def os_walk(location):
    """Given a location, returns a list of all files in that directory, excluding those that begin with a "." 
    to avoid issues with hidden files."""
    imgstr = []
    for root, dirs, filenames in os.walk(location):
        for f in filenames:
            if (f.startswith('.') == False):
                imgstr.append(location + f)
    return imgstr

def modelLoader(model_loc):
    """Given the path to a .h5 model file, loads and compiles the model."""
    model = load_model('/Users/craig/Documents/tp3/CSM-project/Standalone/CNN/CNNbinary/demonstration/testing.h5')
    model.compile(loss='binary_crossentropy',
                optimizer='rmsprop',
                metrics=['accuracy'])
    return model

def predictImage(imgstr, model):
    """Given a list of images, the function outputs the image names to the
    corresponding prediction class .txt file in the current directory.
    """
    for image in imgstr:
        img = Image.open(image)
        img = img.resize(size, Image.ANTIALIAS)
        img = img.convert('RGB')
        x = np.asarray(img, dtype='float32')
        x = np.expand_dims(x, axis=0)
        x = x/255
        choice = model.predict(x)
        out1 = class_to_name[model.predict_classes(x)[0][0]]
        if (choice >= 0.5):
            out2 = str(round(choice[0][0]*100, 2)) + "%"
        else:
            out2 = str(round((1 - choice[0][0])*100, 2)) + "%"
        f = open(out1+".txt", "a")
        f.write(image[image.rfind('/')+1:] + "\n")
        
        print(out1, out2) #1=class, 2 = %
        print(image)
    f.close() 



if __name__ == '__main__':
    slice_image('false_full_tile1.jpg', 900)
    imgstr = os_walk("./slices/")
    model = modelLoader(MODEL_LOCATION)
    predictImage(imgstr, model)
