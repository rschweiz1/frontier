import os

import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler

import frontier as ft

PATH = os.path.join(os.path.dirname(__file__), 'frontier','features', 'machine data.csv')

# load dataset
dataset = ft.scrub(PATH)
values = dataset.values
# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler()
scaled = scaler.fit_transform(values)
# specify the number of lag samples
n_days = 5
n_features = values.shape[1]
# frame as supervised learning
reframed = ft.series_to_supervised(scaled, n_days, 1)
# split into train and test sets
values = reframed.values
n_train_samples = round(0.6 * values.shape[0])
train = values[:n_train_samples, :]
test = values[n_train_samples:, :]
#split into input and outputs
n_obs = n_days * n_features
train_X, train_y = train[:, :n_obs], train[:, -n_features]
test_X, test_y = test[:, :n_obs], test[:, -n_features]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], n_days, n_features))
test_X = test_X.reshape((test_X.shape[0], n_days, n_features))
# build neural network
model = ft.RNN(train_X, train_y, test_X, test_y)
# begin learning process
model.learn()
# make a prediction
yhat = model.forecast()
# de-normalize predictions
test_X = test_X.reshape((test_X.shape[0], n_days * n_features))
inv_yhat = np.concatenate((yhat, test_X[:, -7:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:, 0]
# de-normalize actual results
test_y = test_y.reshape((len(test_y), 1))
inv_y = np.concatenate((test_y, test_X[:, -7:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:, 0]
# calculate percent error
score = 100 * (np.exp(np.sqrt(mean_squared_error(inv_y, inv_yhat))) - 1)
score = round(score, 2)
print('Average error: {}%'.format(score))
