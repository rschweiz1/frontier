import os
import datetime

import numpy as np
import pandas as pd
import pandas_datareader as pdr
import scipy.stats as ss
import time


class OneSource:
    """Returns every ticker from Schwab's OneSource ETFbase"""

    def __init__(self):

        dmst = ['DEF', 'DEUS', 'DGRS', 'DGRW', 'DWAS', 'ESGL', 'EWSC', 'FNDA',
                'FNDB', 'FNDX', 'JHML', 'JHMM', 'JPME', 'JPSE', 'JPUS', 'KNOW',
                'KRMA', 'MDYG', 'MDYV', 'ONEO', 'ONEV', 'ONEY', 'PDP', 'PKW',
                'QQQE', 'QUS', 'RDIV', 'RFG', 'RFV', 'RPG', 'RPV', 'RSP',
                'RWJ', 'RWK', 'RWL', 'RZG', 'RZV', 'SCHA', 'SCHB', 'SCHD',
                'SCHG', 'SCHK', 'SCHM', 'SCHV', 'SCHX', 'SDOG', 'SHE', 'SLYG',
                'SLYV', 'SPHB', 'SPLV', 'SPMD', 'SPYD', 'SPYX', 'SYE', 'SYG',
                'SYV', 'WMCR', 'XLG'
               ]

        intl = ['ACIM', 'CQQQ', 'CWI', 'DBAW', 'DBEF', 'DBEM', 'DBEZ', 'DDWM',
                'DEEF', 'DEMG', 'DGRE', 'DNL', 'DWX', 'DXGE', 'DXJS', 'EDIV',
                'EDOG', 'EEB', 'EELV', 'ESGF', 'EUSC', 'EWEM', 'EWX', 'FEU',
                'FNDC', 'FNDE', 'FNDF', 'FRN', 'GMF', 'GXC', 'HDAW', 'HFXE',
                'HFXI', 'HFXJ', 'HGI', 'IDLV', 'IDOG', 'IHDG', 'JHDG', 'JHMD',
                'JPEH', 'JPEM', 'JPEU', 'JPGE', 'JPIH', 'JPIN', 'JPN', 'LOWC',
                'PAF', 'PID', 'PIE', 'PIN', 'PIZ', 'QCAN', 'QDEU', 'QEFA',
                'QEMM', 'QGBR', 'QJPN', 'SCHC', 'SCHE', 'SCHF', 'WDIV'
               ]

        bond = ['AGGE', 'AGGP', 'AGGY', 'AGZD', 'BKLN', 'BSCH', 'BSCI', 'BSCJ',
                'BSCK', 'BSCL', 'BSCM', 'BSCN', 'BSCO', 'BSCP', 'BSCQ', 'BSJH',
                'BSJI', 'BSJJ', 'BSJK', 'BSJL', 'BSJM', 'BSJN', 'BSJO', 'BWX',
                'BWZ', 'CJNK', 'CORP', 'CWB', 'DSUM', 'DWFI', 'FLRN', 'HYLB',
                'HYLV', 'HYMB', 'HYS', 'HYZD', 'IBND', 'PCY', 'PGHY', 'PHB',
                'RVNU', 'SCHO', 'SCHP', 'SCHR', 'SCHZ', 'SHM', 'SPTL', 'SRLN',
                'TFI', 'ZROZ'
               ]

        real = ['BNO', 'CPER', 'GCC', 'GLDW', 'GLTR', 'PALL', 'PPLT', 'SGOL',
                'SIVR', 'UGA', 'UNL', 'USCI', 'USL'
               ]

        sect = ['BOTZ', 'CGW', 'CROP', 'ENFR', 'EWRE', 'GHTI', 'GII', 'GNR',
                'GRES', 'JHMA', 'JHMC', 'JHME', 'JHMF', 'JHMH', 'JHMI', 'JHMS',
                'JHMT', 'JHMU', 'MLPA', 'MLPX', 'NANR', 'PBS', 'PSAU', 'RCD',
                'RGI', 'RHS', 'RTM', 'RWO', 'RWX', 'RYE', 'RYF', 'RYH', 'RYT',
                'RYU', 'SCHH', 'SGDM', 'ZMLP'
               ]

        spec = ['CVY', 'DYLS', 'FXA', 'FXB', 'FXC', 'FXE', 'FXF', 'FXS', 'FXY',
                'GAL', 'INKM', 'LALT', 'MNA', 'PGX', 'PSK', 'PUTW', 'QAI',
                'QMN', 'RLY', 'USDU', 'VRP', 'WDTI'
               ]

        self.tickers = sect

    def get(self,
            start='1/1/2010',
            end=pd.to_datetime('today'),
            source='google'):

        path = os.path.join(os.path.dirname(__file__),
                            '..', 'database', 'machine data.csv')
        df = pdr.DataReader(self.tickers, source, start, end).loc['Close']
        df.to_csv(path)


class Option():
    """
    Generates option object based on input data parameters.

    inputs: strike, date, bid, ask, delta, gamma, theta, vega

    outputs: none
    """
    def __init__(self, otype, underlying, strike, expiry, bid, ask, delta, gamma, theta, vega, IV):
        self.type = otype # Call or put
        self.underlying = underlying
        self.strike = strike
        self.expiry = date
        self.bid = bid
        self.ask = ask
        self.delta = delta
        self.gamma = gamma
        self.theta = theta
        self.vega = vega
        self.IV = IV

        now = datetime.datetime.now()
        self.TTM = self.expiry - now
        r = 1.02 # US federal funds rate
        self.d1 = (np.log(self.underlying/self.strike) + (r + self.IV**2 / 2) * T)/(self.IV * np.sqrt(TTM))
        self.d2 = (np.log(self.underlying/self.strike) + (r - self.IV**2 / 2) * T)/(self.IV * np.sqrt(TTM))

        if self.otype=="C":
            self.dist = self.underlying * ss.norm.cdf(self.d1) - self.strike * np.exp(-r * self.TTM) * ss.norm.cdf(self.d2)
        else:
            self.dist = self.strike * np.exp(-r * self.TTM) * ss.norm.cdf(-self.d2) - self.underlying * ss.norm.cdf(-self.d1)
        return
