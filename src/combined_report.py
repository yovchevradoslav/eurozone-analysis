import src.reports as reports
import src.analysers as analysers
import src.utils as utils

class CombinedReport():

    def __init__(self, DATA_PATH: str, REPORTS_PATH: str, country: str):
        self.DATA_PATH = DATA_PATH
        self.REPORTS_PATH = REPORTS_PATH
        self.country = country

    def publish(self):
            simple_report_analyser = analysers.GenericAnalyser(self.DATA_PATH)
            simple_report = reports.SimpleVariablesReport(simple_report_analyser, self.REPORTS_PATH, {"country": self.country})

            variability_report_analyser = analysers.GenericAnalyser(self.DATA_PATH)
            variability_report = reports.VariabilityToAverageReport(variability_report_analyser, self.REPORTS_PATH, {"country": self.country})

            ratio_report_analyser = analysers.GenericAnalyser(self.DATA_PATH)
            ratio_report = reports.RatioToAverageReport(ratio_report_analyser, self.REPORTS_PATH, {"country": self.country})

            change_rate_report_analyser = analysers.GenericAnalyser(self.DATA_PATH)
            change_rate_report = reports.ChangeRateReport(change_rate_report_analyser, self.REPORTS_PATH, {"country": self.country})
    
            utils.merge_reports([simple_report, variability_report, ratio_report, change_rate_report], self.REPORTS_PATH, self.country)
