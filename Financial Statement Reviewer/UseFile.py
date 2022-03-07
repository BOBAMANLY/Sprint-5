import csv
import json
import os
from os import system, name


class UseFile:
    def __init__(self):
        self.file = ""
        self.csv = []
        self.filters = []

    def read_csv(self):
        with open(self.file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.csv.append(row)
        return self.csv

    def read_filters(self):
        with open("Financial Statement Reviewer/filters.json", 'r') as jsonfile:
            self.filters = json.load(jsonfile)
        return self.filters

    def write_filters(self,json_file):
        with open("Financial Statement Reviewer/filters.json", 'w') as jsonfile:
            json.dump(json_file, jsonfile)

    def clear(self):
  
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def get_file_name(self):
        print("Please ensure the file to analyze is saved in the 'CSV Files' folder in a CSV file format.")
        input("Press Enter to continue...\n")

        # List the possible options
        path = "Financial Statement Reviewer/CSV Files"
        path_options = os.listdir(path)
        if len(path_options) == 0:
            print("\nThere are no files in the 'CSV Files' folder.")
            print("Please ensure the file to analyze is saved in the 'CSV Files' folder in a CSV file format.")
            print("Check the file location and re-run the program to continue.")
            input("Press Enter to close...\n")
            self.clear()
            exit()
        else:
            x = 1
            for file in path_options:
                if file.endswith(".csv"):
                    print(f"{x}. {file}")
                    x += 1  

            # Display warning
            print("\nWARNING: File must be in CSV format to view and continue.")

            # Get user input
            while True:
                try:
                    file_number = int(input("\nEnter the number of the file you wish to analyze: "))
                    if file_number <= 0 or file_number > len(os.listdir(path)):
                        print("\nInvalid input. Please try again.")
                        continue
                    else:
                        break
                except ValueError:
                    print("\nInvalid input. Please try again.")

            # Get the file name
            self.file = os.listdir(path)[file_number - 1]
            return self.file

    def get_file(self):
        return self.file
        
    def get_csv(self):
        return self.csv

    def get_filters(self):
        return self.filters

        