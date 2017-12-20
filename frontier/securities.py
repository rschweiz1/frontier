import os

import pandas as pd
import pandas_datareader.data as web


class OneSource:
    """Returns every ticker from Schwab's OneSource ETFbase using get()"""

    def __init__(self):

        dmst = ['DEE', 'DEUS', 'DGRS', 'DGRW', 'DWAS', 'ESGL', 'EWSC',
                'FNDA', 'FNDB', 'FNDX', 'JHML', 'JHMM', 'JPME', 'JPSE',
                'JPUS', 'KNOW', 'KRMA', 'MDYG', 'MDYV', 'ONEO', 'ONEV',
                'ONEY', 'PDP', 'PKW', 'QQQE', 'QUS', 'RDIV', 'RFG', 'RFV',
                'RPG', 'RPV', 'RSP', 'RWJ', 'RWK', 'RWL', 'RZG', 'RZV',
                'SCHA', 'SCHB', 'SCHD', 'SCHG', 'SCHK', 'SCHM', 'SCHV',
                'SCHX', 'SDOG', 'SHE', 'SLYG', 'SLYV', 'SPHB', 'SPLV',
                'SPMD', 'SPYD', 'SPYX', 'SYE', 'SYG', 'SYV', 'WMCR', 'XLG'
               ]

        intl = ['ACIM', 'CQQQ', 'CWI', 'DBAW', 'DBEF', 'DBEM', 'DBEZ',
                'DDWM', 'DEEF', 'DEMG', 'DGRE', 'DNL', 'DWX', 'DXGE',
                'DXJS', 'EDIV', 'EDOG', 'EEB', 'EELV', 'ESGF', 'EUSC',
                'EWEM', 'EWX', 'FEU', 'FNDC', 'FNDE', 'FNDF', 'FRN', 'GMF',
                'GXC', 'HDAW', 'HFXE', 'HFXI', 'HFXJ', 'HGI', 'IDLV',
                'IDOG', 'IHDG', 'JHDG', 'JHMD', 'JPEH', 'JPEM', 'JPEU',
                'JPGE', 'JPIH', 'JPIN', 'JPN', 'LOWC', 'PAF', 'PID', 'PIE',
                'PIN', 'PIZ', 'QCAN', 'QDEU', 'QEFA', 'QEMM', 'QGBR',
                'QJPN', 'SCHC', 'SCHE', 'SCHF', 'WDIV'
               ]

        bond = ['AGGE', 'AGGP', 'AGGY', 'AGZD', 'BKLN', 'BSCH', 'BSCI',
                'BSCJ', 'BSCK', 'BSCL', 'BSCM', 'BSCN', 'BSCO', 'BSJH',
                'BSJI', 'BSJJ', 'BSJK', 'BSJL', 'BSJM', 'BSJN', 'BSJO',
                'BWX', 'BWZ', 'CJNK', 'CORP', 'CWB', 'DSUM', 'DWFI', 'FLRN',
                'HYLB', 'HYS', 'HYZD', 'IBND', 'PCY', 'PGHY', 'PHB', 'RVNU',
                'SCHO', 'SCHP', 'SCHR', 'SCHZ', 'SHM', 'SPTL', 'SRLN',
                'TFI', 'ZROZ'
               ]

        real = ['BNO', 'CPER', 'GCC', 'GLDW', 'GLTR', 'PALL', 'PPLT',
                'SGOL', 'SIVR', 'UGA', 'UNL', 'USCI', 'USL'
               ]

        sect = ['BOTZ', 'CGW', 'CROP', 'ENFR', 'EWRE', 'GHTI', 'GII', 'GNR',
                'GRES', 'JHMA', 'JHMC', 'JHME', 'JHMF', 'JHMH', 'JHMI',
                'JHMS', 'JHMT', 'JHMU', 'MLPA', 'MLPX', 'NANR', 'PBS',
                'PSAU', 'RCD', 'RGI', 'RHS', 'RTM', 'RWO', 'RWX', 'RYE',
                'RYF', 'RYH', 'RYT', 'RYU', 'SCHH', 'SGDM', 'ZMLP'
               ]

        spec = ['CVY', 'DYLS', 'FXA', 'FXB', 'FXC', 'FXE', 'FXF', 'FXS', 'FXY',
                'GAL', 'INKM', 'LALT', 'MNA', 'PGX', 'PSK', 'PUTW', 'QAI',
                'QMN', 'RLY', 'USDU', 'VRP', 'WDTI'
               ]

        self.tickers = dmst + intl + real + sect

        def get(self,
                start='1/1/2010',
                end=pd.to_datetime('today'),
                source='google'):

            path = os.path.join(os.path.dirname(__file__),
                                '..', 'database', 'machine data.csv')
            df = web.DataReader(self.tickers, source, start, end).loc['Close']
            df.to_csv(path)
