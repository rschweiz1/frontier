import frontier
import pandas as pd
import numpy as np
import os

# Create Croup of Tickers

indices = pd.Series(['JKD', 'IJH', 'IJR', 'JKF','IJS', 'ICF',
                    'EFA', 'SCZ', 'EEM', 'SHV', 'IAU'])

print('Updating Indices...')

# Changesum is the compiled percent changes to put into the correlation matrix.

changesum = pd.DataFrame(frontier.Share(indices[0], 'Indices'))

# Path to filename.
cpath = os.path.join(os.path.dirname(__file__),
'database', 'Indices', 'Correlation Matrix.csv')


# Pull the % change data for all ETF's, join the columns, and save to CSV.

for i in range(1, indices.size):
    change = frontier.Share(indices[i], 'Indices')
    changesum = pd.concat([changesum, change], axis=1)

# Get correlation between asset classes. This is the data to be fed into the NN.

correlation = changesum.corr()
correlation.to_csv(cpath)

print('Done.')



schwab = pd.Series(['SCHX', 'SCHM', 'SCHA', 'FNDX', 'FNDA', 'SCHH',
                    'SCHF', 'SCHC', 'SCHE', 'FNDF', 'FNDC', 'FNDE',
                    'SCHZ', 'SCHO', 'SGOL'])


print('Updating Schwab Asset Classes...')

for i in range(schwab.size):
    change = frontier.Share(schwab[i], 'Schwab Asset Classes')


print('Done.')
