import sys
import os
import csv
import tkinter as tk
from tkinter.filedialog import askopenfilename
from keras.models import load_model
import numpy as np
from PIL import Image, ImageTk

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

class_to_name = ["clear", "cloudy"]
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

#Example: clear_primary to Clear Primary
def format(out1):
    return out1.replace("_", " ").title()

#If a user wants to select an other image, just restart the program
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# returns the actual values for the file, specified in the given CSV
def getvals(filename):
    csvFile=open("/Users/craig/Documents/tp3/split/data/train_v2.csv")
    reader=csv.reader(csvFile)
    for item in reader:
        if item[0] == filename:
            return item[1]
    return "None"

#getting the actual classes for the image
check = (getvals(os.path.basename(filename).split(".")[0]))

#just getting width and height in order to centre window
screen_width = int((window.winfo_screenwidth()/2) - 200)
screen_height = int((window.winfo_screenheight()/2) - 175)

window.geometry("400x425+" + str(screen_width) + "+" + str(screen_height))
window.deiconify()
window.title("CNN Predictions")

#importing image to the window
img = ImageTk.PhotoImage(Image.open(filename))
panel = tk.Label(window, image = img, height = "256", width = "256").pack()
T = tk.Text(window, height = 2)
T.config(font=("Arial"))
T.pack()
T.insert(tk.END,"I'm about " + out2 + " sure that is " + format(out1))
T.insert(tk.END, "\nActual: " + check + "\n")
T.tag_add("start", "1.10", "1.16")

T.tag_config("center", justify='center')
T.tag_add("center", 1.0, "end")

#highlights colour of certainty with colour codes
num = float(out2[:-1])
if(num >= 80):
    T.tag_config("start", foreground="green")
elif(num >= 70):
    T.tag_config("start", foreground="orange")
else:
    T.tag_config("start", foreground="red")


#output if the image is *actually* cloudy or clear
if (format(out1).lower() in check):
    result = tk.Label(window, text = "✓", fg = "green", font=(None, 50)).pack()
else:
    result = tk.Label(window, text = "✗", fg = "red", font=(None, 50)).pack()

b = tk.Button(window, text="Choose Another", command=restart_program, pady = '3', font=("Arial")).pack()
window.mainloop()