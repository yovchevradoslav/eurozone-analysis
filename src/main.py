import data_handler
import data_types
import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def getDataSource(filename):
    return "{}/../data/{}".format(ROOT_DIR, filename)

def transformDate(input):
    return input.split("-")[0]


eurozone = ['Austria', 'Belgium', 'Germany', 'Italy', 'Ireland', 'Luxembourg', 'Netherlands', 'France',	'Finland',	'Greece', 'Spain', 'Portugal', 'Cyprus', 'Malta']

GDPGrowthDescriptor = data_types.CSV(getDataSource("gdp-growth.csv"), "Country Name", 3, ",")
UnemploymentDescriptor = data_types.TSV(getDataSource("../data/unemployment.tsv"), "Country Name")


GDPGrowthAnalyser = data_handler.CSVAnalyser(GDPGrowthDescriptor)
UnemploymentAnalyser = data_handler.TSVAnalyser(UnemploymentDescriptor)
unemployment = UnemploymentAnalyser.getRawDataByRowId('Germany')
gdpGrowth = GDPGrowthAnalyser.getRawDataByRowId('Germany')



unemployment.rename(lambda x: x.split("-")[0], inplace=True)
unemployment.name = "Unemployment"
gdpGrowth.rename(lambda x: x.split("-")[0], inplace=True)
gdpGrowth.name = "GDP Growth"


print(pd.concat([unemployment, gdpGrowth], axis=1))

# GDPGrowthAnalyser.getRawDataByRowId(eurozone).to_excel("gdp-growth.xlsx")
# UnemploymentAnalyser.getRawDataByRowId("Bulgaria").to_excel("unemployment.xlsx")
