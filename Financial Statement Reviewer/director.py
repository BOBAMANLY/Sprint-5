# Code imports
from UseFile import UseFile
from Report import Report
from filters import Filters

# Library imports
from os import system, name
from time import sleep

class Director:
    def __init__(self):
        self.file_name = ""
        self.choice = ""
        self.filters_object = Filters()

    def csv_info(self):
        loop = True
        while loop == True:
            print("We will need some information to create a report from your .csv file.")
            print("Use this example to help you: \n")
            print("  1    |     2     |    3")
            print("1/1/10 | Groceries | $100.00\n")
            date_column = input("Using the example tell us which column in your .csv file is the date: ")
            descriptions_column = input("Using the example tell us which column in your .csv file is the description: ")
            amount_column = input("Using the example tell us which column in your .csv file is the amount: ")


    def create_report(self):
        self.clear()
        csv_column_info = self.csv_info()

        


        # Determine if filters are needed
        loop = True
        while loop == True:
            use_filters = input("Would you like to use filters? (yes/no): ").lower()
            if use_filters == "yes" or use_filters == "no":
                loop = False
            else:
                print("\nInvalid input. Please try again.")
                continue

        # Create a new report
        report = Report(self.file_name, self.filters_object.get_filters(), use_filters).create_report()

        # Save the report
        report.save_report(report)

    def view_report(self):
        # TODO: Implement this function
        pass

    def view_csv(self):
        self.clear()
        print("...Financial Statement Reveiwer...")
        print(f"\nFile: {self.file_name}\n")
        csv_file = UseFile().read_csv(self.file_name)
        for line in csv_file:
            print(line)

        input("\nPress enter to return to the main menu.")
        self.main_menu()

    def view_filters(self):
        self.clear()
        self.filters_object.display_filters()
        input("Press enter to return to the main menu.")
        self.main_menu()

    def clear(self):
  
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def main_menu(self):
        self.clear()
        # Display the main menu
        print("...Financial Statement Reveiwer...")
        print("1. Create a new report")
        print("2. View a report")
        print("3. View CSV file")
        print("4. View filters")
        print("5. Exit")

        # Get user input and validate it
        loop = True
        while loop == True:
            try:
                self.choice = int(input("\nEnter your choice: "))
            except:
                print("\nInvalid input. Please try again.")
                continue
            if self.choice >= 1 and self.choice <= 5:
                loop = False
            else:
                print("\nInvalid input. Please try again.")
                continue
        
        # Clear the screen
        self.clear()

        # get file name based on menu choice
        if self.choice == 1 or self.choice == 3:
            # get the file name
            self.file_name = UseFile().get_file_name()

        # Execute the user's choice
        if self.choice == 1:
            self.create_report()
        elif self.choice == 2:
            self.view_report()
        elif self.choice == 3:
            self.view_csv()
        elif self.choice == 4:
            self.view_filters()
        elif self.choice == 5:
            self.clear()
            print("Goodbye!")
            sleep(2)
            self.clear()
            exit()
        else:
            print("Something went wrong.")
            print("Restart and try again.")

        
            
                

