"""!@brief GUI prediction for Binary Neural Network, used to demonstrate progress to client.
Used as a demonstration of the neural network at the end of Sprint 2. GUI interface which allows a user to select an image. This image is then classified by the 
neural network, and the certainty is displayed. If the file exists in the kaggle dataset CSV file, the correct class will be displayed, and a 
tick or a cross will represent whether the classification was accurate.
"""

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

# For usage, change MODEL_LOCATION and CSV_LOCATION to = "<.H5 OR CSV FILE PATH>"
MODEL_LOCATION = ""
CSV_LOCATION = ""

# Since binary classification, only 2 class names required. 
class_to_name = ["cloudy", "clear"]

# Show an "Open" dialog box for user to select image, and return the path to the selected file
filename = askopenfilename()

def modelLoader(model_loc):
    """Given the path to a .h5 model file, loads and compiles the model."""
    model = load_model(model_loc)
    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
    return model

def initImage(filename):
    """Converts image to suitable format to be input into the model. 
    Rescales by 1/255 to account for RGB value coefficients."""
    size = 150, 150
    # Convert image to suitable format to be input into the model. 
    # Rescale by 1/255 to account for RGB value coefficients.
    img = Image.open(filename)
    img = img.resize(size, Image.ANTIALIAS)
    img = img.convert('RGB')
    x = np.asarray(img, dtype='float32')
    x = np.expand_dims(x, axis=0)
    x = x/255
    return x

def predictImage(image, model):
    """Given an augmented image, the function returns the prediction from the model, 
    the class name of the prediction and the certainty percentage."""
    # Get the prediction from the model and obtain the class name.
    choice = model.predict(image)
    print(choice)
    classString = class_to_name[model.predict_classes(image)[0][0]]

    # Checking if the prediction is substantial evidence to use that class.
    # Display as certainty percentage
    if (choice >= 0.5):
        certainty= str(round(choice[0][0]*100, 2)) + "%"
    # If not display as uncertainty percentage
    else:
        certainty = str(round((1 - choice[0][0])*100, 2)) + "%"
    return choice, classString, certainty

def format(category):
    """Given a category name, returns the category name with spaces instead of underscores, 
    and formatted to Title Case. clear_primary -> Clear Primary"""
    return category.replace("_", " ").title()

def restart_program():
    """Restarts the current program, so user can select another image to predict."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def getvals(filename):
    """Returns the actual image classification, specified in the given CSV. If not present "None" returned."""
    csvFile=open(CSV_LOCATION)
    reader=csv.reader(csvFile)
    for item in reader:
        if item[0] == filename:
            return item[1]
    return "None"

model = modelLoader(MODEL_LOCATION)
scaledImage = initImage(filename)
choice, out1, out2 = predictImage(scaledImage, model)

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