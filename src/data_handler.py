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

    def addFilterByCountry(self, listOfCountries):
        modified = self.df.loc[:, listOfCountries].dropna(how='all')
        self.df = modified
        return self
            
    def getVariance(self, country):
        return statistics.variance(self.df[country])

    def addAverage(self):
        average = []
        for year in self.df.index:   
            average.append(self.calculateAverageFromSeries(self.df.loc[year,:]))
        self.df.insert(0, 'Average', average)
        return self

    def addVarFromAverage(self, country):
        """
        Adds a variability column. Requires an Average column. 
        """
        average = self.df.loc[:,'Average']
        countryValues = self.df.loc[:,country]
        self.df.insert(0, "{} variability".format(country), (countryValues - average)/average)
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
        """
        Loading and normalizing csv file such as debt-to-gdp.csv
        """
        df = pd.read_csv(dataProperties.source , sep=dataProperties.separator)
        df.set_index(dataProperties.indexName, inplace=True)
        df.drop(df.iloc[:, 0:dataProperties.dataOffset], axis=1, inplace=True)
        if dataProperties.transpose: df = df.transpose()
        df.name = dataProperties.name
        self.df = df        

class CSVSequenceAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.CSVSequence):
        """
        Loading and normalizing csv file sucha as trade-unionism.csv
        """
        df = pd.read_csv(dataProperties.source , sep=dataProperties.separator)
        df.name = dataProperties.name
        countries = np.unique(list(df.loc[:, dataProperties.countryColumnName]))
        years = np.unique(list(df.loc[:,dataProperties.dateColumnName]))
        data = []
        for year in years:
            element = []
            for country in countries:
                try:
                    a = float(df[(df[dataProperties.dateColumnName] == year) & (df[dataProperties.countryColumnName] == country)][dataProperties.valueColumnName])
                except:
                    a = float('nan')
                element.append(a)
            data.append(element)
        self.df = pd.DataFrame(data, years, countries)
        print(self.df)
                



class TSVAnalyser(DataAnalyser):

    def __init__(self, dataProperties: data_types.TSV):
        """
        Loading and normalizing tsv file such as debt-to-gdp.csv
        """
        self.source = dataProperties.source
        
        df = pd.read_table(self.source)
        df.set_index(dataProperties.indexName, inplace=True)
        df.name = dataProperties.name
        if dataProperties.transpose: 
            self.df = df.transpose()
        else: 
            self.df = df

    



