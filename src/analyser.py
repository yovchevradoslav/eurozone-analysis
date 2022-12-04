import sys
import traceback
import data_handler
import data_types
import os
import pandas as pd


class Analyser: 
    def __init__(self, data_path):
        
        GDPGrowthDescriptor = data_types.CSVTimeseries("GDP Growth", "{}/gdp-growth.csv".format(data_path), "Country Name", 3, ",", True)
        DebtToGDPDescriptor = data_types.CSVTimeseries("Debt To GDP", "{}/debt-to-gdp.csv".format(data_path), "Country Name", 3, ",", True)
        UnemploymentDescriptor = data_types.TSV("Unemployment", "{}/unemployment.tsv".format(data_path), "Country Name", True)
        TradeUnionDensityDescriptor = data_types.CSVSequence("Trade Union Density", "{}/trade-unionism.csv".format(data_path), "Country", "Time", "Value", ",", True)
        GovernmentSpendingDescriptor = data_types.TSV("Government Spending", "{}/gov-expenditure.tsv".format(data_path), "Country", True)
        IntraExtraTrade = data_types.CSVTimeseries("Intra/Extra EU Trade", "{}/export-intra-by-extra.csv".format(data_path), "Country", 0, ";", True)
        DeficitDescriptor = data_types.TSV("Deficit", "{}/deficit.tsv".format(data_path), "Country", True)

        self.gdp_growth = data_handler.CSVTimeseriesAnalyser(GDPGrowthDescriptor)
        self.debt_to_gdp = data_handler.CSVTimeseriesAnalyser(DebtToGDPDescriptor)
        self.unemployment = data_handler.TSVAnalyser(UnemploymentDescriptor)
        self.trade_union_density = data_handler.CSVSequenceAnalyser(TradeUnionDensityDescriptor)
        self.government_spending = data_handler.TSVAnalyser(GovernmentSpendingDescriptor)
        self.intra_extra_trade = data_handler.CSVTimeseriesAnalyser(IntraExtraTrade)
        self.deficit = data_handler.TSVAnalyser(DeficitDescriptor)

    def modifyDate(x):
        return x.split("-")[0]







# gdp_growth = gdp_growth_analyser.refine_set().add_filter_by_country('adsad').add_average().get_var_to_average('adsad')
# print(gdp_growth)

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


#################
# try:
#     gdp_growth = gdp_growth_analyser.refine_set().add_filter_by_country('adsad').add_average().get_var_to_average('adsad')
#     print(gdp_growth)
# except Exception as e:
#     if(e.message): print(e.message)
#     traceback.print_exc()