from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Whack-A-Mine")
root.configure(background='gray')


heading = Label(root, text="Whack-A-Mine (Select image to play)")
heading.grid(row=0, columnspan=3, sticky="we")
heading.configure(background='blue')

addBtn = Button(root, text="Select your own image")
addBtn.grid(row=1, columnspan=3, sticky="we")

frameList = Frame(root)
frameList.grid(row=2, column=0)

lsbox = Listbox(frameList, width=25, height=25)
lsbox.pack(side="left", fill="y")
lsbox.config(background='green')
for i in range(100):
	lsbox.insert(i,i)

scrollbar = Scrollbar(frameList, orient="vertical")
scrollbar.config(command=lsbox.yview)
scrollbar.pack(side="right", fill="y")

lsbox.config(yscrollcommand=scrollbar.set)


frameBtns = Frame(root)
frameBtns.grid(row=2, column=1)

viewBtn = Button(frameBtns, text="View")
viewBtn.pack()
selectBtn = Button(frameBtns, text="Select")
selectBtn.pack()
renameBtn = Button(frameBtns, text="Rename")
renameBtn.pack()
deleteBtn = Button(frameBtns, text="Delete")
deleteBtn.pack()

image = Label(root, width=25, height=25)
image.grid(row=2, column=2)
image.configure(background='yellow')


lastPlayedImg = Image.open("Assets/imagetest.jpg").resize((150, 150), Image.ANTIALIAS)
lastPlayedImg = ImageTk.PhotoImage(lastPlayedImg)
lastPlayedImgBtn = Button(text="Select this last image you played", image=lastPlayedImg, compound="left")
lastPlayedImgBtn.config(image=lastPlayedImg)
lastPlayedImgBtn.grid(row=3, columnspan=3, sticky="we")







root.mainloop()