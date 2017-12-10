import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

img_width, img_height = 48, 48
model_path = 'model.h5'
model_weights_path = 'weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)


for i, ret in enumerate(os.walk('../../csmdata3/toPredict')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."): #hidden files lik .DS_STORE
      continue
    
    imgDir = ret[0] + '/' + filename
    x = load_img(imgDir, target_size=(img_width,img_height))

    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    x = x/255
    
    predictions = model.predict(x) #predictions in each class
    pred = np.argmax(predictions[0]) #winner index

    print("predictions: ", predictions)
    print("img: ", imgDir[imgDir.rfind('/')+1:])

    if pred == 0:
      print("prediction = 0 = burn")
    elif pred == 1:
      print("prediction = 1 = cloudy")
    elif pred == 2:
      print("prediction = 2 = mine")

    print("----------------------")


