import data_handler
from data_types import CSV
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def getDataSource(filename):
    return "{}/../data/{}.csv".format(ROOT_DIR, filename)


GDPGrowthDataDescriptor = CSV(getDataSource("gdp-growth"), "Country Name", 3, ",")
GDPGrowthAnalyser = data_handler.CSVAnalyser(GDPGrowthDataDescriptor)


result = GDPGrowthAnalyser.getRawDataByRowId("Bulgaria")