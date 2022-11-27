import pandas as pd
import statistics 
import os
import data_types
import numpy as np
import math

class DataAnalyser:

    def refineSet(self):
        self.df = self.df.applymap(self.transformDataset)
        self.df.apply(pd.to_numeric) 
        return self

    def getDataframe(self):
        return self.df

    def addFilterByCountry(self, rowIds):
        modified = self.df.loc[:, rowIds].dropna(how='all')
        self.df = modified
        return self
            
    def getVariance(self, rowId):
        return statistics.variance(self.df[rowId])

    def addAverage(self, rowIds):
        average = []
        for year in self.df.index:   
            average.append(self.calculateAverageFromSeries(self.df.loc[year,:]))
        self.df.insert(0, 'Average', average)
        return self

    def transformDataset(self, x):
        try:
            x = float(x)
            return x
        except:
            x = float('nan')
            return x
    
    def renameColumns(self, func):
        self.df.rename(func, inplace=True, axis=0)
        return self

    def calculateAverageFromSeries(self, series):
        sum = 0
        n = 0 
        for item in series:
            if not math.isnan(item):
                sum += item
                n += 1
        if n > 0: 
            return sum/n
        else: 
            return float('nan')


class CSVTimeseriesAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.CSVTimeseries):

        df = pd.read_csv(dataProperties.source , sep=dataProperties.separator)
        df.set_index(dataProperties.indexName, inplace=True)
        df.drop(df.iloc[:, 0:dataProperties.dataOffset], axis=1, inplace=True)
        if dataProperties.transpose: df = df.transpose()
        df.name = dataProperties.name
        self.df = df        

class CSVSequenceAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.CSVSequence):

        df = pd.read_csv(dataProperties.source , sep=dataProperties.separator)
        df.name = dataProperties.name
        df = df.loc[:,:]
        df.set_index(dataProperties.indexName, inplace=True)        
        newIndex = list(df.index.unique())
        newColumns = np.unique(list(df.loc[:,'Time']))
        print(newIndex)
        print(newColumns)
        data = []
        for country in newIndex:
            elem = []
            # elem.append(country)
            elem += list(df.loc[country, "Value"])
            data.append(elem)
        
        print(data)
        newDf = pd.DataFrame(data, newIndex, newColumns)
        self.df = newDf.transpose()


class TSVAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.TSV):

        self.source = dataProperties.source
        
        df = pd.read_table(self.source)
        df.set_index(dataProperties.indexName, inplace=True)
        df.name = dataProperties.name
        if dataProperties.transpose: 
            self.df = df.transpose()
        else: 
            self.df = df

    



