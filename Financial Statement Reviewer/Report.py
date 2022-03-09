import pandas as pd
import numpy as np
from os import system, name

from UseFile import UseFile

class Report:
    def __init__(self, file_name, filters, use_filters):
        self.file_name = file_name
        self.filters = filters
        self.use_filters = use_filters
        self.specific_filter = ""

    def clear(self):
  
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def save_report(self, report):
        # TODO: Edit saving process to with open()
        report_name = input("Please enter a name for the report: ")
        report.to_csv(f"Financial Statement Reviewer/Reports/{report_name}.csv")
        print(f"\nReport saved as {report_name}.csv")

    

    def create_report(self):
        # Read the file
        csv_file = UseFile().read_csv(self.file_name)

        # Filter the file
        if self.use_filters == "yes":
            loop = True
            while loop == True:
                saved = input("Would you like to use a saved filter? (yes/no): ").lower()
                if saved == "yes" or saved == "no":
                    loop = False
                    if saved == "yes":

                        # Display the filter options
                        count = 0
                        for saved_filter in self.filters["Saved Filters"][count]:
                            count += 1
                            print(f"{count}: {saved_filter}")

                        loop = True
                        while loop == True:
                            filter_choice = input("Please enter the number of the filter you would like to use: ")
                            if filter_choice.isdigit() and int(filter_choice) <= len(self.filters["Saved Filters"] and int(filter_choice) > 0):
                                loop = False
                                self.specific_filter = self.filters["Saved Filters"][int(filter_choice) - 1]
                                self.saved_filter_report(csv_file)
                            else:
                                print("\nInvalid input. Please try again.")
                                continue
                    elif saved == "no":
                        self.generic_report(csv_file)
                    else:
                        print("\nInvalid input. Please try again.")
                        loop = True
                        continue
                else:
                    print("\nInvalid input. Please try again.")
                    continue
        else:
            self.filter_report(csv_file)

        # Return the file
        return csv_file

    
    # Report types
    def generic_report(self, csv_file):
        pass

    def saved_filter_report(self, csv_file):
        pass

    def filter_report(self):
        pass

    # Filters and reporting
    def filter_amount(self, csv_file):
        pass

    def organize_expenditures(self, csv_file):
        pass

    def organize_income(self, csv_file):
        pass



        