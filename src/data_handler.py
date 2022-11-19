import pandas as pd
import statistics 
import os
import data_types
import numpy as np

class CSVAnalyser:

    def __init__(self, dataProperties: data_types.CSV):

        self.dataProperties = dataProperties
        self.source = dataProperties.source
        self.indexName = dataProperties.indexName
        self.dataOffset = dataProperties.dataOffset
        self.separator = dataProperties.separator

        dataframe = pd.read_csv(self.source , sep=self.separator)
        dataframe.set_index(self.indexName, inplace=True)
        dataframe.drop(dataframe.iloc[:, 0:self.dataOffset], axis=1, inplace=True)
        self.dataframe = dataframe

    def getRawDataByRowId(self, rowId):
    
        return self.dataframe.loc[rowId, :]

    def getVarianceByRowId(self, rowId):

        return statistics.variance(self.dataframe.loc[rowId, :])