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





def addNeuralLayers(neuralModel):
    '''This function takes a neural network model (Sequential in our case) and adds a series of layers to the model.
       Input -> Conv2D -> MaxPooling2D -> Droput -> Conv2D -> MaxPooling2D -> Dropout -> Flatten -> Dense Layer -> Output
       Return a layered model.
     ''' 
    
    # Conv2D - 2D convolution layer. It creates a convolution kernel that is convolved with the layer input to produce a tensor of outputs.
    # Conv2D Parameters:    
        # 32 - filters: Integer, the dimensionality of the output space. (the number of output filters in the convolution)
        # (3-3) - strides:  Specifies the strides of the convolution along the width and height. 
        # input_shape = 3D tensor of the input. Needs to have the dimensions of our image size and 3 as the 3rd value in the touple because there are 3 channels in an image (RGB)
        # activation - Activation function to use. A 'relu' activation - rectifier activation function. It is most common act. function.
        # padding - 'same' means no padding is applied on the layer.
   
    neuralModel.add(Conv2D(32, (3, 3), padding='same',
                        input_shape=(IMG_SIZE, IMG_SIZE, 3),
                        activation='relu'))
    neuralModel.add(Conv2D(32, (3, 3), activation='relu'))
    
    # MaxPooling2D - Is a 2D pooling layer. It is common to periodically insert a pooling layer in-between successive convolutional layers
    # It preduces the spatial size of the representation to reduce the amount of parameters and computation in the networks. 
    # Also controls overfitting.
    # Parameters:
        # pool_size - The factor by which to downscale in each dimension (vertical and horizontal). In our case it halves the input in both spatial dimensions.

    
    neuralModel.add(MaxPooling2D(pool_size=(2, 2)))
    
    # Dropout - A fraction of randomly selected neurons are ignored during training. Helps with preventing overfitting.
    # Parameters:
        # rate - fraction of the input units to drop.
    neuralModel.add(Dropout(0.2))

    nerualModel.add(Conv2D(64, (3, 3), padding='same',
                        activation='relu'))
    neuralModel.add(Conv2D(64, (3, 3), activation='relu'))
    neuralModel.add(MaxPooling2D(pool_size=(2, 2)))
    neuralModel.add(Dropout(0.2))

    neuralModel.add(Conv2D(128, (3, 3), padding='same',
                        activation='relu'))
    neuralModel.add(Conv2D(128, (3, 3), activation='relu'))
    neuralModel.add(MaxPooling2D(pool_size=(2, 2)))
    neuralModel.add(Dropout(0.2))

    
    # Flatten - Flattens the input. Does not affect the batch size. 
    neuralModel.add(Flatten())
    
    # Dense - a fully connected (densely-connected) NN layer
    # Parameters:
        # units - Dimensionality of the output space
        # softmax activation - activation function applied on the last layer. Normalizes the vector in range between 0 and 1.

    neuralModel.add(Dense(512, activation='relu'))
    neuralModel.add(Dropout(0.5))
    neuralModel.add(Dense(NUM_CLASSES, activation='softmax')) 
    return neuralModel 

def compileModel(model):
    ''' 
      Takes a model and compiles it using a categorical crossentropy loss function and an Adam optimizer.
      Return a compiled model
    '''

    # categorical crossentropy is used for multi-class clasification. 
    # Adam optimizer - extension to stochastic gradient descent. Efficient optimizer used often in Computer Vision solutions.

    adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
    model.compile(loss='categorical_crossentropy', 
              optimizer=adam,
              metrics=['accuracy'])
    return model 


def fitModel(model):
    '''Takes a layered model as input and fits it with the training data.
       Return a compiled model.
    '''
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
    return model

baseModel = Sequential()
layeredModel = addNeuralLayers(baseModel)
compiledModel = compileModel(layeredModel)
fittedModel = fitModel(compiledModel)
fittedModel.save_weights('weights.h5')









