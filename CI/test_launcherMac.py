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
 
      
        list = os.listdir("CI/slices")
        
        if not os.path.exists("text/"):
            os.makedirs("text/")
        
        for x in range(len(list)):
            list[x] = "CI/slices/"+list[x]
        
        predict(list,class_to_name,"text/",load_model("CI/model.h5"))
        list = os.listdir("text/")
        
        boolean = False
        for file in list:
           
            name = file[:-4]
            if name in class_to_name:
                boolean = True
            else:
                boolean = False
        self.assertEqual(boolean,True)
    
        # #test the coordinates:
        # coordinates_list = []
        # for file in list:
        #     file_object = open("text/"+file, "r")
        #     text = file_object.read()
        #     coordinates_list.extend(text.split(','))
        #     file_object.close()
        # shutil.rmtree("text")
        # self.assertEqual(len(coordinates_list),20)


    
        



if __name__ == '__main__':
    unittest.main()