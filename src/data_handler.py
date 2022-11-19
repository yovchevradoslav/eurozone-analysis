import pandas as pd
import statistics 
import os
import data_types

class CSVAnalyser:

    def __init__(self, dataProperties: data_types.CSV):
        self.dataProperties = dataProperties
        df = pd.read_csv(dataProperties.dataLocation , sep=dataProperties.separator)
        df.set_index(dataProperties.indexName, inplace=True)
        self.data = df

    def getRawData(self, column):
        
        df.iloc[[2, 3, 4]]

        return self.data.loc[2]    