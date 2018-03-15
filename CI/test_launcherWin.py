import unittest 
import os 
import shutil
from Standalone.launcherWin import slice
from Standalone.launcherWin import predict
from Standalone.launcherWin import class_to_name
import numpy as numpy
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import h5py

class test_launcherWin(unittest.TestCase):
    '''Tests the windows launcher of our application'''

    # tests if number of slices created is equal to the number it was asked to be sliced.
    def testSliceNumber(self):
        if not os.path.exists("output/"):
            os.makedirs("output/")
        imagepath = "CI/orig.jpg"
        number = 20
        slice(number,imagepath,"output/")
        file_list = os.listdir("output/")
        file_number = 0 
        for file in file_list:
            if file[0] != ".":
                file_number += 1

        shutil.rmtree("output/")
        self.assertEqual(number,file_number)
    
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
    

if __name__ == '__main__':
    unittest.main()