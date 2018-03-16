# Whack-A-Mine
Web App and Standalone game based on neural network trained using a deep learning image classification algorithm using the [Keras](https://keras.io/) and [TensorFlow](https://www.tensorflow.org/) frameworks. The neural network was trained with the supplied dataset in the Kaggle [dataset](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/data) and can now distinguish between 4 categories (clear, burn, cloudy and mine).

There is one default image to play the game in the web app, but the standalone includes the functionality of image uploads.

Both versions can be downloaded at the web app https://whackamine.ml/ or cloned from our [github repository](https://github.com/Team-CSM).

Project code documentation can be viewed at https://whackamine.ml/Documentation/

## Repository's contents
- CI.			Continuous Integration to automate builds and tests scripts such as syntax errors.
- docs.			Dissertation of this project.
- Game.			Codebase of the game developed using [Unity](https://unity3d.com/).
- Standalone.	Python scripts used to train the different versions Convolutional Neural Network, data parse and launchers.
- WebServer.	Codebase of the webapp.

## CNN
- Requirements:
	- h5py (2.7.1)
	- image (1.5.19)
	- image-slicer (0.1.1)
	- Keras (2.1.4)
	- macholib (1.9)
	- numpy (1.14.1)
	- Pillow (5.0.0)
	- PyInstaller (3.3.1)
	- scipy (1.0.0)
	- tensorflow (1.5.0)
	- Reduced [data set](https://drive.google.com/file/d/1QjvzyQEgdijjch93Q7xfNklzLWy2lNob/view)

## Binary Convolutional Neural Network
- Initially at the start of the project, a binary decision neural network was developed in order to distinguish between clouds and clear skies, this classification is useful to satellites in order to preserve battery over cloudy skies as no other information can be gathered.

[![Screen_Shot_2018-02-14_at_15.58.01.png](https://s13.postimg.org/i5a8ig2dz/Screen_Shot_2018-02-14_at_15.58.01.png)](https://postimg.org/image/apaywneoj/)

- A simple GUI interface was created using Tkinter to display the results, in order to demonstrate progress to the client. The `.csv` file relating to the actual classification of the image is parsed, and matched to see if the prediciton made by the model is correct.

- Training of the binary CNN:
- Run the binary CNN script for training:
	1. Ensure CNN.py `train_data_dir` & `validation_data_dir` point to the correct folders from the reduced data set.
	2. `python BinaryCNN.py`

- Demonstration. A visual representation of the prediction from CNN, which when given an .h5 file from the output of the CNN, will determine whether or not it believes the image passed to it is either a cloud, or clear primary. Used at the demonstration at the end of Sprint 1.

- Run the demonstration interface:
	1. Ensure that the .h5 file model and csv is linked at the line `MODEL_LOCATION = ""` and `CSV_LOCATION = ""`.
    2. `python BinaryDemo.py`
	3. Choose an image to predict it’s outcome from the CNN

- Prediction. Used to split a singulatr image into slices, and predict those slices. Slice classifications output to txt files for usage in the game.

- Run the prediction:
	1. Ensure that the .h5 file model and image is linked at the line `MODEL_LOCATION = ""` and `IMAGE_LOCATION = ""`.
    2. `python BinaryPredict.py`
	3. Choose an image to predict it’s outcome from the CNN

## Multi-class Convolutional Neural Network
Following up the binary network, we decided to expand to include other classes valuable to satellite image detection, such as deforestation (in form of slash'n'burn) and illegal mining activity. After some experimentation, as opposed to building the entire model, VGG19 was used in order to increase accuracy. When an image is selected for the game to be loaded, it is split into a 30x30 grid and input into the neural network, from there, the co-ordinates of key data are output to .txt files to be read into the game.

- Run the training:
	1. Ensure CNN.py `TRAIN_DATA_PATH` & `VALIDATION_DATA_PATH` point to the correct folders from the reduced data set.
	2. `python MultiCNN_v2.py`

# Standalone Mac and Windows

![Launcher User Interface](https://s14.postimg.org/cjzb0t7td/Screen_Shot_2018-03-15_at_17.46.05.png)


## Game
The game is a 2d image that was sliced into 9 further images, each in which the user is competing against the neural network. Each slice pops up on the screen in turn for a number of seconds depending on the difficulty level, as the user to select a grid of co-ordinates that they believe contain key labels (clouds, mines and slash'n'burn). One point will be awarded for each correct answer and one point will be deducted for clicking a box without any clouds. Double points for finding any mines or grids with slash and burn.

## Play
Simply run the application "Whack-A-Mine" and select an image to start playing. An alias (File->Make alias) can be made so you are able to move the application elsewhere in your system.

## Game Mechanics
- Use the magnifying glass to identify which grids contain one or multiple clouds and click on them.
- You will be awarded 1 point for each correct answer and 1 point will be deducted for clicking a box without any clouds.
- You will get double points for finding any mines or grids with slash and burn.
- Controls:
	- Left click to select
	- m to mute
	- q to return to menu

## Launcher features
- Upload your own images which will be copied into a new directory that is named beginning in "players_(name of image the user inputs)"
- Able to rename the images the user uploads, but unable to rename default images
- Able to delete own images, but unable to delete default images
- Able to preview the image first before playing the game

## Directory Structure and Contents
- Whack-A-Mine.app (Mac). Whack-A-Mine.bat (Windows)
	- application made using AppleScript and ShellScript to put all the scripts together
	- batch file to put all the scripts together
- subfolders with names that begin with "creator" and "players" store important information of the corresponding image. Creator means defaults we provide and players mean images players have uploaded.
	- orig.jpg is the full image
	- 9 slice png images are the slices of the full image
	- txt files each named a category that the neural network predicted the original image contains. Each text file contains the coordinates of areas on the image that that the neural network predicts it to be.
- launcherMac.py and launcherWin.py
	- source code of launcher
- GameMac.app (Mac). WhackAMine.exe, WhackAMine_Data (Windows)
	- Mac version of the game application. Relies on logfile.txt, highscore.txt and the images subfolders.
- model.h5 and weights.h5
	- produced by the neural network and used to predict when uploading images.
- highscore.txt
	- populated as the player plays the game
- logfile.txt
	- populated as the user selects an image on the launcher interface.
- __pycache__, build, dist, launcherMac.spec
	- produced when packaging scripts using [PyInstaller](https://www.pyinstaller.org/)

## Running without the built application
- Requirements:
	- h5py (2.7.1)
	- image (1.5.19)
	- image-slicer (0.1.1)
	- Keras (2.1.4)
	- macholib (1.9)
	- numpy (1.14.1)
	- Pillow (5.0.0)
	- PyInstaller (3.3.1)
	- scipy (1.0.0)
	- tensorflow (1.5.0)

- Open terminal in this directory and type ```python launcherMac.py```

## Building with pyinstaller
- When making changes to the launcher source code which can be retrieved from the main repository, the scripts must be packaged again. Ensure that the following files are in the same directory:
	- launcherMac.py
	- subfolders of images
	- GameMac.app
	- Whack-A-Mine.app
- model.h5 and weights.h5
- logfile.txt
- highscore.txt


## Description
Welcome. Thank you for downloading our game, Whack-A-Mine. This game's intention is to demonstrate our neural network that is trained to detect clouds and illegal activity in satellite images.

Be sure to check out our website, https://whackamine.ml

## Play
Simply run the application "Whack-A-Mine" and select an image to start playing. An alias (File->Make alias) can be made so you are able to move the application elsewhere in your system.

## Game Mechanics
- Use the magnifying glass to identify which grids contain one or multiple clouds and click on them.
- You will be awarded 1 point for each correct answer and 1 point will be deducted for clicking a box without any clouds.
- You will get double points for finding any mines or grids with slash and burn.
- Controls:
	- Left click to select
	- m to mute
	- q to return to menu

## Launcher features
- Upload your own images which will be copied into a new directory that is named beginning in "players_(name of image the user inputs)"
- Able to rename the images the user uploads, but unable to rename default images
- Able to delete own images, but unable to delete default images
- Able to preview the image first before playing the game

## Directory Structure and Contents
- Whack-A-Mine.app (Mac). Whack-A-Mine.bat (Windows)
	- application made using AppleScript and ShellScript to put all the scripts together
	- batch file to put all the scripts together
- subfolders with names that begin with "creator" and "players" store important information of the corresponding image. Creator means defaults we provide and players mean images players have uploaded.
	- orig.jpg is the full image
	- 9 slice png images are the slices of the full image
	- txt files each named a category that the neural network predicted the original image contains. Each text file contains the coordinates of areas on the image that that the neural network predicts it to be.
- launcherMac.py and launcherWin.py
	- source code of launcher
- GameMac.app (Mac). WhackAMine.exe, WhackAMine_Data (Windows)
	- Mac version of the game application. Relies on logfile.txt, highscore.txt and the images subfolders.
- model.h5 and weights.h5
	- produced by the neural network and used to predict when uploading images.
- highscore.txt
	- populated as the player plays the game
- logfile.txt
	- populated as the user selects an image on the launcher interface.
- __pycache__, build, dist, launcherMac.spec
	- produced when packaging scripts using [PyInstaller](https://www.pyinstaller.org/)

## Running without the built application
- Requirements:
	- h5py (2.7.1)
	- image (1.5.19)
	- image-slicer (0.1.1)
	- Keras (2.1.4)
	- macholib (1.9)
	- numpy (1.14.1)
	- Pillow (5.0.0)
	- PyInstaller (3.3.1)
	- scipy (1.0.0)
	- tensorflow (1.5.0)

- Open terminal in this directory and type ```python launcherMac.py```

## Building with pyinstaller
- When making changes to the launcher source code which can be retrieved from the main repository, the scripts must be packaged again. Ensure that the following files are in the same directory:
	- launcherMac.py
	- subfolders of images
	- GameMac.app
	- Whack-A-Mine.app
- model.h5 and weights.h5
- logfile.txt
- highscore.txt

1. Edit 'hook-_tkinter.py' in site-packages/pyinstaller/blob/develop/PyInstaller/hooks/hook-_tkinter.py
    a. change 'tcl' to 'tclResources'
    b. change 'tk' to 'tkResources'
2. Edit 'pyi_rth_tkinter.py' in site-packages/pyinstaller/blob/develop/PyInstaller/loader/rthooks/pyi_rth__tkinter.py
    a. change 'tcl' to 'tclResources'
    b. change 'tk' to 'tkResources'
3. Remove all references to scipy in 'image.py' from Python36\Lib\site-packages\tensorflow\python\keras_impl\keras\preprocessing\image.py
4. Build with 'pyinstaller --hidden-import=scipy._lib.messagestream --hidden-import=h5py.defs --hidden-import=h5py.utils launcher.py'
5. Copy 'tcl' from System/Library/Frameworks/tcl.framework/versions/8.5/tcl to dist
6. Copy 'tk' from System/Library/Frameworks/tk.framework/versions/8.5/tk to dist
7. ```pyinstaller --hidden-import=scipy._lib.messagestream --hidden-import=h5py.defs --hidden-import=h5py.utils launcherMac.py```

## Credits

Developers:
- Dan Cristian Cecoi
- Eerika Emilia Haajanen
- Craig Stewart Massie
- Frances Lou Ramirez
- Chun Pang Adrian Wong

Special thanks: 
- Kevin Tozer
- Panagiotis Antoniou
