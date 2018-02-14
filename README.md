# Craft Prospects 'Whack-A-Mole'

Image Recognition software developed with Keras and TensorFlow to distinguish between categories supplied in the Kaggle [dataset](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/data). A game has been built upon the neural network in order to demonstrate the uses of machine learning to potential clients of the company.

## Binary Convolutional Neural Network
Initially at the start of the project, a binary decision neural network was developed in order to distinguish between clouds and clear skies, this classification is useful to satellites in order to preserve battery over cloudy skies as no other information can be gathered.

[![Screen_Shot_2018-02-14_at_15.58.01.png](https://s13.postimg.org/i5a8ig2dz/Screen_Shot_2018-02-14_at_15.58.01.png)](https://postimg.org/image/apaywneoj/)

A simple GUI interface was created using Tkinter to display the results, in order to demonstrate progress to the client. The `.csv` file relating to the actual classification of the image is parsed, and matched to see if the prediciton made by the model is correct.

## Multi-class Convolutional Neural Network
Following up the binary network, we decided to expand to include other classes valuable to satellite image detection, such as deforestation (in form of slash'n'burn) and illegal mining activity. After some experimentation, as opposed to building the entire model, VGG19 was used in order to increase accuracy. When an image is selected for the game to be loaded, it is split into a 50x50 grid and input into the neural network, from there, the co-ordinates of key data are output to .txt files to be read into the game.

## Multi-label Convolutional Neural Network
A multi-label is currently being developed in order to detect multiple occurances of labels within a single image, such as if a mine was detected, but the scene was also cloudy, the network will return both results relating to the image.

## Game
The game is essentially a 2d scroller in which the user is competing against the neural network. The image moves across the scene, as the user has to select co-ordinates that they believe contain key labels (clouds, mines and slash'n'burn).

[![Screen_Shot_2018-02-14_at_16.07.34.png](https://s13.postimg.org/kb4jcxip3/Screen_Shot_2018-02-14_at_16.07.34.png)](https://postimg.org/image/ijbki0zc3/)

There is a varying difficulty, which changes the accuracy of the model used to compete with the user, rules describing how the operate the in-game satellite, and high scores to compare to other users.

## Executable

An executable should be uploaded by the end of March, when the project is complete.
