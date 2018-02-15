import os
import sys
import random
import subprocess

from Tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename


def selectedBtn(img):
	print("Select clicked img: ", img)
	subprocess.call(["open", "testbuild.app"])

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
	filepath = askopenfilename(initialdir = "/", title = "Select file",
								filetypes = (("jpeg files","*.jpg"),
												("GIF files","*.gif"),
												("PNG files","*.png")))
	print("filepath", filepath)

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

images = getImages()

## Main window
root = Tk()

root.title("Whack-A-Mine")

## Grid sizing behavior in window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


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


Label(frame, text="Whack-A-Mineeeeeeeeeeeeeeeeeeee").grid(row=0, columnspan=3)

addButton = Button(frame, text="Add your own image", command=addImage)
addButton.grid(row=1, columnspan=3)

selectBtns = [None]*len(images)
deleteBtns = [None]*len(images)
for x in range(len(images)):
    im = Image.open(images[x])
    im = im.resize((150, 150), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(frame, image = tkimage)
    myvar.image = tkimage
    myvar.grid(row=x+2, column=0)
    selectBtns[x] = Button(frame, text="Select", command=lambda x=x: selectedBtn(images[x]))
    selectBtns[x].grid(row=x+2, column=1)
    deleteBtns[x] = Button(frame, text="Delete", command=lambda x=x: deleteBtn(images[x]))
    deleteBtns[x].grid(row=x+2, column=2)




## Update display to get correct dimensions
frame.update_idletasks()
## Configure size of canvas's scrollable zone
cnv.configure(scrollregion=(0, 0, frame.winfo_width(), frame.winfo_height()))
## Go!


root.mainloop()





