'''
 categorises images in a way that an image doesn't gets classified in more than one class
 only saves 340 images randomly selected in each class. This is because there are not enough slash_burn and artisinal_mine images
'''

import csv
from random import shuffle
import os
from shutil import copyfile



def populateDict(csvDir, classes):

	classFiles = {}
	alreadyAdded = []

	for name in classes:
		classFiles[name]=[]
		csvFile=open(csvDir)
		reader=csv.reader(csvFile)

	for row in reader:
	
		if row[1].find('slash_burn') != -1 and row[0] not in alreadyAdded:
			classFiles['slash_burn'].append(row[0])
			alreadyAdded.append(row[0])
	
		elif row[1].find('artisinal_mine') != -1 and row[0] not in alreadyAdded:
			classFiles['artisinal_mine'].append(row[0])
			alreadyAdded.append(row[0])
	
		elif row[1].find('cloudy') != -1 and row[0] not in alreadyAdded:
			if row[1].find('partly_cloudy') == -1:
				classFiles['cloudy'].append(row[0])
				alreadyAdded.append(row[0])
	
		elif row[1].find('clear primary') != -1 and row[0] not in alreadyAdded:
			classFiles['clear primary'].append(row[0])
			alreadyAdded.append(row[0])

	return classFiles


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

#--------------------------------------------------

if __name__ == '__main__':
	classes = ["clear primary", "cloudy", "artisinal_mine", "slash_burn"]
	csvDir = "train_v2.csv"

	classFiles = populateDict(csvDir, classes)

	# only get save first 340 images in each class
	for cl in classFiles:
		shuffle(classFiles[cl])
		classFiles[cl] = classFiles[cl][:340]

	makeFolders(classes,"train-jpg")
	relocateFiles(classFiles,"train-jpg")
