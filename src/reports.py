
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
        return: set of dataframes
        """
        pass
    
    @abstractmethod
    def publish(self, report_name):
        try:
            dataframes = self.generate_dataframes()
            shutil.rmtree(self.report_dir)
        except Exception as e:
            print('Dataframes failed for whatever reason')
            print(e.with_traceback)
        finally:
            os.mkdir(self.report_dir, 0o777)
            pd.concat(dataframes, axis=1).to_excel( self.report_dir + '/' + report_name + ".xlsx")

    @abstractmethod
    def modifyDate(self, x):
        return x.split("-")[0]

class SimpleVariablesReport(GenericReport):

    def generate_dataframes(self):

        gdp_growth = self.analyser.gdp_growth.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('GDP Growth')

        debt_to_gdp = self.analyser.debt_to_gdp.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Debt to GDP')

        unemployment = self.analyser.unemployment.refine_set().add_filter_by_country(self.settings['country']).rename_columns(self.modifyDate).get_dataframe('Unemployment')

        trade_union_density = self.analyser.trade_union_density.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Trade Union Density')

        government_spending = self.analyser.government_spending.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Government Spending')

        intra_extra_trade = self.analyser.intra_extra_trade.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Intra Extra Trade')

        deficit = self.analyser.deficit.refine_set().add_filter_by_country(self.settings['country']).get_dataframe('Deficit')

        return [debt_to_gdp, gdp_growth, unemployment, trade_union_density, government_spending, intra_extra_trade, deficit]



class VariabilityToAverageReport(GenericReport):

    def generate_dataframes(self):

        eurozone = ['Austria', 'Belgium', 'Germany', 'Italy', 'Ireland', 'Luxembourg', 'Netherlands', 'France',	'Finland',	'Greece', 'Spain', 'Portugal', 'Cyprus', 'Malta']

        gdp_growth = self.analyser.gdp_growth.refine_set().add_filter_by_country(eurozone).add_average().get_var_to_average('Portugal')
        print(gdp_growth)

        debt_to_gdp = self.analyser.debt_to_gdp.refine_set().add_filter_by_country(eurozone).add_average().get_var_to_average('Portugal')
        print(debt_to_gdp)

        unemployment = self.analyser.unemployment.refine_set().add_filter_by_country(eurozone).rename_columns(self.modifyDate).add_average().get_var_to_average('Portugal')
        print(unemployment)

        trade_union_density = self.analyser.trade_union_density.refine_set().add_average().get_var_to_average('Portugal')
        print(type(trade_union_density.index))

        government_spending = self.analyser.government_spending.refine_set().get_var_to_average('Slovakia')
        print(government_spending)

        intra_extra_trade = self.analyser.intra_extra_trade.refine_set().add_filter_by_country("Portugal").get_dataframe()
        print(intra_extra_trade)

        deficit = self.analyser.deficit.refine_set().add_filter_by_country("Portugal").get_dataframe()
        print(deficit)

        return [debt_to_gdp, gdp_growth]