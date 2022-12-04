import pandas as pd

class Report():
    def __init__(self, Analyser, data_dir, report_dir, report_file_name):
        self.analyser = Analyser(data_dir)
        self.report_file_name = report_file_name
        self.report_dir = report_dir

    def generate_dataframes(self):
        """
        return: set of dataframes
        """
        pass

    def publish(self):
        dataframes = self.generate_dataframes()
        pd.concat(dataframes, axis=1).to_excel( self.report_dir + '/' + self.report_file_name)