import csv
import json
import os
from os import system, name


class UseFile:
    def __init__(self):
        self.file = ""
        self.file_name = ""
        self.csv = []

    def read_csv(self, file_name):
        with open(f"Financial Statement Reviewer/CSV Files/{file_name}", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.csv.append(row)
        return self.csv

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
                    if file_number <= 0 or file_number > len(path_options):
                        print("\nInvalid input. Please try again.")
                        continue
                    else:
                        break
                except ValueError:
                    print("\nInvalid input. Please try again.")

            # Get the file name
            self.file_name = path_options[file_number - 1]
            return self.file_name

    def get_file(self):
        return self.file
        
    def get_csv(self):
        return self.csv

        