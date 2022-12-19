
from abc import abstractmethod
import shutil
import pandas as pd
import os

class GenericReport():

    @abstractmethod
    def __init__(self, analyser, report_dir, settings: map):
        self.analyser = analyser
        self.report_dir = report_dir
        self.settings = settings

    @abstractmethod
    def generate_dataframes(self):
        """
        return: list of dataframes
        """
        pass
    
    @abstractmethod
    def publish(self, report_name):
        dataframes = self.generate_dataframes()
        pd.concat(dataframes, axis=1).to_excel( self.report_dir + '/' + report_name + ".xlsx")
    
    @abstractmethod
    def modifyDate(self, x):
        return x.split("-")[0]

class SimpleVariablesReport(GenericReport):

    def generate_dataframes(self):
        
        gdp_growth = self.analyser.gdp_growth.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('GDP Growth')

        trade_balance = self.analyser.trade_balance.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Trade Balance')

        unemployment = self.analyser.unemployment.refine_set().add_filter_by_country(self.settings['country']).rename_columns(self.modifyDate).get_dataframe('Unemployment')

        trade_union_density = self.analyser.trade_union_density.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Trade Union Density')

        government_spending = self.analyser.government_spending.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Government Spending')

        intra_extra_trade = self.analyser.intra_extra_trade.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Intra Extra Trade')

        deficit = self.analyser.deficit.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Deficit')

        inflation = self.analyser.inflation.refine_set().add_filter_by_country(self.settings['country']).rename_columns(self.modifyDate).get_dataframe('Inflation')

        return [gdp_growth, trade_balance, unemployment, trade_union_density, government_spending, intra_extra_trade, deficit, inflation]



class VariabilityToAverageReport(GenericReport):

    def generate_dataframes(self):

        eurozone = ['Austria', 'Belgium', 'Germany', 'Italy', 'Ireland', 'Luxembourg', 'Netherlands', 'France',	'Finland',	'Greece', 'Spain', 'Portugal']

        gdp_growth = self.analyser.gdp_growth.refine_set().add_filter_by_country(eurozone).add_average().get_variability(self.settings['country'])

        trade_balance = self.analyser.trade_balance.refine_set().add_filter_by_country(eurozone).add_average().get_variability(self.settings['country'])
        
        unemployment = self.analyser.unemployment.refine_set().add_filter_by_country(eurozone).rename_columns(self.modifyDate).add_average().get_variability(self.settings['country'])

        trade_union_density = self.analyser.trade_union_density.refine_set().add_filter_by_country(eurozone).add_average().get_variability(self.settings['country'])

        government_spending = self.analyser.government_spending.refine_set().add_filter_by_country(eurozone).add_average().get_variability(self.settings['country'])

        intra_extra_trade = self.analyser.intra_extra_trade.refine_set().add_filter_by_country(eurozone).add_average().get_variability(self.settings['country'], percent=True)

        deficit = self.analyser.deficit.refine_set().add_filter_by_country(eurozone).add_average().get_variability(self.settings['country'])

        inflation = self.analyser.inflation.refine_set().add_filter_by_country(eurozone).rename_columns(self.modifyDate).add_average().get_variability(self.settings['country'])

        return [gdp_growth, trade_balance, unemployment, trade_union_density, government_spending, intra_extra_trade, deficit, inflation]


class RatioToAverageReport(GenericReport):

    def generate_dataframes(self):

        eurozone = ['Austria', 'Belgium', 'Germany', 'Italy', 'Ireland', 'Luxembourg', 'Netherlands', 'France',	'Finland',	'Greece', 'Spain', 'Portugal']

        gdp_growth = self.analyser.gdp_growth.refine_set().add_filter_by_country(eurozone).add_average().get_ratio_to_average(self.settings['country'])

        unemployment = self.analyser.unemployment.refine_set().add_filter_by_country(eurozone).rename_columns(self.modifyDate).add_average().get_ratio_to_average(self.settings['country'])

        trade_union_density = self.analyser.trade_union_density.refine_set().add_filter_by_country(eurozone).add_average().get_ratio_to_average(self.settings['country'])

        government_spending = self.analyser.government_spending.refine_set().add_filter_by_country(eurozone).add_average().get_ratio_to_average(self.settings['country'])

        intra_extra_trade = self.analyser.intra_extra_trade.refine_set().add_filter_by_country(eurozone).add_average().get_ratio_to_average(self.settings['country'])

        deficit = self.analyser.deficit.refine_set().add_filter_by_country(eurozone).add_average().get_ratio_to_average(self.settings['country'])

        inflation = self.analyser.inflation.refine_set().add_filter_by_country(eurozone).rename_columns(self.modifyDate).add_average().get_ratio_to_average(self.settings['country'])

        return [gdp_growth, unemployment, trade_union_density, government_spending, intra_extra_trade, deficit, inflation]


class ChangeRateReport(GenericReport):

    def generate_dataframes(self):

        eurozone = ['Austria', 'Belgium', 'Germany', 'Italy', 'Ireland', 'Luxembourg', 'Netherlands', 'France',	'Finland',	'Greece', 'Spain', 'Portugal']

        gdp_growth = self.analyser.gdp_growth.refine_set().add_filter_by_country(eurozone).get_change_rate(self.settings['country'])

        trade_balance = self.analyser.trade_balance.refine_set().add_filter_by_country(eurozone).get_change_rate(self.settings['country'])

        unemployment = self.analyser.unemployment.refine_set().add_filter_by_country(eurozone).rename_columns(self.modifyDate).add_average().get_change_rate(self.settings['country'])

        trade_union_density = self.analyser.trade_union_density.refine_set().add_filter_by_country(eurozone).add_average().get_change_rate(self.settings['country'])

        government_spending = self.analyser.government_spending.refine_set().add_filter_by_country(eurozone).add_average().get_change_rate(self.settings['country'])

        intra_extra_trade = self.analyser.intra_extra_trade.refine_set().add_filter_by_country(eurozone).add_average().get_change_rate(self.settings['country'])

        deficit = self.analyser.deficit.refine_set().add_filter_by_country(eurozone).add_average().get_change_rate(self.settings['country'])

        inflation = self.analyser.inflation.refine_set().add_filter_by_country(eurozone).rename_columns(self.modifyDate).add_average().get_change_rate(self.settings['country'])

        return [gdp_growth, trade_balance, unemployment, trade_union_density, government_spending, intra_extra_trade, deficit, inflation]