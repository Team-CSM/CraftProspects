from PIL import Image
import os

dirs = ["./artisinal_mine", "./cloudy", "./slash_burn", "./clear_primary"]
outputdir = "/Users/craig/Documents/tp3/split/kaggledata/data/validation/new"

for dir in dirs: 
    content = os.listdir(dir)

    for image in content:
        if (image != ".DS_Store"):
            name = image.split(".")[0]
            imagedir = (dir + "/" + image)
            im = Image.open((dir + "/" + image)).convert('RGB')
            im.save(outputdir + dir.split(".")[1] + "/" + name + ".jpg")