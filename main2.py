import os
import shutil
import src.combined_report as report


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

    germany = report.CombinedReport(DATA_PATH, REPORTS_PATH, 'Germany')
    germany.publish()

    greece = report.CombinedReport(DATA_PATH, REPORTS_PATH, 'Greece')
    greece.publish()

    italy = report.CombinedReport(DATA_PATH, REPORTS_PATH, 'Italy')
    greece.publish()

