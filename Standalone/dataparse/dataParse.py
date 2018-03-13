import csv
import os
from shutil import copyfile

#create an array of the classes we are using. In this case we are using 2 classes, clear primary and cloudy

classes = ["clear primary", "cloudy", "artisinal_mine", "slash_burn"]

#create a dictionary that will store the file names. {classname: [filename]}

classFiles = {}

for name in classes:
    classFiles[name]=[]


csvFile=open("/Users/craig/Documents/tp3/split/data/train_v2.csv")
reader=csv.reader(csvFile)
for row in reader:
    for name in classes:
        if name in row[1]:
            array = classFiles.get(name)
            array.append(row[0])
            classFiles[name] = array




def makeFolders(classes_list,path):
    for var in classes_list:
        if " " in var:
            newpath=path+"/"+var.replace(" ","_")
        else:
            newpath=path+"/"+var
        if not os.path.exists(newpath):
            os.makedirs(newpath)


def relocateFiles(dictionary,path):
    #gets the keys of the dictionary
    keys=dictionary.keys()

    for key in keys:
        if " " in key:
            newpath=path+"/"+key.replace(" ","_") #if there is a space in the name its replaced with an underscore.
        else:
            newpath=path+"/"+key

        #gets the array of files:
        fileArray = dictionary.get(key)

        for file in fileArray:
            oldfilePath = path+"/"+file+".jpg"
            newFilePath = newpath +"/"+file+".jpg"
            copyfile(oldfilePath,newFilePath)



makeFolders(classes,"/Users/craig/Documents/tp3/split/data/train-jpg")
relocateFiles(classFiles,"/Users/craig/Documents/tp3/split/data/train-jpg")



