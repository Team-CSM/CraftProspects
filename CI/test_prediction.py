import unittest
import os 
import shutil
from Standalone.CNN.CNNbinary.predict.prediction import slice_image, os_walk




class test_prediction(unittest.TestCase):
    
    def test_slice_directory(self):
        slice_image("CI/orig.jpg",20)
        
        if os.path.exists("output/"):
            answer = True
        
        else:
            answer = False
        
        shutil.rmtree("slices/")
        self.assertTrue(answer)
        
    
    def test_slice_number(self):
        slice_image("CI/orig.jpg",20)
        file_list = os.listdir("slices/")
        shutil.rmtree('slices/')
        self.assertEqual(len(file_list),20)

    def test_os_walk(self):
        os_walk_list = os_walk('CI/slices/')
        file_list = os.listdir('CI/slices/')
       
        file_count = 0
        for file in file_list:
            if file[0] != ".":
                file_count += 1
        self.assertEqual(len(os_walk_list),file_count)

    


if __name__ == '__main__':
    unittest.main()