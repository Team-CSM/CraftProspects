from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from Tkinter import Tk
from tkFileDialog import askopenfilename
import os
from skimage import color, exposure, transform, io

IMG_SIZE = 48

def preprocess_img(img):
    # Histogram normalization in v channel
    hsv = color.rgb2hsv(img)
    hsv[:, :, 2] = exposure.equalize_hist(hsv[:, :, 2])
    img = color.hsv2rgb(hsv)

    # central square crop
    min_side = min(img.shape[:-1])
    centre = img.shape[0] // 2, img.shape[1] // 2
    img = img[centre[0] - min_side // 2:centre[0] + min_side // 2,
              centre[1] - min_side // 2:centre[1] + min_side // 2,
              :]

    # rescale to standard size
    img = transform.resize(img, (IMG_SIZE, IMG_SIZE))

    # roll color axis to axis 0
    img = np.rollaxis(img, -1)

    return img


model = load_model('20epochs04527.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


imgstr = []
location = "../../slices/"
for root, dirs, filenames in os.walk(location):
    for f in filenames:
        if (f.startswith('.') == False):
            imgstr.append(preprocess_img(io.imread(location + f)))

for image in imgstr:
    x = np.asarray(image, dtype='float32')
    x = np.expand_dims(x, axis=0)
    x = x/255
    probs = model.predict(x) #percent
    classIndex = probs.argmax(axis=-1)[0]
    print("probs: ", probs)
    print("class , accuracy", classIndex, probs[0][classIndex])
    print("-------------------------")

# 00000 = artisinal_mine.jpg
# 00001 = clear_primary.jpg
# 00002 = cloudy.jpg
# 00003 = slash_burn.jpg



