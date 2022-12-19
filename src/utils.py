import pandas as pd

def merge_reports(reports: list, report_dir, report_name):
    dataframes = []
    for report in reports:
            dataframes.append(report.generate_dataframes())
    dataframes=[item for sublist in dataframes for item in sublist]
    
    print(len(dataframes))
    pd.concat(dataframes, axis=1).to_excel(report_dir + '/' + report_name + ".xlsx")
