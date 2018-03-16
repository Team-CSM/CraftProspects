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
        if not os.path.exists("CI/output/"):
            os.makedirs("CI/output/")
        imagepath = "CI/assets/orig.jpg"
        number = 20
        slice(number,imagepath,"CI/output/")
        file_list = os.listdir("CI/output/")
        file_number = 0 
        for file in file_list:
            if file[0] != ".":
                file_number += 1

        shutil.rmtree("CI/output/")
        self.assertEqual(number,file_number)
    
    def testPredict_text(self):
 
        list = os.listdir("CI/assets/slices")
        
        if not os.path.exists("CI/text/"):
            os.makedirs("CI/text/")
        
        for x in range(len(list)):
            list[x] = "CI/assets/slices/"+list[x]
        
        predict(list,class_to_name,"CI/text/",load_model("CI/assets/model.h5"))
        list = os.listdir("CI/text/")
        
        boolean = False
        for file in list:
           
            name = file[:-4]
            if name in class_to_name:
                boolean = True
            else:
                boolean = False
        shutil.rmtree("CI/text")
        self.assertEqual(boolean,True)
        

if __name__ == '__main__':
    unittest.main()