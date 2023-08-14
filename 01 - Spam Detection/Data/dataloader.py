import pandas as pd
from Config.config import CFG


def dataloader():
    """ load the data from the config file path """
    data_yt01 = pd.read_csv(CFG["data"]["data_dir"] + "/Youtube01-Psy.csv")
    data_yt02 = pd.read_csv(CFG["data"]["data_dir"] + "/Youtube02-KatyPerry.csv")
    data_yt03 = pd.read_csv(CFG["data"]["data_dir"] + "/Youtube03-LMFAO.csv")
    data_yt04 = pd.read_csv(CFG["data"]["data_dir"] + "/Youtube04-Eminem.csv")
    data_yt05 = pd.read_csv(CFG["data"]["data_dir"] + "/Youtube05-Shakira.csv")
    # merge all the data into one dataframe 
    data = pd.concat([data_yt01, data_yt02, data_yt03, data_yt04, data_yt05], axis=0)
    # shuffle the data
    data = data.sample(frac=1).reset_index(drop=True)
    # return the data
    return data
