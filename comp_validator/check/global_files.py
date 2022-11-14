import os
import re

import pandas as pd

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

    def check_files(self):
        error_values = [2, 4, 3, 3]

        for idx, file in enumerate([self.readme, self.changes, self.participants_json, self.participants_tsv]):
            if file is None:
                utils.add_error(error_values[idx], self.path, GLOBAL_FILES[idx])
            else:
                if idx == 0:
                    self.check_readme()
                elif idx == 1:
                    self.check_changes()
                elif idx == 2:
                    self.check_participants_json()
                else:
                    self.check_participants_tsv()

    def check_readme(self):
        ext = self.readme.split('.')[-1]
        if ext not in ['rst', 'md', 'txt']:
            utils.add_error(2, self.path, os.path.basename(self.readme))

        # open readme file
        self.check_content(self.readme)

    def check_changes(self):
        if not self.changes.endswith('.txt'):
            utils.add_error(6, self.path, os.path.basename(self.changes))

        # open readme file
        self.check_content(self.changes)

    def check_participants_json(self):
        pass

    def check_participants_tsv(self):
        file = pd.read_csv(self.participants_tsv, sep='\t')
        print(file)
        basename = os.path.basename(self.participants_tsv)

        # check if the required column is present
        if 'participant_id' not in list(file.columns):
            utils.add_error(7, self.path, basename)
        else:
            # check if each column contains unique id
            if len(file['participant_id'].unique()) != len(file):
                utils.add_error(8, self.path, basename)

            # check if each participant is correctly named (starts with 'sub-' and ends with alphanumeric values)
            for idx, content in file.iterrows():
                if len(re.findall(r'sub-[0-9a-zA-Z]+', content['participant_id'], flags=re.IGNORECASE)) == 0:
                    utils.add_error(9, self.path, basename, f'Line {idx}, subject: {content["participant_id"]}')

    def check_content(self, file):
        f = open(file).readlines()

        if len(f) == 0:
            utils.add_error(5, self.path, os.path.basename(file))
