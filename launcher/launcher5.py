from tkinter import *
from PIL import Image, ImageTk
import os
import subprocess
#classes = burn, cloud, mine, clear
# images/players_imagetest.jpg
# images/players_imagetest_cloud.txt
######################################################################################
PATH = 'images/'
IMAGES_DICT = {} # { imageName: [path, owner]} # owner = players/creator/selects
LOGFILEPATH = "images/logfile.log"

######################################################################################
def getImage(imgPath):
	print "imgPath: ", imgPath
	img = Image.open(imgPath).resize((150, 150), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	return img


 
######################################################################################
def updateLsbox():

	lsbox.delete(0, END)

	for dirname, dirnames, filenames in os.walk(PATH):
	    for filename in filenames:
	        file = os.path.join(dirname, filename)
	        if ('.jpg' in file.lower()) or ('.gif' in file.lower()) or ('.png' in file.lower()):
	            # print("path, owner, imgname : ", file, file[7:14], file[15:-4])
	            path = file
	            owner = file[7:14]
	            imgname = file[15:-4]
	            IMAGES_DICT[imgname] = [path, owner]
	            lsbox.insert(END,imgname)


######################################################################################
def launchGame():
	subprocess.call(["open", "testbuild.app"])

######################################################################################
def view():
	imgNameActive = lsbox.get('active')
	imgActivePath = IMAGES_DICT[imgNameActive][0]
	img = getImage(imgActivePath)
	myvar = Label(selectedLab, image = img)
	myvar.image = img
	myvar.grid(row=0, column=0)
######################################################################################
def delete():
	imgNameActive = lsbox.get('active')
	imgActivePath = IMAGES_DICT[imgNameActive][0]
	ownerImg = IMAGES_DICT[imgNameActive][1]

	if (ownerImg == "creator"):
		print "Cannot delete creators' images. You can only delete images you uploaded."
		return

	txtClearPath = PATH + ownerImg + "_" + imgNameActive + "_clear.txt" 
	txtBurnPath = PATH + ownerImg + "_" + imgNameActive + "_burn.txt" 
	txtMinePath = PATH + ownerImg + "_" + imgNameActive + "_mine.txt" 
	txtCloudPath = PATH + ownerImg + "_" + imgNameActive + "_cloud.txt"

	print "deleteImg: ", imgActivePath
	print "deleteTxts: ", txtClearPath, txtBurnPath, txtMinePath, txtCloudPath

	subprocess.call(["rm", imgActivePath])
	subprocess.call(["rm", txtClearPath])
	subprocess.call(["rm", txtBurnPath])
	subprocess.call(["rm", txtMinePath])
	subprocess.call(["rm", txtCloudPath])

	root.after(1000, updateLsbox)

######################################################################################

def select():
	imgNameActive = lsbox.get('active')
	imgActivePath = IMAGES_DICT[imgNameActive][0]
	ownerImg = IMAGES_DICT[imgNameActive][1]

	toWrite = ""

	for dirname, dirnames, filenames in os.walk(PATH):
	    for filename in filenames:
	        file = os.path.join(dirname, filename)
	        if (imgNameActive in file):
	        	print "file: ", file
	        	toWrite += file + '\n'
	
	toWrite = toWrite[:-1]	# deletes the last '\n'
	file = open(LOGFILEPATH, "w")
	file.write(toWrite)

	file.close()

	launchGame()
######################################################################################
def rename():
	imgNameActive = lsbox.get('active')
	imgActivePath = IMAGES_DICT[imgNameActive][0]
	ownerImg = IMAGES_DICT[imgNameActive][1]

	if (ownerImg == "creator"):
		print "Cannot rename creators' images. You can only rename images you uploaded."
		return

######################################################################################


root = Tk()
root.title("Whack-A-Mine")
root.configure(background='gray')
root.resizable(False,False)



heading = Label(root, text="Whack-A-Mine (Select image to play)")
heading.grid(row=0, columnspan=3, sticky="we")
heading.configure(background='blue')

frameUpload = Frame(root)
frameUpload.grid(row=1, columnspan=3, sticky="nsew")
frameUpload.grid_rowconfigure(0, weight=1)
frameUpload.grid_columnconfigure(0, weight=1)


uploadLabel = Label(frameUpload, text="Upload your own image").grid(row=0, columnspan=3, sticky=NSEW)

uploadNameLabel = Label(frameUpload, text="Name").grid(row=1, column=0)
uploadNameEntry = Entry(frameUpload, width=50).grid(row=1, column=1, sticky=W)
 
uploadDirLabel = Label(frameUpload, text="Path").grid(row=2, column=0)
uploadDirEntry = Entry(frameUpload, width=50).grid(row=2, column=1, sticky=W)

browseBtn = Button(frameUpload, text="Browse").grid(row=2, column=2, sticky=E)
uploadBtn = Button(frameUpload, text="Upload").grid(row=3, columnspan=3, sticky=NSEW)

frameList = Frame(root)
frameList.grid(row=2, column=0)

lsbox = Listbox(frameList, width=25, height=25)
scrollbar = Scrollbar(frameList, orient="vertical")
lsbox.config(background='green')
scrollbar.config(command=lsbox.yview)
lsbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
lsbox.pack(side="left", fill="y")
updateLsbox()


frameBtns = Frame(root)
frameBtns.grid(row=2, column=1)

viewBtn = Button(frameBtns, text="View", command=view).pack()
selectBtn = Button(frameBtns, text="Select", command=select).pack()
deleteBtn = Button(frameBtns, text="Delete", command=delete).pack()

renameLabel = Label(frameBtns, text="Rename:").pack()
renameEntry = Entry(frameBtns).pack()
renameBtn = Button(frameBtns, text="Rename", command=rename).pack()



selectedLab = Label(root, width=25, height=25)
selectedLab.grid(row=2, column=2)
selectedLab.configure(background='yellow')




root.mainloop()



# def getLastPlayed():
# 	imgInLog = ""
# 	file = open(LOGFILEPATH)
# 	lines = file.readlines()
# 	print "lines: ", lines

# 	for line in lines:
# 		if ('.jpg' in line.lower()) or ('.gif' in line.lower()) or ('.png' in line.lower()):
# 			print "line: ", line
# 			imgInLog = line
# 	file.close()

# 	if imgInLog[-1] == '\n':
# 		imgInLog = imgInLog[:-1]
# 	print "imgInLog: ", imgInLog

# 	return imgInLog

# lastPlayedImg = getLastPlayed()
# lastPlayedImg = getImage(lastPlayedImg)
# lastPlayedImgBtn = Button(text="Select this last image you played", image=lastPlayedImg, compound="left", command=launchGame)
# lastPlayedImgBtn.config(image=lastPlayedImg)
# lastPlayedImgBtn.grid(row=3, columnspan=3, sticky="we")
