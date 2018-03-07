from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# import Image#, ImageTk
# from tkFileDialog import askopenfilename
from tkinter.filedialog import askopenfilename
import os
import subprocess
from scipy import optimize
import tkinter.font as font
import sys
import numpy
from keras import *
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import image_slicer

#classes = burns, cloud, mines, clear

# images/players_imagetest.jpg
# images/players_imagetest_cloud.txt
######################################################################################
PATH = "Asset1/"
IMAGES_DICT = {} # { imageName: [path, owner]} # owner = players/creator/selects
LOGFILEPATH = "logfile.txt"
CLASSNAMES = ["burns", "cloud", "mines"]
FONTBTN="Futura 12 bold"
FONTLABEL="Futura 12 bold"
CURSORBTN = "center_ptr"


img_width, img_height = 64, 64
model_path = 'model.h5'
model_weights_path = 'weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

class_to_name = ["clear", "cloudy", "mine", "slash"]

# python predictMulti.py ./players_money/orig.jpg
globalImgPath = "ohno"

#print ("PREDICTMULTI imgPath: ", imgPath)
#print ("PREDICTMULTI dirPath: ", dirPath)

######################################################################################
def launchGame():
    os.system("WhackAMine.exe") # for windows
    # subprocess.call(["open", "GameMac3.app"]) #for mac
    #os.system("open GameMac.app")
    root.destroy()

######################################################################################
def getImage(imgPath):
    # print "imgPath: ", imgPath
    img = Image.open(imgPath).resize((165, 165), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img
######################################################################################
def updateLsbox():
    lsbox.delete(0, END)
    for dirname, dirnames, filenames in os.walk("./"):
        if (dirname[:9]=="./players" or dirname[:9]=="./creator"):
            imageName = dirname[dirname.rfind('_')+1:]
            path = dirname+'/'
            owner = dirname[2:dirname.rfind('_')]
            IMAGES_DICT[imageName] = [path, owner]
            lsbox.insert(END,imageName)

    # print "IMAGES_DICT: ", IMAGES_DICT

######################################################################################

def browse():
    source = askopenfilename(initialdir = "/", title = "Select file",
                                filetypes = (("jpeg files","*.jpg"),
                                                ("GIF files","*.gif"),
                                                ("PNG files","*.png")))
    # print("source", source)

    uploadPathVar.set(source)

def maine(imgPathe):
    imgPath = imgPathe
    dirPath = imgPath[:imgPath.rfind('\\')+1]
    #dirPath = dirPath[1:]
    #imgPath = imgPath[1:]
    IMAGE = "."+imgPath
    # location = dirPath + IMAGE.split('.')[0] + '_' + 'slices'
    locationSlices = dirPath + 'slices'
    locationSlices = locationSlices.replace("/", "\\")

    print(imgPath)

    if not os.path.exists(locationSlices):
        os.makedirs(locationSlices)
        print("make slices dir")
        slice(900, IMAGE, locationSlices)

    imgstr = []

    # Add all slices to the imgstr
    for root, dirs, filenames in os.walk(locationSlices):
        for f in filenames:
            if (f.startswith('.') == False):
                imgstr.append(locationSlices + '/' + f)

    print("imgstr: ", len(imgstr))



    # Getting predictions for all the slices from the model
    predict(imgstr, class_to_name, dirPath)

    # outloc = dirPath
    # if not os.path.exists(outloc):
    # Finally splitting the input image into 9 slices, with set ratio to be input to game.
    slice(9, IMAGE, dirPath)
    
    print("resizing...")
    for root, dirs, filenames in os.walk(dirPath):
        for f in filenames:
            if f[-3:]==".png":
                im = Image.open(dirPath + f)
                nx, ny = im.size
                im = im.resize((int(nx*1.4), ny), Image.BICUBIC)
                im.save(dirPath + f)

    # subprocess.call(["rm","-r",locationSlices]) #cleanup= delete the thousands of slices
    os.system("rd /s /q " + locationSlices)
    print("done")

def slice(number, IMAGE, location):
    # slice image for stream and add to the slices folder
    
    print("slicing...")
    IMAGE = IMAGE[1:]
    tiles = image_slicer.slice(IMAGE, number, save=False)
    print("save in folder:", location)
    image_slicer.save_tiles(tiles, directory=location, prefix='slice')
    # image_slicer.save_tiles(tiles, directory=location)


def predict(imgstr, class_to_name, dirPath):
    print("predicting...")
    for image in imgstr:
        x = load_img(image, target_size=(img_width,img_height))

        x = img_to_array(x)
        x = numpy.expand_dims(x, axis=0)
        # normalise
        x = x/255
        
        predictions = model.predict(x) #predictions in each class
        pred = numpy.argmax(predictions[0]) #winner index

        if (max(predictions[0]) > 0.5):
            out1 = class_to_name[pred]

            #write coordinates to log files to help out with input to game
            f = open(dirPath+out1+".txt", "a")
            f.write(image[image.rfind('/')+7:-4].replace("_", ",") + "_")
            f.close() 


#maine()
######################################################################################
def upload():

    uploadPathEntryText = uploadPathEntry.get()
    uploadNameEntryText = uploadNameEntry.get()


    if (uploadPathEntryText == "") or (uploadNameEntryText == ""):
        popup("Must specify path and name of image to upload.")
        return
    if uploadNameEntryText in IMAGES_DICT:
        popup("Image name already exists. Change name of image to rename it to.")
        return

    imgOrigFileName = uploadPathEntryText[uploadPathEntryText.rfind("/")+1:]
    newDir = "players_"+uploadNameEntryText
    newupet = os.path.dirname(uploadPathEntryText)
    newupet = newupet.replace('/', "\\")
    newupet = newupet + "\\" + imgOrigFileName
#    print("newupet: ", newupet)
    if not os.path.exists(newDir):
        os.makedirs(newDir)
    #subprocess.call(["copy", uploadPathEntryText, newDir])
    os.system('copy "' + newupet + '" "'  + newDir + '\"')
    os.system("copy " + uploadPathEntryText + " " + newDir)

    beforePathName = newDir+'/'+imgOrigFileName
    beforePathName = beforePathName.replace('/', "\\")
    afterPathName = newDir+"/orig.jpg"
    afterPathName = afterPathName.replace('/', "\\")
    globalImgPath = afterPathName
    # subprocess.call(["move", beforePathName, afterPathName])
    os.system("move " + beforePathName + " " + afterPathName)

    # subprocess.call(["python", "predictMulti.py", afterPathName])
    # os.system("python predictMulti.py /" + afterPathName)
	
    maine(afterPathName)
	
    #os.system("predictMulti.exe " + afterPathName)

    print("after predictiMulti.py ran")
	
    
    updateLsbox()

######################################################################################
def view():
    selection = lsbox.curselection()
    if (len(selection) == 0):
        popup("No item selected.")
        return    
    imgNameSelected = lsbox.get(selection[0])
    imgActivePath = IMAGES_DICT[imgNameSelected][0]
	
    img = getImage(imgActivePath+"orig.jpg")
    myvar = Label(selectedLab, image = img)
    myvar.image = img
    myvar.grid(row=0, column=0)
######################################################################################
def delete():

    selection = lsbox.curselection()

    if (len(selection) == 0):
        popup("No item selected.")
        return

    imgNameSelected = lsbox.get(selection[0])
    imgSelectedPath = IMAGES_DICT[imgNameSelected][0]
    imgSelectedPath = imgSelectedPath[2:-1]
    ownerImg = IMAGES_DICT[imgNameSelected][1]
 #   print("imgselectedpath", imgSelectedPath)
    if (ownerImg == "creator"):
        popup("Cannot delete creators' images. You can only delete images you uploaded.")
        return

    # subprocess.call(["rm","-r",imgSelectedPath])
    os.system("rd /s /q " + imgSelectedPath)

    updateLsbox()

######################################################################################

def select():

    selection = lsbox.curselection()

    if (len(selection) == 0):
        popup("No item selected.")
        return

    imgNameSelected = lsbox.get(selection[0])
    imgSelectedPath = IMAGES_DICT[imgNameSelected][0]                

    file = open(LOGFILEPATH, "w")
    file.write(imgSelectedPath)
    file.close()

    launchGame()
######################################################################################
def rename():

    selection = lsbox.curselection()
    renameEntryText = renameEntry.get()


    if len(selection) == 0 or renameEntryText == "":
        popup("Must select item and specify name to rename image to.")
        return

    if renameEntryText in IMAGES_DICT:
        popup("Image name already exists. Change name of image to rename it to.")
        return

    imgNameSelected = lsbox.get(selection[0])
    imgSelectedPath = IMAGES_DICT[imgNameSelected][0]
    ownerImg = IMAGES_DICT[imgNameSelected][1]

    if (ownerImg == "creator"):
        popup("Cannot rename creators' images. You can only rename images you uploaded.")
        return

    # print "----", renameEntryText, imgNameSelected, imgSelectedPath, ownerImg
    
    beforePath = imgSelectedPath[2:-1]
    afterPath = imgSelectedPath[:imgSelectedPath.rfind('_')+1] + renameEntryText
    afterPath = afterPath[2:]

    # subprocess.call(["mv", beforePath, afterPath])
    os.system("move " + beforePath + " " + afterPath)
    updateLsbox()
######################################################################################
def popup(msg):
    # print "ERROR: ", msg
    messagebox.showinfo("Alert", msg)

######################################################################################

root = Tk()

root.title("Whack-A-Mine")
root.resizable(False,False)



heading = Label(root, text="Whack-A-Mine\n(Select image to play)", font = "Futura 24 bold")
heading.grid(row=0, columnspan=3, sticky="we")
heading.configure(background='pale green')

frameUpload = Frame(root)
frameUpload.grid(row=1, columnspan=3, sticky="nsew")
frameUpload.grid_rowconfigure(0, weight=1)
frameUpload.grid_columnconfigure(0, weight=1)



uploadLabel = Label(frameUpload, text="Upload your own image", font=FONTLABEL).grid(row=0, columnspan=3, sticky=NSEW)
uploadNameLabel = Label(frameUpload, text="Name", font=FONTLABEL).grid(row=1, column=0)
uploadPathLabel = Label(frameUpload, text="Path", font=FONTLABEL).grid(row=2, column=0)


uploadNameEntry = Entry(frameUpload, width=50, relief=RIDGE)
uploadPathVar = StringVar()
uploadPathEntry = Entry(frameUpload, textvariable=uploadPathVar, width=50, relief=RIDGE)

browseBtn = Button(frameUpload, text="Browse", command=browse, font=FONTBTN, cursor=CURSORBTN, bg="green")
uploadBtn = Button(frameUpload, text="Upload", command=upload, font=FONTBTN, cursor=CURSORBTN)

uploadNameEntry.grid(row=1, column=1, sticky=W)
uploadPathEntry.grid(row=2, column=1, sticky=W)

browseBtn.grid(row=2, column=2, sticky=E)
uploadBtn.grid(row=3, columnspan=3, sticky=NSEW)


frameList = Frame(root)
frameList.grid(row=2, column=0)

lsbox = Listbox(frameList)#, width=25, height=25)
scrollbar = Scrollbar(frameList, orient="vertical")
lsbox.config(background='pale green')
scrollbar.config(command=lsbox.yview)
lsbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
lsbox.pack(side="left", fill="y")
lsbox.selection_set(first=0)


frameBtns = Frame(root)
frameBtns.grid(row=2, column=1)

viewBtn = Button(frameBtns, text="View", command=view, font=FONTBTN, cursor=CURSORBTN).pack()
selectBtn = Button(frameBtns, text="Select", command=select, font=FONTBTN, cursor=CURSORBTN).pack()
deleteBtn = Button(frameBtns, text="Delete", command=delete, font=FONTBTN, cursor=CURSORBTN).pack()

renameLabel = Label(frameBtns, text="Rename:", font=FONTLABEL)
renameEntry = Entry(frameBtns, relief=RIDGE)
renameBtn = Button(frameBtns, text="Rename", command=rename, font=FONTBTN, cursor=CURSORBTN)
renameLabel.pack()
renameEntry.pack()
renameBtn.pack()


selectedLab = Label(root, width=20, height=10, text="Select image to view here")
selectedLab.grid(row=2, column=2)
selectedLab.configure(background='pale green')

updateLsbox()


root.mainloop()



# def getLastPlayed():
#     imgInLog = ""
#     file = open(LOGFILEPATH)
#     lines = file.readlines()
#     print "lines: ", lines

#     for line in lines:
#         if ('.jpg' in line.lower()) or ('.gif' in line.lower()) or ('.png' in line.lower()):
#             print "line: ", line
#             imgInLog = line
#     file.close()

#     if imgInLog[-1] == '\n':
#         imgInLog = imgInLog[:-1]
#     print "imgInLog: ", imgInLog

#     return imgInLog

# lastPlayedImg = getLastPlayed()
# lastPlayedImg = getImage(lastPlayedImg)
# lastPlayedImgBtn = Button(text="Select this last image you played", image=lastPlayedImg, compound="left", command=launchGame)
# lastPlayedImgBtn.config(image=lastPlayedImg)
# lastPlayedImgBtn.grid(row=3, columnspan=3, sticky="we")

