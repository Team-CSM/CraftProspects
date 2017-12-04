# CNN

Image Recognition software developed with Keras and TensorFlow to distinguish between categories supplied in the Kaggle [dataset](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/data). 

### Requirements
- `Python 3.5`
- `Keras 2.1.1`
- `Tensorflow 1.4.0`
- Reduced [data set](https://drive.google.com/file/d/1QjvzyQEgdijjch93Q7xfNklzLWy2lNob/view)

### How to run:
- Ensure CNN.py `train_data_dir` & `validation_data_dir` point to the correct folders from the reduced data set.
- `python CNN.py`

# demonstration

A visual representation of the prediction from CNN, which when given an .h5 file from the output of the CNN, will determine whether or not it believes the image passed to it is either a cloud, or clear primary. Used at the demonstration at the end of Sprint 1.

### How to run:
- Ensure that the .h5 file model is linked at the line `model = load_model(FILE_NAME)`
- Edit `test.command` to work on your own virtualenv (with tensor flow, eras etc installed)
- Choose an image to predict it’s outcome from the CNN
