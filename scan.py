import frontier
import pandas as pd
import numpy as np
import os

# Create Croup of Tickers

BlackRock = pd.Series(['JKD', 'IJH', 'IJR', 'JKF','IJS', 'ICF',
                    'EFA', 'SCZ', 'EEM', 'SHV', 'IAU'])

print('Updating BlackRock ETFs...')

# Changesum is the compiled percent changes to put into the correlation matrix.
# Pull the % change data for all ETF's, join the columns, and save to CSV.
changesum = pd.DataFrame(frontier.Share(BlackRock[0], 'BlackRock'))

for i in range(1, BlackRock.size):
    change = frontier.Share(BlackRock[i], 'BlackRock')
    changesum = pd.concat([changesum, change], axis=1)



changesum.to_csv(os.path.join(os.path.dirname(__file__),
'database', 'BlackRock', 'Compiled Data.csv'))

frontier.Alpha('BlackRock')

print('Done.')
