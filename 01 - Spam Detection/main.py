# Path: TextClassification_Using_ML\main.py
import pandas as pd
from Config.config import CFG
from Data.dataloader import dataloader
from Preprocessing.data_preprocessing import preprocess_data
def main():
    """ main function """
    # load the data
    data = dataloader()
    # show the first 5 rows of the data
    print (data.head())
    # lets first print to verify the whtat is the preprocessed column and it is correct or not
    print(data["CONTENT"].head())
    # call the preprocessing function with the data and necessary parameters as input and store the preprocessed data in a new column in the dataframe  
    data["preprocessed_data"] = data[CFG["data_preprocessing"]["Column"]].apply(lambda x: preprocess_data(x, CFG["data_preprocessing"]["preprocessing_steps"]))
    print (data.head())



if __name__ == "__main__":
    main()
