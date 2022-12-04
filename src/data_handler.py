import pandas as pd
import statistics 
import os
import data_types
import numpy as np
import math
import error

class DataAnalyser:

    def refine_set(self):
        '''
        Turn all elements in the dataset in float values. 
        In case of non numeric value such as ":", the value is replaced by NaN
        '''
        self.df = self.df.applymap(self.transform_dataset)
        self.df.apply(pd.to_numeric)
        self.df.index = self.df.index.astype("unicode")
        return self


    def get_dataframe(self):
        return self.df

    @error.throws_error(error.InvalidFilter)
    def add_filter_by_country(self, list_of_countries):
        modified = self.df.loc[:, list_of_countries].dropna(how='all')
        self.df = modified
        return self

    def add_average(self):
        average = []
        for year in self.df.index:   
            average.append(self.calculate_average_from_series(self.df.loc[year,:]))
        self.df.insert(0, 'Average', average)
        return self

    def add_var_from_average(self, country):
        """
        Adds a column: (CountryValue - Average)/Average
        """
        average = self.df.loc[:,'Average']
        countryValues = self.df.loc[:,country]
        self.df.insert(0, "{} var to average".format(country), (countryValues - average)/average)
        return self

    def add_variability(self, country):
        """
        Inserts a column: (CountryValue - Average)
        """
        average = self.df.loc[:,'Average']
        countryValues = self.df.loc[:,country]
        self.df.insert(0, "{} variability".format(country), (countryValues - average))
        return self

    def get_variability(self, country):
        """
        returns series of variability
        """
        average = self.df.loc[:,'Average']
        countryValues = self.df.loc[:,country]
        filteredDf = countryValues - average
        filteredDf.name = self.data_properties.name
        return filteredDf
    
    def get_var_to_average(self, country):
        """
        returns series of:
        (country_value - average)/average
        """
        average = self.df.loc[:,'Average']
        countryValues = self.df.loc[:,country]
        filteredDf = (countryValues - average)/average
        filteredDf.name = self.data_properties.name
        return filteredDf

    def transform_dataset(self, x):
        try:
            x = float(x)
            return x
        except:
            x = float('nan')
            return x
    
    def rename_columns(self, func):
        '''
        Renames columns in the dataset using a function from outside. 
        '''
        self.df.rename(func, inplace=True, axis=0)
        return self

    def calculate_average_from_series(self, series):
        '''
        Calculates averages ignoring NaN
        '''
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

    def __init__(self, data_properties: data_types.CSVTimeseries):
        """
        Loading and normalizing csv file such as debt-to-gdp.csv
        """
        self.data_properties = data_properties
        df = pd.read_csv(data_properties.source , sep=data_properties.separator)
        df.set_index(data_properties.indexName, inplace=True)
        df.drop(df.iloc[:, 0:data_properties.dataOffset], axis=1, inplace=True)
        if data_properties.transpose: df = df.transpose()
        self.df = df 
        self.df.name = data_properties.name       

class CSVSequenceAnalyser(DataAnalyser):

    def __init__(self, data_properties: data_types.CSVSequence):
        """
        Loading and normalizing csv file sucha as trade-unionism.csv
        """
        self.data_properties = data_properties
        df = pd.read_csv(data_properties.source , sep=data_properties.separator)
        countries = np.unique(list(df.loc[:, data_properties.countryColumnName]))
        years = np.unique(list(df.loc[:,data_properties.dateColumnName]))
        data = []
        for year in years:
            element = []
            for country in countries:
                try:
                    # print(df[(df[data_properties.dateColumnName] == year) & (df[data_properties.countryColumnName] == country)][data_properties.valueColumnName])
                    value = float(df[(df[data_properties.dateColumnName] == year) & (df[data_properties.countryColumnName] == country)][data_properties.valueColumnName])
                except:
                    value = float('nan')
                element.append(value)
            data.append(element)
        self.df = pd.DataFrame(data, years, countries)
        self.df.set_index(years, inplace=True)
        self.df.name = data_properties.name               

class TSVAnalyser(DataAnalyser):

    def __init__(self, data_properties: data_types.TSV):
        """
        Loading and normalizing tsv file such as debt-to-gdp.csv
        """
        self.data_properties = data_properties
        self.source = data_properties.source
        
        df = pd.read_table(self.source)
        df.set_index(data_properties.indexName, inplace=True)
        if data_properties.transpose: 
            self.df = df.transpose()
        else: 
            self.df = df
        self.df.name = data_properties.name

    



