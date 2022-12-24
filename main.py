import os
import shutil
import src.reports as reports
import src.analysers as analysers
import src.utils as utils


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

    simple_report_analyser_portugal = analysers.GenericAnalyser(DATA_PATH)
    simple_report_portugal = reports.SimpleVariablesReport(simple_report_analyser_portugal, REPORTS_PATH, {"country": "Portugal"})
    # simple_report_portugal.publish('simple_report_portugal')

    variability_report_analyser_portugal = analysers.GenericAnalyser(DATA_PATH)
    variability_report_portugal = reports.VariabilityToAverageReport(variability_report_analyser_portugal, REPORTS_PATH, {"country": "Portugal"})
    # variability_report_portugal.publish('variability_report_portugal')

    ratio_report_analyser_portugal = analysers.GenericAnalyser(DATA_PATH)
    ratio_report_portugal = reports.RatioToAverageReport(ratio_report_analyser_portugal, REPORTS_PATH, {"country": "Portugal"})
    # ratio_report_portugal.publish('ratio_report_portugal')

    utils.merge_reports([simple_report_portugal, variability_report_portugal, ratio_report_portugal], REPORTS_PATH, 'Portugal')

    simple_report_analyser_germany = analysers.GenericAnalyser(DATA_PATH)
    simple_report_germany = reports.SimpleVariablesReport(simple_report_analyser_germany, REPORTS_PATH, {"country": "Germany"})
    # simple_report_germany.publish('simple_report_germany')

    variability_report_analyser_germany = analysers.GenericAnalyser(DATA_PATH)
    variability_report_germany = reports.VariabilityToAverageReport(variability_report_analyser_germany, REPORTS_PATH, {"country": "Germany"})
    # variability_report_germany.publish('variability_report_germany')

    ratio_report_analyser_germany = analysers.GenericAnalyser(DATA_PATH)
    ratio_report_germany = reports.RatioToAverageReport(ratio_report_analyser_germany, REPORTS_PATH, {"country": "Germany"})
    # ratio_report_germany.publish('ratio_report_germany')

    change_rate_report_analyser_germany = analysers.GenericAnalyser(DATA_PATH)
    change_rate_report_germany = reports.ChangeRateReport(change_rate_report_analyser_germany, REPORTS_PATH, {"country": "Germany"})
    # change_rate_report_germany.publish('change_rate_report_germany')
    
    utils.merge_reports([simple_report_germany, variability_report_germany, ratio_report_germany, change_rate_report_germany], REPORTS_PATH, 'Germany')

    simple_report_analyser_italy = analysers.GenericAnalyser(DATA_PATH)
    simple_report_italy = reports.SimpleVariablesReport(simple_report_analyser_italy, REPORTS_PATH, {"country": "Italy"})
    # simple_report_germany.publish('simple_report_germany')

    variability_report_analyser_italy = analysers.GenericAnalyser(DATA_PATH)
    variability_report_italy = reports.VariabilityToAverageReport(variability_report_analyser_italy, REPORTS_PATH, {"country": "Italy"})
    # variability_report_germany.publish('variability_report_germany')

    ratio_report_analyser_italy = analysers.GenericAnalyser(DATA_PATH)
    ratio_report_italy = reports.RatioToAverageReport(ratio_report_analyser_italy, REPORTS_PATH, {"country": "Italy"})
    # ratio_report_germany.publish('ratio_report_germany')

    change_rate_report_analyser_italy = analysers.GenericAnalyser(DATA_PATH)
    change_rate_report_italy = reports.ChangeRateReport(change_rate_report_analyser_italy, REPORTS_PATH, {"country": "Italy"})
    # change_rate_report_germany.publish('change_rate_report_germany')
    
    utils.merge_reports([simple_report_italy, variability_report_italy, ratio_report_italy, change_rate_report_italy], REPORTS_PATH, 'Italy')
