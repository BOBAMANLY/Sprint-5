import pandas as pd
import numpy as np
class Report:
    def __init__(self, file_name, filters, use_filters):
        self.file_name = file_name
        self.filters = filters
        self.use_filters = use_filters

    def save_report(self, report):
        report_name = input("Please enter a name for the report: ")
        report.to_csv(f"Financial Statement Reviewer/Reports/{report_name}.csv")
        print(f"\nReport saved as {report_name}.csv")

    def organize_expenditures(self):
        pass

    def organize_income(self):
        pass

    def create_report(self):
        # Read the file
        csv_file = pd.read_csv(self.file_name)

        # Filter the file
        if self.use_filters == "yes":
            pass

        else:
            pass

        # Return the file
        return csv_file

        