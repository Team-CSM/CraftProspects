from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# import Image#, ImageTk
# from tkFileDialog import askopenfilename
from tkinter.filedialog import askopenfilename
import os
import subprocess
import tkinter.font as font

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

######################################################################################
def launchGame():
	# os.system("C:/Users/Adrian/Desktop/Launcher/GameWin.exe") # for windows
	# subprocess.call(["open", "GameMac3.app"]) #for mac
	os.system("open GameMac.app")
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
	newDir = "./players_"+uploadNameEntryText

	if not os.path.exists(newDir):
		os.makedirs(newDir)

	# subprocess.call(["cp", uploadPathEntryText, newDir])
	os.system("cp " + uploadPathEntryText + " " + newDir)
	beforePathName = newDir+'/'+imgOrigFileName
	afterPathName = newDir+"/orig.jpg"
	# subprocess.call(["mv", beforePathName, afterPathName])
	os.system("mv " + beforePathName + " " + afterPathName)
	print ("afterPathName: ", afterPathName)
	# subprocess.call(["python", "predictMulti.py", afterPathName])
	os.system("python predictMulti.py " + afterPathName)

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
	# print "imgActivePath: ", imgActivePath

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
	ownerImg = IMAGES_DICT[imgNameSelected][1]

	if (ownerImg == "creator"):
		popup("Cannot delete creators' images. You can only delete images you uploaded.")
		return

	# subprocess.call(["rm","-r",imgSelectedPath])
	os.system("rm -r " + imgSelectedPath)

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
	beforePath = imgSelectedPath
	afterPath = imgSelectedPath[:imgSelectedPath.rfind('_')+1]+renameEntryText

	# subprocess.call(["mv", beforePath, afterPath])
	os.system("mv " + beforePath + " " + afterPath)
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
