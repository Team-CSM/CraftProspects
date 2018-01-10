import numpy as np
from skimage import color, exposure, transform, io
import os
import glob
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import SGD, Adam
from keras import backend as K
from keras.callbacks import LearningRateScheduler, ModelCheckpoint
from keras.utils.np_utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
from keras import callbacks

NUM_CLASSES = 3
IMG_SIZE = 48
batch_size = 32
epochs = 20
lr = 0.001

#samples_per_epoch = 100
#validation_steps = 300

nb_train_samples = 891
nb_validation_samples = 114

train_data_path = '../../csmdata/train'
validation_data_path = '../../csmdata/validation'
#label: 0,1,2
# 00000 = burn
# 00001 = cloudy
# 00002 = mine


model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same',
                     input_shape=(IMG_SIZE, IMG_SIZE, 3),
                     activation='relu'))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

model.add(Conv2D(64, (3, 3), padding='same',
                     activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

model.add(Conv2D(128, (3, 3), padding='same',
                     activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(NUM_CLASSES, activation='softmax')) #tanh, softmax



# train model with adam or sgd?

sgd = SGD(lr=lr, decay=1e-6, momentum=0.9, nesterov=True)
adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
model.compile(loss='categorical_crossentropy', #binary_crossentropy, categorical_crossentropy
              optimizer=adam,
              metrics=['accuracy'])



train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)


test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_path,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=batch_size,
    class_mode='categorical')


validation_generator = test_datagen.flow_from_directory(
    validation_data_path,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=batch_size,
    class_mode='categorical')



def lr_schedule(epoch):
    return lr * (0.1 ** int(epoch / 10))


model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size,
    callbacks=[LearningRateScheduler(lr_schedule),
                ModelCheckpoint('model.h5', save_best_only=True)]
    )

#model.save('./models/model.h5')
model.save_weights('weights.h5')









