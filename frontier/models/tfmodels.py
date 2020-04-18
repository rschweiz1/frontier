from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential
from matplotlib import pyplot


class RNN():
    def __init__(self, train_X, train_y, test_X, test_y):
        # design network
        self.train_X = train_X
        self.train_y = train_y
        self.test_X = test_X
        self.test_y = test_y
        self.model = Sequential()
        self.model.add(LSTM(50, dropout=0.25, recurrent_dropout=0.25,
                            input_shape=(self.train_X.shape[1],
                                         self.train_X.shape[2])))
        self.model.add(Dense(1))
        self.model.compile(loss='mse', optimizer='adam')
    def learn(self):
        # fit network
        history = self.model.fit(self.train_X, self.train_y, epochs=20,
                                 validation_data=(self.test_X, self.test_y),
                                 verbose=2)
        pyplot.plot(history.history['loss'], label='train error')
        pyplot.plot(history.history['val_loss'], label='validation error')
        pyplot.legend()
        pyplot.show()
    def forecast(self):
        yhat = self.model.predict(self.test_X)
        return yhat
