We have the list consist of ones and zeros which represents the binary number. For example:
[0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0] represents 15.
Our model will have recognise from binary number to natural number.
The expected result is showed in predict.py. In this file is checked if your model was trained correctly.
1. *Kacper's files will be support for you. You have to do everything using floats, because only with that type of data the tensorflow is working.
3. Data_set was prepared by us. This is the description what it contains:
   a.the list which contains all 2^8-1 binary numbers(lists like [0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0])
   b.the list which contains list with the natural number corresponding binary
   c.Randomly select the numbers to training and test. I chose 9% lists from the prepared test to training and 1% to testing. Training data and testing data should be a disjoint sets.
   d.The input data should be a np.array, this is why we used x_train = np.array(x_train), for all lists.
You have to prepare the next steps using ready data_set:
3.Create model:
  a.Initialize
  b.Add layers
  c.model.summary()
4.Compile the model using Adam optimizer, fit the learning_rate.
5.Fit the model, increase, decrease the amount of epochs, check when the score is the same as expected
6.Save model
Expected output of this process is decreasing the function of loss to 0.
