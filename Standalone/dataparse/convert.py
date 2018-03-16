"""!@brief Converts jpg images to RGB colour spectrum, in a new specified folder, so there is no issues importing the images into Unity.
"""

from PIL import Image
import os

def convert(dirs, outputdir):
    """Takes in the directories that need to be parsed for images, and the output path. Converts the images in the directories to RGB
    and saves them to the output directory."""
    for dir in dirs: 
        content = os.listdir(dir)
        #Loop images, and resave them as converted.
        for image in content:
            if (image != ".DS_Store"):
                name = image.split(".")[0]
                im = Image.open((dir + "/" + image)).convert('RGB')
                im.save(outputdir + dir.split(".")[1] + "/" + name + ".jpg")

dirs = ["./artisinal_mine", "./cloudy", "./slash_burn", "./clear_primary"]
outputdir = ""
convert(dirs, outputdir)