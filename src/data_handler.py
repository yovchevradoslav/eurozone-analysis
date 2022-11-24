import pandas as pd
import statistics 
import os
import data_types
import numpy as np

class DataAnalyser:

    def getRawDataByRowId(self, rowId, transpose=True):
        if transpose:
            return self.df.loc[rowId, :].dropna(how='all').transpose()
        else:
            return self.df.loc[rowId, :].dropna(how='all')

    def getVariance(self):
        return statistics.variance(self.df)

    def getMean(self):
        return statistics.mean(self.df)


class CSVAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.CSV):

        self.dataProperties = dataProperties
        self.source = dataProperties.source
        self.indexName = dataProperties.indexName
        self.dataOffset = dataProperties.dataOffset
        self.separator = dataProperties.separator

        df = pd.read_csv(self.source , sep=self.separator)
        df.set_index(self.indexName, inplace=True)
        df.drop(df.iloc[:, 0:self.dataOffset], axis=1, inplace=True)
        self.df = df

class TSVAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.TSV):

        self.source = dataProperties.source
        self.indexName = dataProperties.indexName

        df = pd.read_table(self.source)
        df.set_index(self.indexName, inplace=True)
        self.df = df

    



