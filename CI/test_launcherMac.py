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
import h5py

class test_launcherMac(unittest.TestCase):
    '''Tests the mac launcher of our application'''

    # tests if number of slices created is equal to the number it was asked to be sliced.
    def testSliceNumber(self):
        if not os.path.exists("output1/"):
            os.makedirs("output1/")
        imagepath = "CI/orig.jpg"
        number = 20
        slice(number,imagepath,"output1/")
        list = os.listdir("output1/")
        number_files = len(list)
        shutil.rmtree("output1/")
        self.assertEqual(number,number_files)
    
    def testPredict_text(self):
 
        if not os.path.exists("output2/"):
            os.makedirs("output2/")

        imagepath = "CI/orig.jpg"
        number = 20 
        slice(number,imagepath,"output2/")
        list = os.listdir("output2/")
        
        if not os.path.exists("output2/text/"):
            os.makedirs("output2/text/")
        
        for var in range(len(list)):
            list[var] = "output2/"+list[var]
        
        predict(list,class_to_name,"output2/text/",load_model("CI/model.h5"))
        list = os.listdir("output/2text/")
        
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
            file_object = open("output2/text/"+file, "r")
            text = file_object.read()
            coordinates_list.extend(text.split(','))
        
        self.assertEqual(len(coordinates_list),number)
        shutil.rmtree("output2/text/")
        shutil.rmtree("output2/")

    
        



if __name__ == '__main__':
    unittest.main()