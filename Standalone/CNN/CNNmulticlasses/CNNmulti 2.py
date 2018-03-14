import numpy as np
from skimage import color, exposure, transform, io
import os
import glob
from keras.models import Sequential
from keras.layers import BatchNormalization
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import SGD, Adam
from keras import backend as K
from keras.callbacks import LearningRateScheduler, ModelCheckpoint
from keras.utils.np_utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
from keras import callbacks
from keras.applications.vgg19 import VGG19

# Set the number of classes, the size of the image, and the parameters for the training.
NUM_CLASSES = 4
IMG_SIZE = 64
batch_size = 32
epochs = 40
lr = 0.001


nb_train_samples = 4000
nb_validation_samples = 400

# Set the path to the train data and validation (needs to be split into folders per classes). 
TRAIN_DATA_PATH= ''
VALIDATION_DATA_PATH = ''



def createModel():
    '''Loads the VGG19 pretrained neural network and uses it for the base layers. Adds a Dense layer for the output layer.
       Input -> VGG19 -> BatchNormalization Layer -> Dense -> Output. 
    '''

    # Loads the pretrained 19-layer network.
    base_model = VGG19(include_top=False,
                        weights='imagenet',
                        input_shape=(IMG_SIZE, IMG_SIZE, 3))


    # creates a sequential model
    model = Sequential()
    
    # Batch normalization layer. Normalizez the activations of the previous layer at each batch. 
    model.add(BatchNormalization(input_shape=(IMG_SIZE, IMG_SIZE, 3)))
    
    #Adds the VGG19 to be the base layers. 
    model.add(base_model)
    
    # Flattens the input. Does not affect the batch size.
    model.add(Flatten())
    
    # Dense - a fully connected (densely-connected) NN layer
    # Parameters:
        # units - Dimensionality of the output space
        # softmax activation - activation function applied on the last layer. Normalizes the vector in range between 0 and 1.
    model.add(Dense(NUM_CLASSES, activation='softmax'))
    return model 


def compileModel(model):
    ''' 
    Takes a model and compiles it using a categorical crossentropy loss function and an Adam optimizer.   
    
    '''
    # categorical crossentropy is used for multi-class clasification. 
    # Adam optimizer - extension to stochastic gradient descent. Efficient optimizer used often in Computer Vision solutions.
    opt = Adam(lr=1e-4)


    model.compile(loss='categorical_crossentropy',
                  # We NEED binary here, since categorical_crossentropy l1 norms the output before calculating loss.
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


def fitModel(model):
    '''takes a layered model as input and fits it with the training data.'''
    def lr_schedule(epoch):
        return lr * (0.1 ** int(epoch / 10))
     
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

    model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        validation_data=validation_generator,
        validation_steps=nb_validation_samples // batch_size,
        callbacks=[LearningRateScheduler(lr_schedule),
                    ModelCheckpoint('model.h5', save_best_only=True)]
        )


model = createModel()
compiledModel = compileModel(model)
compiledModel.save('model.h5')
compiledModel.save_weights('weights.h5')









