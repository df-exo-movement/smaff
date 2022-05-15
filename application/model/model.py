import numpy
import tensorflow as tf
from tensorflow import keras
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

train = ImageDataGenerator(rescale=1 / 255)

class_names = ['angry', 'disgust', 'fear', 'sad', 'surprise', 'happy', 'neutral']
train_dataset = train.flow_from_directory('./data/train', target_size=(200, 200),
                                          class_mode='categorical', color_mode="grayscale")

model = tf.keras.models.Sequential()
# model.add(keras.Input(shape=(200, 200, 3)))
model.add(tf.keras.layers.Conv2D(16, (3, 3), padding='same', activation='relu', input_shape=(200,200,1)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.MaxPool2D(2, 2))

model.add(tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.MaxPool2D(2, 2))

model.add(tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.MaxPool2D(2, 2))

model.add(tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.MaxPool2D(2, 2))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(512, activation='relu'))
model.add(tf.keras.layers.BatchNormalization())

model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.BatchNormalization())

model.add(tf.keras.layers.Dense(120, activation='relu'))
model.add(tf.keras.layers.BatchNormalization())

model.add(tf.keras.layers.Dense(4, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=0.0001)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=['accuracy'])

model.fit(train_dataset, batch_size=120, steps_per_epoch=200, epochs=15)

model.save('newemotion.h5')

