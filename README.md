# Whack-A-Mine
Web App and Standalone game based on neural network trained using a deep learning image classification algorithm with the help of [Keras](https://keras.io/) and [TensorFlow](https://www.tensorflow.org/). The neural network was trained with the supplied dataset in the Kaggle [dataset](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/data) and can now distinguish between 4 categories (clear, burn, cloudy and mine).

There are three choices of default images to play the game in the web app, but the standalone includes the functionality of image uploads.

Standalone versions can be downloaded in the web app https://whackamine.ml/ and cloned in our [github repository](https://github.com/Team-CSM).

Project code documentation can be viewed in https://whackamine.ml/Documentation/

## Directories' contents
- CI.			Continuous Integration to automate builds and tests scripts such as syntax errors.
- docs.			Dissertation of this project.
- Game.			Codebase of the game developed using [Unity](https://unity3d.com/).
- Standalone.	Python scripts used to train the different versions Convolutional Neural Network, data parse and launchers.
- WebServer.	Codebase of the webapp.

## Game
The game is a 2d image that was sliced into 9 further images, each in which the user is competing against the neural network. Each slice pops up on the screen in turn for a number of seconds depending on the difficulty level, as the user to select a grid of co-ordinates that they believe contain key labels (clouds, mines and slash'n'burn). One point will be awarded for each correct answer and one point will be deducted for clicking a box without any clouds. Double points for finding any mines or grids with slash and burn.

[![Screen_Shot_2018-02-14_at_16.07.34.png](https://s13.postimg.org/kb4jcxip3/Screen_Shot_2018-02-14_at_16.07.34.png)](https://postimg.org/image/ijbki0zc3/)

## Binary Convolutional Neural Network
- Initially at the start of the project, a binary decision neural network was developed in order to distinguish between clouds and clear skies, this classification is useful to satellites in order to preserve battery over cloudy skies as no other information can be gathered.

[![Screen_Shot_2018-02-14_at_15.58.01.png](https://s13.postimg.org/i5a8ig2dz/Screen_Shot_2018-02-14_at_15.58.01.png)](https://postimg.org/image/apaywneoj/)

- A simple GUI interface was created using Tkinter to display the results, in order to demonstrate progress to the client. The `.csv` file relating to the actual classification of the image is parsed, and matched to see if the prediciton made by the model is correct.

- Requirements:
	- Python 3.5
	- Keras 2.1.1
	- Tensorflow 1.4.0
	- Reduced [data set](https://drive.google.com/file/d/1QjvzyQEgdijjch93Q7xfNklzLWy2lNob/view)

- Run the binary CNN script:
	1. Ensure CNN.py `train_data_dir` & `validation_data_dir` point to the correct folders from the reduced data set.
	2. `python CNN.py`

- demonstration. A visual representation of the prediction from CNN, which when given an .h5 file from the output of the CNN, will determine whether or not it believes the image passed to it is either a cloud, or clear primary. Used at the demonstration at the end of Sprint 1.

- Run the demonstration interface:
	1. Ensure that the .h5 file model is linked at the line `model = load_model(FILE_NAME)`.
	2. Edit `test.command` to work on your own virtualenv (with tensor flow, eras etc installed).
	3. Choose an image to predict it’s outcome from the CNN

## Multi-class Convolutional Neural Network
Following up the binary network, we decided to expand to include other classes valuable to satellite image detection, such as deforestation (in form of slash'n'burn) and illegal mining activity. After some experimentation, as opposed to building the entire model, VGG19 was used in order to increase accuracy. When an image is selected for the game to be loaded, it is split into a 50x50 grid and input into the neural network, from there, the co-ordinates of key data are output to .txt files to be read into the game.

