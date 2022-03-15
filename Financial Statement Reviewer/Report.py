import pandas as pd
import numpy as np
from os import system, name
from time import sleep
import csv
import matplotlib.pyplot as plt

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
        with open(f"Financial Statement Reviewer/Reports/{report_name}.csv", "w", newline="") as save_file:
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
                        filter_names = [""]
                        for saved_filter in self.filters["Saved Filters"][count]:
                            count += 1
                            filter_names.append(saved_filter)
                            print(f"{count}: {saved_filter}")

                        # Get the filter to use
                        loop = True
                        while loop == True:
                            filter_choice = input("Please enter the number of the filter you would like to use: ")
                            if (filter_choice.isdigit() and int(filter_choice) <= len(self.filters["Saved Filters"][0]) and int(filter_choice) > 0):
                                loop = False
                                self.specific_filter = self.filters["Saved Filters"][0][filter_names[int(filter_choice)]]
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
        chart_data_expenditures = {}
        chart_data_income = {}
        main_header = ["Date", "Amount", "Description"]
        header = [f"{main_header[0]:10}{main_header[1]:10}{main_header[2]:30}"]
        report.append(header)
        report.append("")
        header = [["Expenditures"], ""]
        for item in header:
            report.append(item)
        for line in expenditures:
            report.append(line)
        # for line in expenditures:
        #     if line[self.csv_column_info[1]] not in chart_data_expenditures:
        #         chart_data_expenditures[line[self.csv_column_info[1]]] += float(line[self.csv_column_info[2]])
        # self.create_graph(chart_data_expenditures)         
        header = ["", ["Income"], ""]
        for item in header:
            report.append(item)
        for line in income:
            report.append(line)
        # for line in income:
        #     if line[self.csv_column_info[1]] not in chart_data_income:
        #         chart_data_income[line[self.csv_column_info[1]]] += float(line[self.csv_column_info[2]])
        # self.create_graph(chart_data_income)  

        # Save the report    
        self.save_report(report)

    def saved_filter_report(self, csv_file):
        #[{'date': '', 'amount': -886.95, 'description': '', 'category': '', 'classification': ''}]
        report = []
        main_header = ["Date", "Amount", "Description"]
        header = [f"{main_header[0]:10}{main_header[1]:10}{main_header[2]:30}"]
        report.append(header)
        report.append("")

        for type in self.specific_filter:
            if type["amount"] != "":
                filtered_amounts = self.filter_amount(csv_file)
                header = [f'Amount Filter: {type["amount"]}']
                report.append(header)
                for line in filtered_amounts:
                    report.append(line)
            if type["date"] != "":
                filtered_dates = self.filter_date(csv_file)
                if type["amount"] == "":
                    header = [f'Date Filter: {type["date"]}']
                else:
                    header = ["", [f'Date Filter: {type["date"]}'], ""]
                report.append(header)
                for line in filtered_dates:
                    report.append(line)
            if type["description"] != "":
                filtered_descriptions = self.filter_description(csv_file)
                if type["amount"] == "" or type["date"] == "":
                    header = [f'Description Filter: {type["description"]}']
                else:
                    header = ["", [f'Description Filter: {type["description"]}'], ""]
                report.append(header)
                for line in filtered_descriptions:
                    report.append(line)
            if type["amount"] == "" and type["date"] == "" and type["description"] == "":
                no_filters = True
            else: 
                no_filters = False
        
        expenditures = self.organize_expenditures(csv_file)
        income = self.organize_income(csv_file)

        # Add all the transactions into the report
        if no_filters == True:
            header = [["Expenditures"], ""]
        else:
            header = ["", ["Expenditures"], ""]
        for item in header:
            report.append(item)
        for line in expenditures:
            report.append(line)
        header = ["", ["Income"], ""]
        for item in header:
            report.append(item)
        for line in income:
            report.append(line)

        # Save the report    
        self.save_report(report)
        

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
        main_header = ["Date", "Amount", "Description"]
        header = [f"{main_header[0]:10}{main_header[1]:10}{main_header[2]:30}"]
        report.append(header)
        report.append("")
        
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
            date_to_filter = self.specific_filter[0]["date"]
            for transaction in csv_file:
                if transaction[self.csv_column_info[0]] == date_to_filter:
                    data = [f"{transaction[self.csv_column_info[0]]:10}", f"{transaction[self.csv_column_info[2]]:10}", f"{transaction[self.csv_column_info[1]]:30}"]
                    filtered_dates.append(data)
            if len(filtered_dates) == 0:
                return [["No transactions found."], ""]
            return filtered_dates

        elif self.saved_filters_bool == False:
            print("Input the date in the same format as your .csv file.")
            date_to_filter = input("Please enter the date you would like to filter by: ")
            for transaction in csv_file:
                if transaction[self.csv_column_info[0]] == date_to_filter:
                    data = [f"{transaction[self.csv_column_info[0]]:10}", f"{transaction[self.csv_column_info[2]]:10}", f"{transaction[self.csv_column_info[1]]:30}"]
                    filtered_dates.append(data)
            return filtered_dates

        else:
            print("\nInvalid input. Please restart and try again.")
            sleep(2)
            exit()

    def filter_amount(self, csv_file):
        filtered_amounts = []
        if self.saved_filters_bool == True:
            amount_to_filter = self.specific_filter[0]["amount"]
            for transaction in csv_file:
                if "$" in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("$", "")
                if "," in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(",", "")
                if "(" in transaction[self.csv_column_info[2]] and ")" in transaction[self.csv_column_info[2]]:
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace("(", "-")
                    transaction[self.csv_column_info[2]] = transaction[self.csv_column_info[2]].replace(")", "")
                if float(transaction[self.csv_column_info[2]]) == float(amount_to_filter):
                    data = [f"{transaction[self.csv_column_info[0]]:10}", f"{transaction[self.csv_column_info[2]]:10}", f"{transaction[self.csv_column_info[1]]:30}"]
                    filtered_amounts.append(data)
            if len(filtered_amounts) == 0:
                return [["No transactions found."], ""]
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
                    data = [f"{transaction[self.csv_column_info[0]]:10}", f"{transaction[self.csv_column_info[2]]:10}", f"{transaction[self.csv_column_info[1]]:30}"]
                    filtered_amounts.append(data)
            return filtered_amounts

        else:
            print("\nInvalid input. Please restart and try again.")
            sleep(2)
            exit()

    def filter_description(self, csv_file):
        filtered_descriptions = []
        if self.saved_filters_bool == True:
            description_to_filter = self.specific_filter[0]["description"].lower()
            for transaction in csv_file:
                if description_to_filter in transaction[self.csv_column_info[1]].lower():
                    data = [f"{transaction[self.csv_column_info[0]]:10}", f"{transaction[self.csv_column_info[2]]:10}", f"{transaction[self.csv_column_info[1]]:30}"]
                    filtered_descriptions.append(data)
            if len(filtered_descriptions) == 0:
                return [["No transactions found."], ""]
            return filtered_descriptions

        elif self.saved_filters_bool == False:
            print("Input the description in the same format as your .csv file.")
            description_to_filter = input("Please enter the description you would like to filter by: ").lower()
            for transaction in csv_file:
                if description_to_filter in transaction[self.csv_column_info[1]].lower():
                    data = [f"{transaction[self.csv_column_info[0]]:10}", f"{transaction[self.csv_column_info[2]]:10}", f"{transaction[self.csv_column_info[1]]:30}"]
                    filtered_descriptions.append(data)
            return filtered_descriptions

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
                data = [f"{transaction[self.csv_column_info[0]]:10}", f"{transaction[self.csv_column_info[2]]:10}", f"{transaction[self.csv_column_info[1]]:30}"]
                expenditures.append(data)

        count = 0
        total = 0
        for amount in expenditures:
            count += 1
            total += float(amount[1])

        totals = ["", [f"Total Expenditures: {total:.2f}"], [f"Number of Expenditures: {count}"]]
        for info in totals:
            expenditures.append(info)

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
                data = [f"{transaction[self.csv_column_info[0]]:10}", f"{transaction[self.csv_column_info[2]]:10}", f"{transaction[self.csv_column_info[1]]:30}"]
                income.append(data)

        total = 0
        count = 0
        for amount in income:
            count += 1
            total += float(amount[1])

        totals = ["", [f"Total Income: {total:.2f}"], [f"Number of Transactions: {count}"]]
        for info in totals:
            income.append(info)
        
        return income

    # This is a bar graph example from the matplotlib documentation.
    """
    import matplotlib.pyplot as plt
    import csv
    
    x = []
    y = []
    
    with open('biostats.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        
        for row in plots:
            x.append(row[0])
            y.append(int(row[2]))
    
    plt.bar(x, y, color = 'g', width = 0.72, label = "Age")
    plt.xlabel('Names')
    plt.ylabel('Ages')
    plt.title('Ages of different persons')
    plt.legend()
    plt.show()
    """
    def create_graph(self, data):
        x = []
        y = []

        for key in data:
            x.append(key)
            y.append(data[key])

        plt.bar(x, y, color = 'g', width = 0.72, label = "Amount")
        plt.xlabel('Category')
        plt.ylabel('Amount Spent')
        plt.title('Visual Representation of Bank Statement')
        plt.legend()
        plt.show()
