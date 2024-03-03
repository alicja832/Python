#mamy tablice zawierajaca 0 i 1 bedaca reprezentacja binarna liczby, chcemy zamienic te tablice na liczbe naturalna
import os
import random
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

# adding aliases
Sequential = tf.keras.models.Sequential
Dense = tf.keras.layers.Dense
Dropout = tf.keras.layers.Dropout
BatchNormalization = tf.keras.layers.BatchNormalization
load = tf.keras.models.load_model
to_categorical = tf.keras.utils.to_categorical
SGD = tf.keras.optimizers.SGD
save_model = tf.keras.models.save_model


def binToNum(binarr):  # mamy tutaj dla n
    result = 0
    for (index, bin) in enumerate(binarr):
        result += bin * pow(2, len(binarr)-1-index)
    return result
#okreslam ile bitowa bedzie ta liczba
n=8
#set of all binary numbers with n-bits
x=[]
#corresponding to them natural numbers
y=[]
k=[]
#inserting into and array of binary numbers sequentially
for j in range (pow(2,n)):
    el=j
    k=[]
    while(el>1):
        k.append(float(el%2))
        el=int(el/2)
    if el==1:
        k.append(float(1))
    while(len(k)<(n)):
        k.append(float(0))
    k.reverse()
    x.append(k)
    y.append([float(j)])

# preparing data set
x_test=[]
y_test=[]
x_train=[]
y_train=[]

#choosing testing data and training data
data=int(len(x)*0.4);
train=int(len(x)*0.3);

#testing data and training data should be a disjoint sets
unic_numeric=random.sample(range(len(x)),data);
numeric=sorted(unic_numeric,reverse=True);

for i in range(train):
    x_train.append(x[numeric[i]])
    y_train.append(y[numeric[i]])
for i in range(train,data):
    x_test.append(x[numeric[i]])
    y_test.append(y[numeric[i]])




y_train = np.array(y_train);
y_test = np.array(y_test);

x_train = np.array(x_train);
x_test = np.array(x_test);

# initialize model
model = Sequential()
#
# # 784 inputs
model.add(Dense(94, activation='linear', input_shape=(n, )))  # hidden layer
model.add(Dense(64, activation='linear'))  # output layer

model.summary()
# # # #
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(learning_rate=0.07), metrics=['accuracy'])
# # # # # #
model.fit(x_train, y_train, epochs=450, verbose=1, validation_data=(x_test, y_test))
# # # # # # #S
save_model(model, 'model_1.h5')
