import json
class Filters:
    def __init__(self):
        pass

    def write_filters(self,json_file):
        with open("Financial Statement Reviewer/filters.json", 'w') as jsonfile:
            json.dump(json_file, jsonfile)

    def read_filters(self):
        with open("Financial Statement Reviewer/filters.json", 'r') as jsonfile:
            self.filters = json.load(jsonfile)
        return self.filters

    def create_filters(self):
        pass

    