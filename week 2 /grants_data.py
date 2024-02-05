from re import split
import pandas as pd


class GrantsData:

    def __init__(self, path: str):
        self.df = pd.read_csv(path, compression= 'zip')

    def read(self) -> pd.DataFrame:
        """Returns a cleaned dataframe"""
        df = self._select_columns(self.df)
        # data can have NaNs
        # different types (reasonable)
        # different types (unreasonable)

        print(self.df)

    @staticmethod  #means it doesn't use anything from self
    def _select_columns(df: pd.DataFrame) -> pd.DataFrame:
        """ Rename and select columns
        NOTE: underscore methods are "private methods" meaning we should on call them from WITHIN the class

        Args:
            df (pd.DataFrame): dataframe

        Returns:
            pd.DataFrame: the subset, clean name dataframe
        """
        mapper= {
            'APPLICATION_ID':'application_id',
            'BUDGET_START': 'budget_start', 
            'ACTIVITY' : 'grant_type',
            'TOTAL_COST' : 'total_cost',
            'PI_NAMEs' : 'pi_names',
            'PI_IDS' : 'pi_ids', 
            "ORG_NAME" : 'organization',
            'ORG_CITY' :'city', 
            "ORG_STATE" : 'state',
            'ORG_COUNTRY' : 'country'
        }
        return df.rename(columns=mapper)[mapper.values()]

@staticmethod
def _clean(df: pd.DataFrame) -> pd.DataFrame:
    """Remove Nans and other cleaning functions

    Args:
        df (pd.DataFrame): dataframe with subset column names 

    Returns:
        pd.DataFrame: DF free of NaNs
    """
    df['pi_names'] = df['pi_names'].str.split(';')
    df = df.explode('pi_names')
    df['is_contact'] = df['pi_names'].str.lower().str.contains('(contact)')
    df['pi_names'] = df['pi_names'].str.replace('(contact)', '') 
    df[['both_names']] = df['pi_names'].apply(lambda x: x.split(',')[:2])
    df[['last_name', 'forename']] = pd.DataFrame(df['both_names'].to_list(), index = df.index)
    print(df)

#  HW TO IMPUTE THE DATES 

def read_grants_year(year: int | str) -> pd.DataFrame:
    """Reads in Grants Data for a year and return as clean dataframe.

    Args:
        year (int | str): year to read

    Returns:
       pd.DataFrame: clean data frame of grants data 
     """
    # We know the filename is: RePORTER_PRJ_C_FY2022.zip
    path = "/Users/alexistroy/Downloads/RePORTER_PRJ_C_FY2022.zip"
    gd = GrantsData(path.format(year=year))
    return gd.read()

if __name__ == '__main__':
    import numpy as np 

    read_grants_year(2022)
    #gd = GrantsData()