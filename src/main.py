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

GDPGrowthDescriptor = data_types.CSVTimeseries("GDP Growth", getDataSource("gdp-growth.csv"), "Country Name", 3, ",", True)
DebtToGDPDescriptor = data_types.CSVTimeseries("Debt To GDP", getDataSource("debt-to-gdp.csv"), "Country Name", 3, ",", True)
UnemploymentDescriptor = data_types.TSV("Unemployment", getDataSource("unemployment.tsv"), "Country Name", True)
TradeUnionDensityDescriptor = data_types.CSVSequence("Trade Union Density", getDataSource("trade-unionism.csv"), "Country", "Time", "Value", ",", True)
GovernmentSpendingDescriptor = data_types.TSV("Government Spending", getDataSource("gov-expenditure.tsv"), "Country", True)
IntraExtraTrade = data_types.CSVTimeseries("Intra/Extra EU Trade", getDataSource("export-intra-by-extra.csv"), "Country", 0, ";", True)
DeficitDescriptor = data_types.TSV("Deficit", getDataSource("deficit.tsv"), "Country", True)




gdp_growth_analyser = data_handler.CSVTimeseriesAnalyser(GDPGrowthDescriptor)
# debt_to_gdp_analyser = data_handler.CSVTimeseriesAnalyser(DebtToGDPDescriptor)
# unemployment_analyser = data_handler.TSVAnalyser(UnemploymentDescriptor)
# TradeUnionDensityAnalyser = data_handler.CSVSequenceAnalyser(TradeUnionDensityDescriptor)
# government_spending = data_handler.TSVAnalyser(GovernmentSpendingDescriptor)
# intra_extra_trade = data_handler.CSVTimeseriesAnalyser(IntraExtraTrade)
# deficit = data_handler.TSVAnalyser(DeficitDescriptor)


gdp_growth = gdp_growth_analyser.refine_set().add_filter_by_country(eurozone).add_average().get_var_to_average('Portugal')
print(gdp_growth)

# debt_to_gdp = debt_to_gdp_analyser.refine_set().add_filter_by_country(eurozone).add_average().get_var_to_average('Portugal')
# print(type(debt_to_gdp.index))

# unemployment = unemployment_analyser.refine_set().add_filter_by_country(eurozone).rename_columns(modifyDate).add_average().get_var_to_average('Portugal')
# # print(unemployment)

# trade_union_density = TradeUnionDensityAnalyser.refine_set().add_average().get_var_to_average('Portugal')
# print(type(trade_union_density.index))

# trade_union_density = TradeUnionDensityAnalyser.refine_set().add_average().get_var_to_average('Portugal')
# print(type(trade_union_density.index))

# government_spending = government_spending.refine_set().get_var_to_average('Slovakia')
# print(government_spending)

# intra_extra_trade = intra_extra_trade.refine_set().add_filter_by_country("Portugal").get_dataframe()
# print(intra_extra_trade)

# deficit = deficit.refine_set().add_filter_by_country("Portugal").get_dataframe()
# print(deficit)

# print(pd.concat([unemployment, trade_union_density, debt_to_gdp, gdp_growth], axis=1).to_excel('../outputs/report1.xlsx'))

