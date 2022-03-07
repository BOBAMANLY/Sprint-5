# Code imports
from UseFile import UseFile
from Report import Report

# Library imports
from os import system, name
from time import sleep

class Director:
    def __init__(self):
        self.file_name = ""
        self.choice = ""

    def create_report(self):

        # Get the file name
        self.file = UseFile().get_file_name()
        
        # choose filters
        filters = UseFile().get_filters()

        # Create a new report
        report = Report(self.file, filters)

    def view_report(self):
        # TODO: Implement this function
        pass

    def view_csv(self):
        # TODO: Implement this function
        pass

    def view_filters(self):
        # TODO: Implement this function
        pass

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

        
            
                

