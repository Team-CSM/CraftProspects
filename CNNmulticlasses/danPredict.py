import numpy as np
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras import applications
from keras.utils.np_utils import to_categorical
import matplotlib.pyplot as plt
import math
import os
import image_slicer

class_to_name = ["artisinal_mine", "clear_primary", "cloudy", "slash_burn"]

if not os.path.exists('./slices'):
    os.makedirs('./slices')
    tiles = image_slicer.slice('false_full_tile1.jpg', 2500, save=False)
    image_slicer.save_tiles(tiles, directory='slices/', prefix='slice')

imgstr = []
location = "./slices/"

for root, dirs, filenames in os.walk(location):
    for f in filenames:
        if (f.startswith('.') == False):
            imgstr.append(location + f)

 # load the class_indices saved in the earlier step
class_dictionary = np.load('class_indices.npy').item()
num_classes = len(class_dictionary)

# build the VGG16 network
model = applications.VGG16(include_top=False, weights='imagenet')

# add the path to your test image below
image = load_img(imgstr[0], target_size=(224, 224))
image = img_to_array(image)

# important! otherwise the predictions will be '0'
image = image / 255
image = np.expand_dims(image, axis=0)

# get the bottleneck prediction from the pre-trained VGG16 model
bottleneck_prediction = model.predict(image)

def buildTopModel():
    model = Sequential()
    model.add(Flatten(input_shape=bottleneck_prediction.shape[1:]))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='sigmoid'))
    model.load_weights('bottleneck_fc_model.h5')
    return model

# build top model
model2 = buildTopModel()


for image_path in imgstr:

    # add the path to your test image below
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)

    # important! otherwise the predictions will be '0'
    image = image / 255
    image = np.expand_dims(image, axis=0)

    bottleneck_prediction = model.predict(image)

    # use the bottleneck prediction on the top model to get the final
    # classification
    class_predicted = model2.predict_classes(bottleneck_prediction)
    
    out1 = class_to_name[class_predicted[0]]

    f = open(out1+".txt", "a")
    f.write(image_path[image_path.rfind('/')+1:] + "\n")
    f.close() 


for output in class_to_name:
    filedir = output+".txt"
    if (os.path.isfile('filedir')):
        f = open(filedir, "r+")
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i][6:-5].replace("_", ",")

        f.seek(0)
        f.truncate()
        lines = "\r\n".join(lines)
        f.writelines(lines)