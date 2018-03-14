from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K


# dimensions of our images.
img_width, img_height = 150, 150

# For usage, please specify the path for the training and validation data in the form "<PATH>".
train_data_dir = ""
validation_data_dir = ""

nb_train_samples = 2000
nb_validation_samples = 800
epochs = 3
batch_size = 16

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

def addNeuralLayers(model):
    '''This function takes a neural network model (Sequential in our case) and adds a series of layers to the model.
       Input -> Conv2D -> Activation -> MaxPooling2D -> Conv2D -> Activation -> MaxPooling2D -> Conv2D -> Activation -> MaxPooling2D -> Flatten -> Dense -> Activation -> Dense -> Activation
     ''' 

    # Conv2D - 2D convolution layer. It creates a convolution kernel that is convolved with the layer input to produce a tensor of outputs.
    # Conv2D Parameters:
        # 32 - filters: Integer, the dimensionality of the output space. (the number of output filters in the convolution)
        # (3-3) - strides:  Specifies the strides of the convolution along the width and height. 
        # input_shape = 3D tensor of the input. Needs to have the dimensions of our image size and 3 as the 3rd value in the touple because there are 3 channels in an image (RGB)
        # activation - Activation function. A 'relu' activation - rectifier activation function. Decides if outside connections consider neural "fired". It is most common act. function. 
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))

    # MaxPooling2D - Is a 2D pooling layer. It is common to periodically insert a pooling layer in-between successive convolutional layers
    # It preduces the spatial size of the representation to reduce the amount of parameters and computation in the networks. 
    # Also controls overfitting.
    # Parameters:
        # pool_size - The factor by which to downscale in each dimension (vertical and horizontal). In our case it halves the input in both spatial dimensions.
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Flatten - Flattens the input. Does not affect the batch size. 
    model.add(Flatten())

    # Dense - a fully connected (densely-connected) NN layer
    # Parameters:
        # units - Dimensionality of the output space
        # relu activation - activation function applied on the last layer.
    model.add(Dense(64))
    model.add(Activation('relu'))

    # Dropout - A fraction of randomly selected neurons are ignored during training. Helps with preventing overfitting.
    # Parameters:
        # rate - fraction of the input units to drop.
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    return model

def compileModel(model):
    ''' 
      Takes a model and compiles it using a categorical crossentropy loss function and an Adam optimizer.
    '''
    model.compile(loss='binary_crossentropy',
                optimizer='rmsprop',
                metrics=['accuracy'])
    return model
    

def fitModel(model):
    '''takes a layered model as input and fits it with the training data.'''
    # this is the augmentation configuration we will use for training
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    # this is the augmentation configuration we will use for testing:
    # only rescaling
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')

    validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')

    model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        validation_data=validation_generator,
        validation_steps=nb_validation_samples // batch_size)
    return model

baseModel = Sequential()
layeredModel = addNeuralLayers(baseModel)
compiledModel = compileModel(layeredModel)
fittedModel = fitModel(compiledModel)
fittedModel.save('testing.h5')