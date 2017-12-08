import numpy as np


class OneSource:
    """Returns every ticker from Schwab's OneSource ETF using get()"""

    def __init__(self):

        domestic = ['DEE', 'DEUS', 'DGRS', 'DGRW', 'DWAS', 'ESGL', 'EWSC',
                    'FNDA', 'FNDB', 'FNDX', 'JHML', 'JHMM', 'JPME', 'JPSE',
                    'JPUS', 'KNOW', 'KRMA', 'MDYG', 'MDYV', 'ONEO', 'ONEV',
                    'ONEY', 'PDP', 'PKW', 'QQQE', 'QUS', 'RDIV', 'RFG', 'RFV',
                    'RPG', 'RPV', 'RSP', 'RWJ', 'RWK', 'RWL', 'RZG', 'RZV',
                    'SCHA', 'SCHB', 'SCHD', 'SCHG', 'SCHK', 'SCHM', 'SCHV',
                    'SCHX', 'SDOG', 'SHE', 'SLYG', 'SLYV', 'SPHB', 'SPLV',
                    'SPMD', 'SPYD', 'SPYX', 'SYE', 'SYG', 'SYV', 'WMCR', 'XLG'
                    ]

        internat = ['ACIM', 'CQQQ', 'CWI', 'DBAW', 'DBEF', 'DBEM', 'DBEZ',
                    'DDWM', 'DEEF', 'DEMG', 'DGRE', 'DNL', 'DWX', 'DXGE',
                    'DXJS', 'EDIV', 'EDOG', 'EEB', 'EELV', 'ESGF', 'EUSC',
                    'EWEM', 'EWX', 'FEU', 'FNDC', 'FNDE', 'FNDF', 'FRN', 'GMF',
                    'GXC', 'HDAW', 'HFXE', 'HFXI', 'HFXJ', 'HGI', 'IDLV',
                    'IDOG', 'IHDG', 'JHDG', 'JHMD', 'JPEH', 'JPEM', 'JPEU',
                    'JPGE', 'JPIH', 'JPIN', 'JPN', 'LOWC', 'PAF', 'PID', 'PIE',
                    'PIN', 'PIZ', 'QCAN', 'QDEU', 'QEFA', 'QEMM', 'QGBR',
                    'QJPN', 'SCHC', 'SCHE', 'SCHF', 'WDIV'
                    ]

        self.tickers = domestic + internat

    def get(self):

        return self.tickers
