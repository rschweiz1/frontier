import frontier
import numpy as np

dow30 = np.array(['AAPL', 'AXP', 'BA', 'CAT', 'CSCO',
                    'CVX', 'DIS', 'DWDP', 'GE', 'GS',
                    'HD', 'IBM', 'INTC', 'JNJ', 'JPM',
                    'KO', 'MCD', 'MMM', 'MRK', 'MSFT',
                    'NKE', 'PFE', 'PG', 'TRV', 'UNH',
                    'UTX', 'V', 'VZ', 'WMT', 'XOM'])

for i in range (dow30.size):
    frontier.Share(dow30[i])
