import pandas as pd


class GrantsData:

    def __init__(self, path: str):
        self.df = pd.read_csv(path, compression = 'zip')
        #print(df)


if __name__ == '__main__':
    gd = GrantsData()
    
