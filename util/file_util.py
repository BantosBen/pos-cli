import json
from os.path import exists


class FileUtil:
    def __init__(self, _table_name):
        self.table_name = 'data/' + _table_name+'.json'

    def read_data(self):
        if exists(self.table_name):
            with open(self.table_name, 'r') as table:
                data = json.load(table)
            return data
        else:
            return dict()

    def write_data(self, data):
        with open(self.table_name, 'w') as table:
            json.dump(data, table)
