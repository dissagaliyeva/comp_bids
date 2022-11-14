import os
from comp_validator import comp_validator as val
from comp_validator import utils


GLOBAL_FILES = ['README', 'CHANGES', 'participants.json', 'participants.tsv']


class GlobalFiles:
    def __init__(self, path):
        self.path = path

        # file
        self.readme = None
        self.participants_json = None
        self.participants_tsv = None
        self.changes = None

        # iterate over global files
        self.get_files()

    def get_files(self):
        for file in os.listdir(self.path):
            path = os.path.join(self.path, file)

            if 'README' in file:
                self.readme = path
            elif 'CHANGES' in file:
                self.readme = path
            elif 'participants.json' in file:
                self.participants_json = path
            elif 'participants.tsv' in file:
                self.participants_tsv = path

        self.check_files()

    def check_files(self):
        error_values = [2, 4, 3, 3]

        for idx, file in enumerate([self.readme, self.changes, self.participants_json, self.participants_tsv]):
            if file is None:
                # val.write_error(error_values[idx], os.path.join(self.path, GLOBAL_FILES[idx]))
                utils.add_error(error_values[idx], self.path, GLOBAL_FILES[idx])

    def check_readme(self):
        pass