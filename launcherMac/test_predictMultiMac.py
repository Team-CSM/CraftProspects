import unittest 
import os 
import shutil
from predictMultiMac import slice
from predictMultiMac import predict
from predictMultiMac import class_to_name

class test_predictMultiMac(unittest.TestCase):
    
    # tests if number of slices created is equal to the number it was asked to be sliced.
    def testSliceNumber(self):
        if not os.path.exists("output/"):
            os.makedirs("output/")
        imagepath = "creator_creatorImage1/orig.jpg"
        number = 20
        slice(number,imagepath,"output/")
        list = os.listdir("output/")
        number_files = len(list)
        shutil.rmtree("output/")
        self.assertEqual(number,number_files)
    
    def testPredict_text(self):
        #check if the text files correspond to class_to_name.
        #recreates the slices.
        if not os.path.exists("output/"):
            os.makedirs("output/")

        imagepath = "creator_creatorImage1/orig.jpg"
        number = 20 
        slice(number,imagepath,"output/")
        list = os.listdir("output/")
        
        if not os.path.exists("output/text/"):
            os.makedirs("output/text/")
        
        for var in range(len(list)):
            list[var] = "output/"+list[var]
        
        predict(list,class_to_name,"output/text/")
        list = os.listdir("output/text/")
        
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