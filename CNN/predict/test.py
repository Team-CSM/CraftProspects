from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from Tkinter import Tk
from tkFileDialog import askopenfilename

#pip install image_slicer
import image_slicer
import os, errno


tiles = image_slicer.slice('false_full_tile1.jpg', 100, save=False)

if not os.path.exists('slices/'):
    os.makedirs('slices/')

image_slicer.save_tiles(tiles, directory='slices/', prefix='slice')

imgstr = []
location = "../../csmdata3/slices/"

for root, dirs, filenames in os.walk(location):
    print("loc: ", location)
    for f in filenames:
        if (f.startswith('.') == False):
            imgstr.append(location + f)
            print("appending...")

print(imgstr)

model = load_model('testing.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

size = 150, 150

class_to_name = ["clear_primary", "cloudy"]



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
