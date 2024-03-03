import numpy as np
#set the precision 4 decimal places to read from np.array
np.set_printoptions(suppress=True, precision=4)

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

load_model = tf.keras.models.load_model

model = load_model('model_1.h5')

def binToNum(binarr):  # mamy tutaj dla n
    "'function returns expected output from binar to naural'"
    result = 0
    for (index, bin) in enumerate(binarr):
        result += bin * pow(2, len(binarr)-1-index)
    return result

def predict_and_assert(input_array):
    "'function check if the model result is correct for input array represents binary number '"
    x = binToNum(input_array)
    input_array = np.array(input_array).reshape(1, 8)
    prediction = model.predict(input_array)
    assert round(prediction[0][0]) == x

#test
tab=[0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0]
predict_and_assert(tab)
tab=[0.0,0.0,0.0,0.0,1.0,1.0,0.0,0.0]
predict_and_assert(tab)
tab=[0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0]
predict_and_assert(tab)

print("The tests passed successfully")