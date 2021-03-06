from keras.datasets import mnist
import matplotlib. pyplot as plt

# Load dataset (download if needed)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# plt.subplot(221)
# plt.imshow(X_train[0], cmap=plt.get_cmap('gray'))
# plt.subplot(222)
# plt.imshow(X_train[1], cmap=plt.get_cmap('gray'))
# plt.subplot(223)
# plt.imshow(X_train[2], cmap=plt.get_cmap('gray'))
# plt.subplot(224)
# plt.imshow(X_train[3], cmap=plt.get_cmap('gray'))

# plt.show()

import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

# fix the seed 
seed = 7
numpy.random.seed(seed)

# Input image dimensions
img_rows, img_cols = 28, 28

if K.image_data_format() == 'channels_first':
    X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols).astype('float32')
    input_shape = (1, img_rows, img_cols)
else: # channels_last
    X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1).astype('float32')
    input_shape = (img_rows, img_cols, 1)


print("Input Shape: ", input_shape)


# Normalize: the value are between [0, 255]
X_train = X_train / 255
X_test = X_test / 255


# Output: one hot encoding
# Example - [ 0 0 0 0 0 1 0 0 0 0 ]
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_train.shape[1]



def baseline_model():
    model = Sequential()
    model.add(Conv2D(8, (3,3), input_shape=input_shape, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(4, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    
    return model

# build a model
model = baseline_model()

# Fit 
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3,
          batch_size=32, verbose=2)

model.save('./api/main/data/model.h5')

# Final eval
scores = model.evaluate(X_test, y_test, verbose=0)
print("CNN error: %.2f%%" % (100 - scores[1]*100))