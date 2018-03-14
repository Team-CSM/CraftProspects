"""Converts jpg images to RGB colour spectrum, in a new specified folder, s.t. there is no issues importing the images into Unity."""

from PIL import Image
import os

dirs = ["./artisinal_mine", "./cloudy", "./slash_burn", "./clear_primary"]

#For usage specify the output directory in the form <"NEW DIRECTORY">
outputdir = ""

for dir in dirs: 
    content = os.listdir(dir)
    #Loop images, and resave them as converted.
    for image in content:
        if (image != ".DS_Store"):
            name = image.split(".")[0]
            imagedir = (dir + "/" + image)
            im = Image.open((dir + "/" + image)).convert('RGB')
            im.save(outputdir + dir.split(".")[1] + "/" + name + ".jpg")