import frontier
import pandas as pd
import numpy as np
import os

# Create Croup of Tickers

BlackRock = np.array(['JKD', 'IJH', 'IJR', 'JKF','IJS', 'ICF',
                    'EFA', 'SCZ', 'EEM', 'IAU'])

print('Updating BlackRock ETFs...')

frontier.ETF(BlackRock, 'BlackRock')


print('Done.')
