import unittest 
import os 
import shutil
from Standalone.launcherMac import slice as macSlice
from Standalone.launcherMac import predict as macPredict
from Standalone.launcherMac import class_to_name as macClass_to_name
from Standalone.launcherWin import slice as winSlice
from Standalone.launcherWin import predict as winPredict
from Standalone.launcherWin import class_to_name as winClass_to_name
import numpy as numpy
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import h5py

class test_launcher(unittest.TestCase):
    '''Tests the launchers of our application'''

    # tests if number of slices created is equal to the number it was asked to be sliced.
    def testSliceNumber_mac(self):
        if not os.path.exists("CI/output/"):
            os.makedirs("CI/output/")
        imagepath = "CI/assets/orig.jpg"
        number = 20
        macSlice(number,imagepath,"CI/output/")
        list = os.listdir("CI/output/")
        number_files = len(list)
        shutil.rmtree("CI/output/")
        self.assertEqual(number,number_files)

    def testPredict_text_mac(self):     
        list = os.listdir("CI/assets/slices")
        
        if not os.path.exists("CI/text/"):
            os.makedirs("CI/text/")
        
        for x in range(len(list)):
            list[x] = "CI/assets/slices/"+list[x]
        
        macPredict(list,macClass_to_name,"CI/text/",load_model("CI/assets/model.h5"))
        list = os.listdir("CI/text/")
        
        boolean = False
        for file in list:
            
            name = file[:-4]
            if name in class_to_name:
                boolean = True
            else:
                boolean = False
        shutil.rmtree("CI/text/")
        self.assertEqual(boolean,True)
   
    def testSliceNumber_win(self):
        if not os.path.exists("CI/output/"):
            os.makedirs("CI/output/")
        imagepath = "CI/assets/orig.jpg"
        number = 20
        winSlice(number,imagepath,"CI/output/")
        file_list = os.listdir("CI/output/")
        file_number = 0 
        for file in file_list:
            if file[0] != ".":
                file_number += 1

        shutil.rmtree("CI/output/")
        self.assertEqual(number,file_number)

    def testPredict_text_win(self):

        list = os.listdir("CI/assets/slices")
        
        if not os.path.exists("CI/text/"):
            os.makedirs("CI/text/")
        
        for x in range(len(list)):
            list[x] = "CI/assets/slices/"+list[x]
        
        winPredict(list,winClass_to_name,"CI/text/",load_model("CI/assets/model.h5"))
        list = os.listdir("CI/text/")
        
        boolean = False
        for file in list:
            
            name = file[:-4]
            if name in class_to_name:
                boolean = True
            else:
                boolean = False
        shutil.rmtree('CI/text/')
        self.assertEqual(boolean,True)


if __name__ == '__main__':
    unittest.main()