import unittest 
import os 
import shutil
import csv
from Standalone.dataparse.categoriseData import makeFolders
from Standalone.dataparse.categoriseData import populateDict

class test_categorisedata(unittest.TestCase):
    

    def test_makeFolders_number(self):
        classes_list = ['a','b','c','d']
        if not os.path.exists("output/"):
            os.makedirs("output")
        makeFolders(classes_list,"output")
        folder_list = os.listdir("output/")
        
        shutil.rmtree("output/")
        # checks if the number of folders created is equal to the number of classes:
        self.assertEqual(len(folder_list),len(classes_list))
    
    def test_makeFolders_name(self):  
        classes_list = ['a','b','c','d']
        if not os.path.exists("output/"):
            os.makedirs("output")
        makeFolders(classes_list,"output")
        folder_list = os.listdir("output/")
        
        # checks if the names correspond to classes:
        for folder in folder_list:
            if folder in classes_list:
                answer = True
            else:
                answer = False 
        
        shutil.rmtree("output/")
        self.assertTrue(answer)
    
    def test_makeFolders_spaces(self):
        classes_list = ['clear primary','artisinal mine','paritally_cloudy']
        if not os.path.exists("output/"):
             os.makedirs("output")
        makeFolders(classes_list,"output")
        folder_list = os.listdir("output/")

        # checks if the spaces are replaced with underscores:
        for folder in folder_list:
            if " " in folder:
                answer = False
            else:
                answer = True 
        self.assertTrue(answer)


   
    def test_populateDict_list_number(self):
        classes_list = ["clear primary", "cloudy", "artisinal_mine", "slash_burn"]
        csv_dict = populateDict('CI/test.csv',classes_list)
        
        # tests if the number of elements in the dictionary value list adds up to the total number of rows in the csv file
        rows = 8

        total_number = 0
        for key in csv_dict.keys():
            value_list = csv_dict[key]
            for var in value_list:
                total_number += 1 
        
        self.assertEqual(total_number,rows)

    def test_populateDict_repeat(self):
        classes_list = ["clear primary", "cloudy", "artisinal_mine", "slash_burn"]
        csv_dict = populateDict('CI/test.csv',classes_list)

        # tests if there are repeats of the same image listed for each class. Fails if there are:
        repeat_dict  = {}
        csvFile=open('CI/test.csv')
        reader=csv.reader(csvFile)
        for line in reader:
            if "image_name" not in line: 
                repeat_dict[line[0]] = 0
        csvFile.close()
        
        for key in csv_dict.keys():
            value_list = csv_dict[key]
            for var in value_list:
                if var in repeat_dict:
                    repeat_dict[var] = repeat_dict[var] + 1
        
        for key in repeat_dict.keys():
            
            if repeat_dict[key] == 1:
                answer = True
            else:
                answer = False
       
        self.assertTrue(answer)

    


if __name__ == '__main__':
    unittest.main()