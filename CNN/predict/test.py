from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from PIL import Image

model = load_model('testing.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

size = 150, 150
imgstr = ['kaggledata/data/validation/clear_primary/train_40427.jpg']
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
    
    print(out1, out2)