import json

import numpy as np
import os
import re

import pandas as pd

from comp_validator import comp_validator as val
from comp_validator import utils


GLOBAL_FILES = ['README', 'CHANGES', 'participants.json', 'participants.tsv', 'dataset_description.json']
SPECIES = ['arabidopsis thaliana', 'bos taurus', 'caenorhabditis elegans', 'chlamydomonas reinhardtii',
           'danio rerio (zebrafish)', 'dictyostelium discoideum', 'drosophila melanogaster', 'escherichia coli',
           'homo sapiens', 'mus musculus', 'hepatitis C virus', 'mycoplasma pneumoniae', 'oryza sativa',
           'plasmodium falciparum', 'pneumocystis carinii', 'rattus norvegicus', 'saccharomyces cerevisiae',
           'schizosaccharomyces pombe', 'takifugu rubripes', 'xenopus laevis', 'zea mays']
HANDEDNESS = ['left', 'l', 'right', 'r', 'a', 'ambidextrous', 'n/a', 'nan', None]

class GlobalFiles:
    def __init__(self, path):
        self.path = path

        # file
        self.readme = None
        self.participants_json = None
        self.participants_tsv = None
        self.changes = None
        self.dataset_description = None

        # iterate over global files
        self.get_files()

    def get_files(self):
        self.readme = utils.check_file_exists(self.path, 'README')
        self.changes = utils.check_file_exists(self.path, 'CHANGES')
        self.participants_tsv = utils.check_file_exists(self.path, 'participants.tsv')
        self.participants_json = utils.check_file_exists(self.path, 'participants.json')
        self.dataset_description = utils.check_file_exists(self.path, 'dataset_description.json')

        self.check_files()

    def check_files(self):
        error_values = [2, 4, 3, 3, 15]

        for idx, file in enumerate([self.readme, self.changes, self.participants_json,
                                    self.participants_tsv, self.dataset_description]):
            if file is None:
                utils.add_error(error_values[idx], self.path, GLOBAL_FILES[idx])
            else:
                if idx == 0:
                    self.check_readme()
                elif idx == 1:
                    self.check_changes()
                elif idx == 2:
                    self.check_participants_json()
                elif idx == 3:
                    self.check_participants_tsv()
                else:
                    self.check_dataset_desc()

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
        file = json.load(open(self.participants_json))
        basename = os.path.basename(self.participants_json)

        if 'age' in file.keys():
            if 'Description' not in file['age'].keys():
                utils.add_error(16, self.path, basename, 'Missing `Description` field for `age` key. Expected the following structure:\n{\n"age"{\n"Description": "age of the participant",\n"Units": "years"\n}\n}'),
            if 'Units' not in file['age'].keys():
                utils.add_error(16, self.path, basename, 'Missing `Units` field for `age` key. Expected the following structure:\n{\n"age"{\n"Description": "age of the participant",\n"Units": "years"\n}\n}'),

        if 'sex' in file.keys():
            if 'Description' not in file['sex'].keys():
                utils.add_error(16, self.path, basename, 'Missing `Description` field for `sex` key. Expected the following structure:\n{\n"sex"{\n"Description": "sex of the participant as reported by the participant",\n"Levels": {\n"M": "male",\n"F": "female"\n}\n}')
            if 'Levels' not in file['sex'].keys():
                utils.add_error(16, self.path, basename, 'Missing `Levels` field for `sex` key. Expected the following structure:\n{\n"sex"{\n"Description": "sex of the participant as reported by the participant",\n"Levels": {\n"M": "male",\n"F": "female"\n}\n}')

        if 'handedness' in file.keys():
            if 'Description' not in file['handedness'].keys():
                utils.add_error(16, self.path, basename, 'Missing `Description` field for `handedness` key. Expected the following structure:\n{\n"handedness"{\n"Description": "handedness of the participant as reported by the participant",\n"Levels": {\n"left": "left",\n"right": "right"\n}\n}')

            if 'Levels' not in file['handedness'].keys():
                utils.add_error(16, self.path, basename, 'Missing `Levels` field for `handedness` key. Expected the following structure:\n{\n"handedness"{\n"Description": "handedness of the participant as reported by the participant",\n"Levels": {\n"left": "left",\n"right": "right"\n}\n}')

    def check_participants_tsv(self):
        file = pd.read_csv(self.participants_tsv, sep='\t')
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
                    utils.add_error(9, self.path, basename, f'Line: {idx}, subject: {content["participant_id"]}')

        for idx, content in file.iterrows():
            # check if species are defined correctly
            if 'species' in content:
                if content['species'] not in SPECIES:
                    utils.add_error(10, self.path, basename,
                                    f'Line: {idx}, subject: {content["participant_id"]}, species: {content["species"]}')

            # check if age is of correct type
            if 'age' in content:
                if type(content['age']) != np.int64 or type(content['age']) != np.float64:
                    utils.add_error(11, self.path, basename,
                                    f'Line: {idx}, subject: {content["participant_id"]}, age: {content["age"]}')

            # check if sex of correct type and if defined correctly
            if 'sex' in content:
                if type(content['sex']) != str:
                    utils.add_error(12, self.path, basename,
                                    f'Line: {idx}, subject: {content["participant_id"]}, sex: {content["sex"]}')
                else:
                    if content['sex'].lower() not in ['m', 'male', 'f', 'female', 'o', 'other', 'n/a', None, 'nan']:
                        utils.add_error(13, self.path, basename,
                                        f'Line: {idx}, subject: {content["participant_id"]}, sex: {content["sex"]}')

            # check if handedness is correctly defined
            if 'handedness' in content:
                if content['handedness'] in HANDEDNESS:
                    utils.add_error(14, self.path, basename,
                                    f'Line: {idx}, subject: {content["participant_id"]}, handedness: {content["handedness"]}')

    def check_dataset_desc(self):
        file = json.load(open(self.dataset_description))
        basename = os.path.basename(self.dataset_description)

        if 'Name' not in file.keys():
            utils.add_error(17, self.path, basename, 'Missing a required field `Name`.')

        if 'Name' in file.keys() and type(file['Name']) != str:
            utils.add_error(17, self.path, basename, 'A required field `Name` should be of type string.')

        if 'BIDSVersion' not in file.keys():
            utils.add_error(17, self.path, basename, 'Missing a required field `BIDSVersion`.')

        if 'BIDSVersion' in file.keys() and type(file['BIDSVersion']) != str:
            utils.add_error(17, self.path, basename, 'A required field `BIDSVersion` should be of type string.')

        if 'HEDVersion' in file.keys() and (type(file['HEDVersion']) != str or type(file['HEDVersion'] != list)):
            utils.add_error(17, self.path, basename, 'A recommended field `HEDVersion` should be of type string or array of strings.')

        if 'DatasetLinks' in file.keys() and (type(file['DatasetLinks']) != object):
            utils.add_error(17, self.path, basename, 'A recommended field `DatasetLinks` should be of type object.')

        if 'DatasetType' in file.keys() and type(file['DatasetType']) != str:
            utils.add_error(17, self.path, basename, 'A recommended field `DatasetType` should be of type string.')

        if 'License' in file.keys() and type(file['License']) != str:
            utils.add_error(17, self.path, basename, 'A recommended field `License` should be of type string.')

        if 'Authors' in file.keys() and (type(file['Authors']) != list):
            utils.add_error(17, self.path, basename, 'A recommended field `Authors` should be of type array of strings.')

        if 'Acknowledgements' in file.keys() and type(file['Acknowledgements']) != str:
            utils.add_error(17, self.path, basename, 'A recommended field `Acknowledgements` should be of type string.')

        if 'HowToAcknowledge' in file.keys() and type(file['HowToAcknowledge']) != str:
            utils.add_error(17, self.path, basename, 'A recommended field `HowToAcknowledge` should be of type string.')

        if 'Funding' in file.keys() and type(file['Funding']) != list:
            utils.add_error(17, self.path, basename, 'A recommended field `Funding` should be of type array.')

        if 'EthicsApproval' in file.keys() and type(file['EthicsApproval']) != list:
            utils.add_error(17, self.path, basename, 'A recommended field `EthicsApproval` should be of type array.')

        if 'ReferencesAndLinks' in file.keys() and type(file['ReferencesAndLinks']) != list:
            utils.add_error(17, self.path, basename, 'A recommended field `ReferencesAndLinks` should be of type array.')

        if 'DatasetDOI' in file.keys() and type(file['DatasetDOI']) != str:
            utils.add_error(17, self.path, basename, 'A recommended field `DatasetDOI` should be of type string.')

        if 'GeneratedBy' in file.keys() and type(file['GeneratedBy']) != list:
            utils.add_error(17, self.path, basename, 'A recommended field `GeneratedBy` should be of type array.')

        if 'SourceDatasets' in file.keys() and type(file['SourceDatasets']) != list:
            utils.add_error(17, self.path, basename, 'A recommended field `SourceDatasets` should be of type array.')

    def check_content(self, file):
        f = open(file).readlines()

        if len(f) == 0:
            utils.add_error(5, self.path, os.path.basename(file))
