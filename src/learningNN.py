# LSTM and CNN for sequence classification in the IMDB dataset
import numpy as np
import pickle

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Conv2D, GlobalAveragePooling2D, MaxPooling2D, Activation, Dropout, Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator

BATCH_SIZE = 10 
TRAIN_SIZE = 100


# Load processed images
input_file = open("data/processed/X.pkl", 'rb')
X_data = pickle.load(input_file)

input_file = open("data/processed/Y.pkl", 'rb')
Y_data = pickle.load(input_file)

X_train, X_test = X_data[:TRAIN_SIZE], X_data[TRAIN_SIZE:]
Y_train, Y_test = Y_data[:TRAIN_SIZE], Y_data[TRAIN_SIZE:]



model = Sequential()
model.add(Conv2D(16, (3, 3), padding='same',
                 input_shape=X_data.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(16, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('softmax'))

# # create the model
# model = Sequential()
# model.add(Dense(32, input_shape=(None,256), activation='relu'))
# model.add(Conv2D(64, 4, activation='relu'))
# model.add(MaxPooling2D(3))
# model.add(Conv2D(128, 4, activation='relu'))
# model.add(Conv2D(128, 4, activation='relu'))
# model.add(GlobalAveragePooling2D())
# model.add(Dense(2, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow(
        X_train,
        Y_train,
        batch_size=BATCH_SIZE)

validation_generator = test_datagen.flow(
        X_test,
        Y_test,
        batch_size=BATCH_SIZE)

model.fit_generator(
        train_generator,
        steps_per_epoch=20,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=800)



print(model.summary())

# Final evaluation of the model
scores = model.evaluate_generator(X_test, 100)

print("Accuracy: %.10f%%" % (scores[1]*100))