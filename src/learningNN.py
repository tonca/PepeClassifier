# LSTM and CNN for sequence classification in the IMDB dataset
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Conv2D, GlobalAveragePooling2D, MaxPooling2D, Activation, Dropout, Flatten
from keras.layers.embeddings import Embedding
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
import h5py


BATCH_SIZE = 10 
TRAIN_SIZE = 800


# Load processed images
with h5py.File('data/processed/dataset.h5', 'r') as hf:
    X_data = hf['X'][:]
    Y_data = hf['Y'][:]

Y_data = Y_data.reshape((Y_data.shape[0],1))

X_train, X_test = X_data[:TRAIN_SIZE], X_data[TRAIN_SIZE:]
Y_train, Y_test = Y_data[:TRAIN_SIZE], Y_data[TRAIN_SIZE:]

print(X_train.shape)
print(Y_train.shape)

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255


model = Sequential()
model.add(Conv2D(16, (6, 6), padding='same',
                 input_shape=X_data.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(16, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(Dropout(0.85))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.8))
model.add(Dense(1))
model.add(Activation('sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(
        X_train, Y_train,
        epochs=10,
        batch_size=10)


print(model.summary())

# Final evaluation of the model
scores = model.evaluate(X_test, Y_test)

print("Accuracy: %.10f%%" % (scores[1]*100))