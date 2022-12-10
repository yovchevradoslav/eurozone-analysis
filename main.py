import os
import src.reports as reports
import src.analysers as analysers


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = "{}/data".format(ROOT_DIR)
REPORTS_PATH = "{}/reports".format(ROOT_DIR)

analyser = analysers.GenericAnalyser(DATA_PATH)
simple_report_portugal = reports.SimpleVariablesReport(analyser, REPORTS_PATH, {"country": "Portugal"})
simple_report_portugal.publish('simple_report_portugal')

# variability_report = reports.SimpleVariablesReport(analyser, REPORTS_PATH, {"country": "Portugal"})
# simple_report.publish('simple_report_portugal')