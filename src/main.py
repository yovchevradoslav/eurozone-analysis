import data_handler
import data_types
import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def getDataSource(filename):
    return "{}/../data/{}".format(ROOT_DIR, filename)

def modifyDate(x):
    return x.split("-")[0]


eurozone = ['Austria', 'Belgium', 'Germany', 'Italy', 'Ireland', 'Luxembourg', 'Netherlands', 'France',	'Finland',	'Greece', 'Spain', 'Portugal', 'Cyprus', 'Malta']
earlyEurozone = ['Austria']

GDPGrowthDescriptor = data_types.CSVTimeseries("GDP Growth", getDataSource("gdp-growth.csv"), "Country Name", 3, ",", True)
DebtToGDPDescriptor = data_types.CSVTimeseries("Debt To GDP", getDataSource("debt-to-gdp.csv"), "Country Name", 3, ",", True)
UnemploymentDescriptor = data_types.TSV("Unemployment", getDataSource("unemployment.tsv"), "Country Name", True)
TradeUnionDensityDescriptor = data_types.CSVSequence("Trade Union Density", getDataSource("trade-unionism.csv"), "Country", "Time", "Value", ",", True)



GDPGrowthAnalyser = data_handler.CSVTimeseriesAnalyser(GDPGrowthDescriptor)
DebtToGDPAnalyser = data_handler.CSVTimeseriesAnalyser(DebtToGDPDescriptor)
UnemploymentAnalyser = data_handler.TSVAnalyser(UnemploymentDescriptor)
TradeUnionDensityAnalyser = data_handler.CSVSequenceAnalyser(TradeUnionDensityDescriptor)


# GDPGrowth = GDPGrowthAnalyser.refineSet().addFilterByCountry(eurozone).addAverage().getDataframe()
# print(GDPGrowth)

# debtToGDP = DebtToGDPAnalyser.refineSet().addFilterByCountry(eurozone).addAverage().getDataframe()
# print(debtToGDP)

# unemployment = UnemploymentAnalyser.refineSet().addFilterByCountry(eurozone).renameColumns(modifyDate).addAverage(eurozone).getDataframe()
# print(unemployment)

tradeUnionDensity = TradeUnionDensityAnalyser.refineSet().addAverage().getDataframe()

axis = ["Bulgaria", "Italy", "Germany"]
columns = ["1960", "1961", "1962"]
newDf = pd.DataFrame([], axis, columns)
# print(newDf)

#print(pd.concat([unemployment, gdpGrowth, tradeUnionism], axis=1))

# 
# DebtToGDPAnalyser.getDataframe().to_excel("../outputs/gdp-growth.xlsx")
# UnemploymentAnalyser.getRawDataByRowId("Bulgaria").to_excel("unemployment.xlsx")
