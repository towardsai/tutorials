#Import required libraries
import numpy as np
import pandas as pd
from keras.optimizers import SGD
from keras.datasets import cifar10
from keras.models import Sequential
from keras.utils import np_utils as utils
from keras.layers import Dropout, Dense, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D

#Load the Cifar01 dataset
(X, y), (X_test, y_test) = cifar10.load_data()

#Display the test dataset
X_test

#Normalize the data
X, X_test = X.astype("float32") / 255.0, X_test.astype("float32") / 255.0

#Convert to categorical
y, y_test = utils.to_categorical(y, 10), u.to_categorical(y_test, 10)

#Initialize the model
model = Sequential()

#Add a convolutional layer with test parameters
model.add(
    Conv2D(32, (3, 3), input_shape=(32, 32, 3), padding="same", activation="relu")
)

#Add the dropout rate
model.add(Dropout(0.2))

#Add another CNN layer with a valid padding value
model.add(Conv2D(32, (3, 3), activation="relu", padding="valid"))

#Add a max pooling lkayer
model.add(MaxPooling2D(pool_size=(2, 2)))

#Flatten the data
model.add(Flatten())

#Add a dense layer
model.add(Dense(512, activation="relu"))

#Add dropout
model.add(Dropout(0.3))

#Add the output dense layer
model.add(Dense(10, activation="softmax"))

#Compile the model
model.compile(
    loss="categorical_crossentropy",
    optimizer=SGD(momentum=0.5, decay=0.0004),
    metrics=["accuracy"],
)

#Fit the algorithm with a number of epochs, 25 in this case
model.fit(X, y, validation_data=(X_test, y_test), epochs=25, batch_size=512)

#Check the accuracy of the model
print("Accuracy: &2.f%%" %(model.evaluate(X_test, y_test)[1]*100))

#Max pooling shape
model.add(MaxPooling1D(pool_size=2))

#Filter shape
model.add(Conv1D(filters=32, kernel_size=3, padding="same", activation="relu"))

#Number of filters
model.add(Conv1D(filters=32, kernel_size=3, padding="same", activation="relu"))

#Add dropout
model.add(Dropout(0.2))

# Early stopping for overfitting
from keras.callbacks import EarlyStopping

earlystop = EarlyStopping(
    monitor="val_loss", min_delta=0, patience=3, verbose=1, restore_best_weights=True
)
