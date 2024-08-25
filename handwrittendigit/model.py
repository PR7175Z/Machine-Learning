import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split


train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

x = train.iloc[:, 1:785]
y = train.iloc[:, 0]
x_test = test.iloc[:, 0:784]

x_tsn = x/255

tsne = TSNE()

tsne_reshape = tsne.fit_transform(x_tsn)

xtrain, xvalidate, ytrain, yvalidate = train_test_split(x, y, test_size = 0.2, random_state = 1212)

xtrain_reshape = xtrain.tonumpy().reshape(33600, 28, 28)
ytrain_reshape = ytrain.values
xvalidate_reshape = xvalidate.tonumpy().reshape(8400, 28,28)
yvalidate_reshape =yvalidate.values
xtest_reshape = x_test.to_numpy().reshape(28000, 28, 28)

(_, IMAGEWIDTH, IMAGEHEIGHT) = xtrain_reshape.shape
IMAGECHANNEL = 1

xtrain_with_channel = xtrain_reshape.reshape(
    xtrain_reshape.shape[0],
    IMAGEWIDTH,
    IMAGEHEIGHT,
    IMAGECHANNEL,
)

xvalidate_with_channel = xvalidate_reshape.reshape(
    xvalidate_reshape.shape[0],
    IMAGEWIDTH,
    IMAGEHEIGHT,
    IMAGECHANNEL,
)

xtest_with_channel = xtest_reshape.reshape(
    xtest_reshape.shape[0],
    IMAGEWIDTH,
    IMAGEHEIGHT,
    IMAGECHANNEL,
)

xtrain_normailze = xtrain_with_channel/255
xvalidate_normalize = xvalidate_with_channel/255
xtest_normalize = xtest_with_channel/255

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Convolution2D(
    input_shape=(IMAGEWIDTH, IMAGEHEIGHT, IMAGECHANNEL),
    kernel_size=5,
    filters=8,
    strides=1,
    activation=tf.keras.activations.relu,
    kernel_initializer=tf.keras.initializers.VarianceScaling()
))

model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2, 2),
    strides=(2, 2)
))

model.add(tf.keras.layers.Convolution2D(
    kernel_size=5,
    filters=16,
    strides=1,
    activation=tf.keras.activations.relu,
    kernel_initializer=tf.keras.initializers.VarianceScaling()
))

model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2, 2),
    strides=(2, 2)
))

model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(
    units=128,
    activation=tf.keras.activations.relu
));

model.add(tf.keras.layers.Dropout(0.2))

model.add(tf.keras.layers.Dense(
    units=10,
    activation=tf.keras.activations.softmax,
    kernel_initializer=tf.keras.initializers.VarianceScaling()
))

adam_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

model.compile(
    optimizer=adam_optimizer,
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    metrics=['accuracy']
)

training_history = model.fit(
    xtrain_normailze,
    ytrain_reshape,
    epochs=10,
    validation_data=(xvalidate_normalize, yvalidate_reshape),
)