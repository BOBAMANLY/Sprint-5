import json
from os import system, name

class Filters:
    def __init__(self):
        self.filters = self.read_filters()

    def clear(self):
  
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    
    def get_filters(self):
        return self.filters

    def write_filters(self,json_file):
        with open("Financial Statement Reviewer/filters.json", 'w') as jsonfile:
            json.dump(json_file, jsonfile)

    def read_filters(self):
        with open("Financial Statement Reviewer/filters.json", 'r') as jsonfile:
            self.filters = json.load(jsonfile)
        return self.filters

    def display_filters(self):
        for item in self.filters["Saved Filters"]:
            print(json.dumps(item, indent=3, sort_keys=True))

    def create_filters(self):
        self.clear()
        print("...Create Filters...")
        

    