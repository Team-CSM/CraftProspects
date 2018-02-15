import os
import sys
import random

from Tkinter import *
from PIL import Image, ImageTk
import tkFileDialog



def selectedBtn(img):
    print("Select clicked img: ", img)

def deleteBtn(img):
    print("Delete clicked img: ", img)

path = 'assets/'

images = []

for dirname, dirnames, filenames in os.walk(path):
    for filename in filenames:
        file = os.path.join(dirname, filename)
        if '.jpg' in file.lower() or '.gif' in file.lower() or '.png' in file.lower():
            images.append(file)


print images


## Main window
root = Tk()

root.title("Whack-A-Mine")

# root.minsize(width=500, height=500)
# root.maxsize(width=500, height=500)

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
frm = Frame(cnv)
## This puts the frame in the canvas's scrollable zone
cnv.create_window(0, 0, window=frm, anchor='nw')
## Frame contents

# labelText = StringVar()
# label = Label(frm, textvariable=labelText)
# labelText.set("Whack-A-Mine")
# label.grid(row=0, column=0)

Label(frm, text="Whack-A-Mineeeeeeeeeeeeeeeeeeee").grid(row=0, columnspan=3)

addButton = Button(frm, text="Add your own image")
addButton.grid(row=1, columnspan=3)

selectBtns = [None]*len(images)
deleteBtns = [None]*len(images)
for x in range(len(images)):
    im = Image.open(images[x])
    im = im.resize((150, 150), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(frm, image = tkimage)
    myvar.image = tkimage
    myvar.grid(row=x+2, column=0)
    selectBtns[x] = Button(frm, text="Select", command=lambda x=x: selectedBtn(images[x]))
    selectBtns[x].grid(row=x+2, column=1)
    deleteBtns[x] = Button(frm, text="Delete", command=lambda x=x: deleteBtn(images[x]))
    deleteBtns[x].grid(row=x+2, column=2)




## Update display to get correct dimensions
frm.update_idletasks()
## Configure size of canvas's scrollable zone
cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
## Go!


root.mainloop()





