"""" main file for the project (Runner Code)"""
import pandas as pd
from configs.config import CFG
from dataloader.dataloader import Dataloader

def run():
    """ run function """
    print("Hello World")
    print(CFG['data']['path_yt01'])
    # data = Dataloader.load_data()
    # print(data.head())
    data_yt01 = pd.read_csv(CFG['data']['path_yt01'])
    data_yt02 = pd.read_csv(CFG['data']['path_yt02'])
    data_yt03 = pd.read_csv(CFG['data']['path_yt03'])
    data_yt04 = pd.read_csv(CFG['data']['path_yt04'])
    data_yt05 = pd.read_csv(CFG['data']['path_yt05'])
    # merge all these dataframes into one dataframe 
    # data = pd.concat([data_yt01, data_yt02, data_yt03, data_yt04, data_yt05])
    # shuffle the data 
    # data = data.sample(frac=1).reset_index(drop=True) 
    # return all the datasets and the merged dataset 
    # show print all the datasets readed 
    print(data_yt01, data_yt02, data_yt03, data_yt04, data_yt05)

if __name__ == "__main__":
    run()