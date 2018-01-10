import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from PIL import Image
import image_slicer

img_width, img_height = 48, 48
model_path = 'model.h5'
model_weights_path = 'weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)



# create slices folder if it doesn't exist
# slice image for stream and add to the slices folder
if not os.path.exists('./slices'):
    os.makedirs('./slices')
    print("slicing...")
    tiles = image_slicer.slice('false_full_tile1.jpg', 2500, save=False)
    image_slicer.save_tiles(tiles, directory='slices/', prefix='slice')
    



imgstr = []
location = "./slices/"


for root, dirs, filenames in os.walk(location):
    for f in filenames:
        if (f.startswith('.') == False):
            imgstr.append(location + f)

print("imgstr: ", len(imgstr))

class_to_name = ["slash_burn", "cloudy", "artisinal_mine"]


for image in imgstr:
    x = load_img(image, target_size=(img_width,img_height))

    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    x = x/255
    
    predictions = model.predict(x) #predictions in each class
    pred = np.argmax(predictions[0]) #winner index

    out1 = class_to_name[pred]

    #write coordinates to txt files to help out with input to game
    f = open(out1+".txt", "a")
    f.write(image[image.rfind('/')+7:-4].replace("_", ",") + "\n")
    f.close() 


    print("predictions: ", predictions)
    print("img: ", image[image.rfind('/')+1:])

    print("prediction = " + out1)


    print("----------------------")





