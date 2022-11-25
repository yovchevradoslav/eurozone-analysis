import pandas as pd
import statistics 
import os
import data_types
import numpy as np

class DataAnalyser:


    def getDataframe(self):
        return self.df

    def addFilterByCountry(self, rowIds, transpose=True):
        if transpose:
            modified = self.df.loc[rowIds, :].dropna(how='all').transpose()
            self.df = modified
        else:
            self.df.replace(self.df.loc[rowIds, :].dropna(how='all'))
        return self
            
    def getVariance(self, rowId):
        return statistics.variance(self.df[rowId])

    def addAverage(self, rowIds):
        print(self.df.loc[:, rowIds])
        return self

    # def addVariability(self, rowId):
    #     modified = self.df.loc[rowId, :].dropna(how='all').transpose()
    #     self.df.update(modified) 
    #     return (self.df['Average'] - self.df[rowId])/self.df['Average']
    
    def renameColumns(self, func):
        self.df.rename(func, inplace=True, axis=0)
        return self
        

class CSVTimeseriesAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.CSVTimeseries):

        self.dataProperties = dataProperties
        self.source = dataProperties.source
        self.indexName = dataProperties.indexName
        self.dataOffset = dataProperties.dataOffset
        self.separator = dataProperties.separator

        df = pd.read_csv(self.source , sep=self.separator)
        df.set_index(self.indexName, inplace=True)
        df.drop(df.iloc[:, 0:self.dataOffset], axis=1, inplace=True)
        df.name = dataProperties.name
        self.df = df

class CSVSequenceAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.CSVSequence):

        self.source = dataProperties.source
        self.indexName = dataProperties.indexName
        self.dateColumnName = dataProperties.dateColumnName
        self.valueColumntName = dataProperties.valueColumntName
        self.separator = dataProperties.separator

        df = pd.read_csv(self.source , sep=self.separator)
        df.set_index(self.indexName, inplace=True)
        df.name = dataProperties.name
        refinedDf = df[[self.dateColumnName, self.valueColumntName]]
        self.df = refinedDf


class TSVAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.TSV):

        self.source = dataProperties.source
        
        df = pd.read_table(self.source)
        df.set_index(dataProperties.indexName, inplace=True)
        df.name = dataProperties.name
        self.df = df

    



