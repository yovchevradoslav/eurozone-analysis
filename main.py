import os
import shutil
import src.reports as reports
import src.analysers as analysers


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = "{}/data".format(ROOT_DIR)
REPORTS_PATH = "{}/reports".format(ROOT_DIR)


try:
    shutil.rmtree(REPORTS_PATH)
except Exception as e:
    print("Error deleting the dir")
    print(e.with_traceback)
finally:
    os.mkdir(REPORTS_PATH)
    analyser = analysers.GenericAnalyser(DATA_PATH)
    
    simple_report_portugal = reports.SimpleVariablesReport(analyser, REPORTS_PATH, {"country": "Portugal"})
    simple_report_portugal.publish('simple_report_portugal')

    variability_report_portugal = reports.VariabilityToAverageReport(analyser, REPORTS_PATH, {"country": "Portugal"})
    variability_report_portugal.publish('variability_report_portugal')