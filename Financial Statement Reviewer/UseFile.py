import csv
import json
import os

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

    def get_file_name(self):
        print("Please ensure the file to analyze is saved in the 'CSV Files' folder in a CSV file format.")
        input("Press Enter to continue...")

        # List the possible options
        path = "Financial Statement Reviewer/CSV Files"
        x = 0
        for file in os.listdir(path):
            if file.endswith(".csv"):
                print(f"{x + 1}. {file}")

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

        