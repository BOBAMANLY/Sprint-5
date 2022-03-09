import pandas as pd
import numpy as np
from os import system, name
from time import sleep
import csv

from UseFile import UseFile

class Report:
    def __init__(self, file_name, filters, use_filters, csv_column_info):
        self.file_name = file_name
        self.filters = filters
        self.use_filters = use_filters
        self.csv_column_info = csv_column_info

        self.specific_filter = ""
        self.saved_filters_bool = True

    def clear(self):
  
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def save_report(self, report):
        report_name = input("Please enter a name for the report: ")
        with open(f"Financial Statement Reviewer/Reports{report_name}.csv", "w", newline="") as save_file:
            writer = csv.writer(save_file)
            writer.writerows(report)

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
                        self.saved_filters_bool = True

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
                        self.saved_filters_bool = False
                        self.filter_report(csv_file)
                    else:
                        print("\nInvalid input. Please try again.")
                        loop = True
                        continue
                else:
                    print("\nInvalid input. Please try again.")
                    continue
        else:
            self.generic_report(csv_file)

        # Return the file
        return csv_file

    
    # Report types
    def generic_report(self, csv_file):
        expenditures = self.organize_expenditures(csv_file)
        income = self.organize_income(csv_file)

        # Add all the transactions into the report
        report = []
        report.append(("Expenditures"))
        for line in expenditures:
            report.append(line)
        report.append(("Income"))
        for line in income:
            report.append(line)

        # Save the report    
        self.save_report(report)

    def saved_filter_report(self, csv_file):
        pass

    def filter_report(self, csv_file):
        loop = True
        while loop == True:
            date_filter_q = input("Would you like to filter by date? (yes/no): ").lower()
            if date_filter_q == "yes" or date_filter_q == "no":
                loop = False
                if date_filter_q == "yes":
                    filtered_dates = self.filter_date(csv_file)
                elif date_filter_q == "no":
                    continue
            else:
                print("\nInvalid input. Please try again.")
                loop = True
                continue

        loop = True
        while loop == True:
            amount_filter_q = input("Would you like to filter by amount? (yes/no): ").lower()
            if amount_filter_q == "yes" or amount_filter_q == "no":
                loop = False
                if amount_filter_q == "yes":
                    filtered_amounts = self.filter_amount(csv_file)
                elif amount_filter_q == "no":
                    continue
            else:
                print("\nInvalid input. Please try again.")
                loop = True
                continue

        expenditures = self.organize_expenditures(csv_file)
        income = self.organize_income(csv_file)

        # Add all the transactions into the report
        report = []
        if date_filter_q == "yes":
            report.append("Dates filtered")
            for transaction in filtered_dates:
                report.append(transaction)
        if amount_filter_q == "yes":
            report.append("Amounts filtered")
            for transaction in filtered_amounts:
                report.append(transaction)
        report.append(("Expenditures"))
        for line in expenditures:
            report.append(line)
        report.append(("Income"))
        for line in income:
            report.append(line)

        # Save the report    
        self.save_report(report)

    # Filters and reporting
    """
    csv_column_info = [{date},{description},{amount},{negative_numbers_bool}]
    """
    def filter_date(self, csv_file):
        filtered_dates = []
        if self.saved_filters_bool == True:
            date_to_filter = self.specific_filter["date"]
            for transaction in csv_file:
                if transaction[self.csv_column_info[0]] == date_to_filter:
                    filtered_dates.append(transaction)
            return filtered_dates

        elif self.saved_filters_bool == False:
            print("Input the date in the same format as your .csv file.")
            date_to_filter = input("Please enter the date you would like to filter by: ")
            for transaction in csv_file:
                if transaction[self.csv_column_info[0]] == date_to_filter:
                    filtered_dates.append(transaction)
            return filtered_dates

        else:
            print("\nInvalid input. Please restart and try again.")
            sleep(2)
            exit()

    def filter_amount(self, csv_file):
        filtered_amounts = []
        if self.saved_filters_bool == True:
            amount_to_filter = self.specific_filter["amount"]
            for transaction in csv_file:
                if "$" in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("$", "")
                if "," in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(",", "")
                if "(" in transaction[self.csv_column_info[2]] and ")" in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("(", "-")
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(")", "")
                if float(transaction[self.csv_column_info[2]]) == float(amount_to_filter):
                    filtered_amounts.append(transaction)
            return filtered_amounts
            
        elif self.saved_filters_bool == False:
            print("Input the amount in the same format as your .csv file.")
            amount_to_filter = float(input("Please enter the amount you would like to filter by: "))
            for transaction in csv_file:
                if "$" in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("$", "")
                if "," in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(",", "")
                if "(" in transaction[self.csv_column_info[2]] and ")" in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("(", "-")
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(")", "")
                if float(transaction[self.csv_column_info[2]]) == float(amount_to_filter):
                    filtered_amounts.append(transaction)
            return filtered_amounts

        else:
            print("\nInvalid input. Please restart and try again.")
            sleep(2)
            exit()

    def organize_expenditures(self, csv_file):
        expenditures = []
        for transaction in csv_file:
            if "$" in transaction[self.csv_column_info[2]]:
                transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("$", "")
            if "," in transaction[self.csv_column_info[2]]:
                transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(",", "")
            if "(" in transaction[self.csv_column_info[2]] and ")" in transaction[self.csv_column_info[2]]:
                transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("(", "-")
                transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(")", "")
            if float(transaction[self.csv_column_info[2]]) < 0.0:
                expenditures.append(transaction)
        return expenditures

    def organize_income(self, csv_file):
        income = []
        for transaction in csv_file:
            if "$" in transaction[self.csv_column_info[2]]:
                transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("$", "")
            if "," in transaction[self.csv_column_info[2]]:
                transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(",", "")
            if "(" in transaction[self.csv_column_info[2]] and ")" in transaction[self.csv_column_info[2]]:
                transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("(", "-")
                transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(")", "")
            if float(transaction[self.csv_column_info[2]]) > 0.0:
                income.append(transaction)
        return income