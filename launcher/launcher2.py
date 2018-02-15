import os
import sys
import random
import subprocess
import shutil

from Tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename

#=======================================================

def selectedBtn(img):
	print("Select clicked img: ", img)
	launchGame()

#=======================================================
def deleteBtn(img):
	print("Delete clicked img: ", img)

#=======================================================

def addImage():
	print("add image button selected")
	# root.filename = tkFileDialog.askopenfiles(filtypes=(("JPEG files","*.jpg"),
														# ("GIF files","*.gif"),
														# ("PNG files","*.png")))
	# print(root.filename)
	source = askopenfilename(initialdir = "/", title = "Select file",
								filetypes = (("jpeg files","*.jpg"),
												("GIF files","*.gif"),
												("PNG files","*.png")))
	print("source", source)

	filename = source[source.rfind("/")+1:]
	newFilename = "yours_"+filename
	shutil.copy(source,"Assets/")
	os.rename("Assets/"+filename, "Assets/"+newFilename)

	subprocess.call(["python", "predictMulti.py", "Assets/"+newFilename])

	# initTk()
	
	launchGame()


#=======================================================

def getImages():

	path = 'assets/'

	images = []

	for dirname, dirnames, filenames in os.walk(path):
	    for filename in filenames:
	        file = os.path.join(dirname, filename)
	        if '.jpg' in file.lower() or '.gif' in file.lower() or '.png' in file.lower():
	            images.append(file)

	return images
#=======================================================

def launchGame():	# params will be paths to .txt files and image stream
	subprocess.call(["open", "testbuild.app"])

#=======================================================
def initTk():
	## Main window
	root = Tk()

	root.title("Whack-A-Mine")

	## Grid sizing behavior in window
	root.grid_rowconfigure(0, weight=1)
	root.grid_columnconfigure(0, weight=1)

	root.minsize(width=350, height=350)
	root.maxsize(width=350, height=350)





	## Canvas
	cnv = Canvas(root)
	cnv.grid(row=0, column=0, sticky='nswe')

	## Scrollbars for canvas
	vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
	vScroll.grid(row=0, column=1, sticky='ns')
	cnv.configure(yscrollcommand=vScroll.set)

	## Frame in canvas
	frame = Frame(cnv)
	## This puts the frame in the canvas's scrollable zone
	cnv.create_window(0, 0, window=frame, anchor='nw')
	## Frame contents

	frame.configure(background='black')

	heading = Label(frame, text="Whack-A-Mineeeeeeeeeeeeeeeeeeee").grid(row=0, columnspan=2)

	# heading.configure(background='blue')

	addButton = Button(frame, text="Add your own image", command=addImage)
	addButton.grid(row=1, columnspan=2)

	images = getImages()
	selectBtns = [None]*len(images)
	deleteBtns = [None]*len(images)

	for x in range(len(images)):

		im = Image.open(images[x])
		im = im.resize((150, 150), Image.ANTIALIAS)
		tkimage = ImageTk.PhotoImage(im)
		myvar = Label(frame, image = tkimage)
		myvar.image = tkimage
		myvar.grid(row=x+2, column=0)

		frameRightCol = Frame(frame)

		Label(frameRightCol, text=images[x]).pack()
		selectBtns[x] = Button(frameRightCol, text="Select", command=lambda x=x: selectedBtn(images[x]))
		selectBtns[x].pack()
		deleteBtns[x] = Button(frameRightCol, text="Delete", command=lambda x=x: deleteBtn(images[x]))
		deleteBtns[x].pack()

		frameRightCol.grid(row=x+2, column=1)
		frameRightCol.configure(background='blue')


	## Update display to get correct dimensions
	frame.update_idletasks()
	## Configure size of canvas's scrollable zone
	cnv.configure(scrollregion=(0, 0, frame.winfo_width(), frame.winfo_height()))
	## Go!


	root.mainloop()
#=======================================================


initTk()


