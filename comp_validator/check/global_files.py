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
        self.readme = utils.check_file_exists(self.path, 'README')
        self.changes = utils.check_file_exists(self.path, 'CHANGES')
        self.participants_tsv = utils.check_file_exists(self.path, 'participants.tsv')
        self.participants_json = utils.check_file_exists(self.path, 'participants.json')

        self.check_files()

        print(self.changes)

    def check_files(self):
        error_values = [2, 4, 3, 3]

        for idx, file in enumerate([self.readme, self.changes, self.participants_json, self.participants_tsv]):
            if file is None:
                utils.add_error(error_values[idx], self.path, GLOBAL_FILES[idx])

    def check_readme(self):
        pass