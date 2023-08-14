""" dataloader file """
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

from configs.config import CFG

class Dataloader:
    """ Data loader class """

    def load_data()->pd.DataFrame:
        """ load data """
        data_yt01 = pd.read_csv(CFG['data']['path_yt01'])
        data_yt02 = pd.read_csv(CFG['data']['path_yt02'])
        data_yt03 = pd.read_csv(CFG['data']['path_yt03'])
        data_yt04 = pd.read_csv(CFG['data']['path_yt04'])
        data_yt05 = pd.read_csv(CFG['data']['path_yt05'])
        # merge all these dataframes into one dataframe 
        data = pd.concat([data_yt01, data_yt02, data_yt03, data_yt04, data_yt05])
        # shuffle the data 
        # data = data.sample(frac=1).reset_index(drop=True) 
        # return all the datasets and the merged dataset 
        # show print all the datasets readed 
        return data, data_yt01, data_yt02, data_yt03, data_yt04, data_yt05