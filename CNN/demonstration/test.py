from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import sys
import os

imglist = []
window = tk.Tk()
window.withdraw()
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
imglist.append(filename)
model = load_model('/Users/craig/Documents/tp3/split/testing.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

size = 150, 150

class_to_name = ["clear_primary", "cloudy"]
for image in imglist:
    img = Image.open(image)
    img = img.resize(size, Image.ANTIALIAS)
    img = img.convert('RGB')
    x = np.asarray(img, dtype='float32')
    x = np.expand_dims(x, axis=0)
    x = x/255
    choice = model.predict(x)
    out1 = class_to_name[model.predict_classes(x)[0][0]]
    if (choice >= 0.5):
        out2 = str(round(choice[0][0]*100, 2)) + "%"
    else:
        out2 = str(round((1 - choice[0][0])*100, 2)) + "%"

def format(out1):
    return out1.replace("_", " ").title()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

screen_width = int((window.winfo_screenwidth()/2) - 200)
screen_height = int((window.winfo_screenheight()/2) - 200)
window.geometry("400x325+" + str(screen_width) + "+" + str(screen_height))
window.deiconify()
window.title("CNN Predictions")
window.configure(background='white')
img = ImageTk.PhotoImage(Image.open(filename))
panel = tk.Label(window, image = img)
panel.pack()
w = tk.Label(window, text="I'm about " + out2 + " sure this is "+ format(out1))
w.pack()
b = tk.Button(window, text="Choose Another", command=restart_program, pady = '3')
b.pack()
window.mainloop()