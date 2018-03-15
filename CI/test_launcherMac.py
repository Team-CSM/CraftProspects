import unittest 
import os 
import shutil
from Standalone.launcherMac import slice
from Standalone.launcherMac import predict
from Standalone.launcherMac import class_to_name
import numpy as numpy
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

class test_launcherMac(unittest.TestCase):
    '''Tests the mac launcher of our application'''

    # tests if number of slices created is equal to the number it was asked to be sliced.
    def testSliceNumber(self):
        if not os.path.exists("output/"):
            os.makedirs("output/")
        imagepath = "CI/orig.jpg"
        number = 20
        slice(number,imagepath,"output/")
        list = os.listdir("output/")
        number_files = len(list)
        shutil.rmtree("output/")
        self.assertEqual(number,number_files)
    
    def testPredict_text(self):
        
        # model = Sequential()
        # model.add(Conv2D(32, (3, 3), input_shape=(150,150,3)))
        # model.add(Activation('relu'))
        # model.add(MaxPooling2D(pool_size=(2, 2)))

        # model.add(Conv2D(32, (3, 3)))
        # model.add(Activation('relu'))
        # model.add(MaxPooling2D(pool_size=(2, 2)))

        # model.add(Conv2D(64, (3, 3)))
        # model.add(Activation('relu'))
        # model.add(MaxPooling2D(pool_size=(2, 2)))
        # model.add(Flatten())
        # model.add(Dense(64))
        # model.add(Activation('relu'))
        # model.add(Dropout(0.5))
        # model.add(Dense(1))
        # model.add(Activation('sigmoid'))
        # model.save("test.h5")
            # Loads the pretrained 19-layer network.
        # base_model = VGG19(include_top=False,
        #                 weights='imagenet',
        #                 input_shape=(64, 64, 3))
        # model = Sequential()
        # model.add(base_model)        
        # model.add(Flatten())
        # model.add(Dense(4, activation='softmax'))
        # model.save("test.h5")
        # #check if the text files correspond to class_to_name.
        # #recreates the slices.
        if not os.path.exists("output/"):
            os.makedirs("output/")

        imagepath = "CI/orig.jpg"
        number = 20 
        slice(number,imagepath,"output/")
        list = os.listdir("output/")
        
        if not os.path.exists("output/text/"):
            os.makedirs("output/text/")
        
        for var in range(len(list)):
            list[var] = "output/"+list[var]
        
        predict(list,class_to_name,"output/text/",load_model("CI/model.h5"))
        list = os.listdir("output/text/")
        
        boolean = False
        for file in list:
           
            name = file[:-4]
            if name in class_to_name:
                boolean = True
            else:
                boolean = False
        self.assertEqual(boolean,True)

        #test the coordinates:
        coordinates_list = []
        for file in list:
            file_object = open("output/text/"+file, "r")
            text = file_object.read()
            coordinates_list.extend(text.split(','))
        
        self.assertEqual(len(coordinates_list),number)
        shutil.rmtree("output/text/")
        shutil.rmtree("output/")

    
        



if __name__ == '__main__':
    unittest.main()