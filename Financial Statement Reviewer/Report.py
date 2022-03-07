import pandas as pd
import numpy as np
class Report:
    def __init__(self, file_name, filters):
        self.file_name = file_name
        self.filters = filters

    def save_report(self, report):
        report_name = input("Please enter a name for the report: ")
        report.to_csv(f"Financial Statement Reviewer/Reports/{report_name}.csv")
        print(f"\nReport saved as {report_name}.csv")
        