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
earlyEurozone = ['Luxembourg', 'Ireland']

GDPGrowthDescriptor = data_types.CSVTimeseries("GDP Growth", getDataSource("gdp-growth.csv"), "Country Name", 3, ",")
DebtToGDPDescriptor = data_types.CSVTimeseries("Debt To GDP", getDataSource("debt-to-gdp.csv"), "Country Name", 3, ",")
UnemploymentDescriptor = data_types.TSV("Unemployment", getDataSource("unemployment.tsv"), "Country Name")
TradeUnionismDescriptor = data_types.CSVSequence("Trade Union Density", getDataSource("trade-unionism.csv"), "Country", "Time", "Value", ",")



# GDPGrowthAnalyser = data_handler.CSVTimeseriesAnalyser(GDPGrowthDescriptor)
# DebtToGDPAnalyser = data_handler.CSVTimeseriesAnalyser(DebtToGDPDescriptor)
UnemploymentAnalyser = data_handler.TSVAnalyser(UnemploymentDescriptor)
#TradeUnionismAnalyser = data_handler.CSVSequenceAnalyser(TradeUnionismDescriptor)


# debtToGDP = UnemploymentAnalyser.addFilterByCountry(eurozone)
# gdpGrowth = GDPGrowthAnalyser.addFilterByCountry('Portugal')
#tradeUnionism = TradeUnionismAnalyser.addFilterByCountry(eurozone, transpose=True)


unemployment = UnemploymentAnalyser.addFilterByCountry(earlyEurozone, True).addAverage(earlyEurozone).renameColumns(modifyDate).getDataframe()
print(unemployment)



#print(pd.concat([unemployment, gdpGrowth, tradeUnionism], axis=1))

# GDPGrowthAnalyser.getRawDataByRowId(eurozone).to_excel("gdp-growth.xlsx")
# UnemploymentAnalyser.getRawDataByRowId("Bulgaria").to_excel("unemployment.xlsx")
