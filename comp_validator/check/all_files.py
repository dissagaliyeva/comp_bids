import json
import os
import re
import numpy as np
import pandas as pd
from comp_validator import utils

ROWS_COLUMNS = ['weights', 'distances', 'delays', 'speeds', 'times', 'nodes', 'labels', 'vertices', 'faces', 'vnormals',
                'fnormals', 'sensors', 'orientations', 'map', 'conv', 'volumes', 'areas', 'cartesian2d', 'cartesian3d',
                'polar2d', 'polar3d', 'vars', 'stimuli', 'noise', 'raster', 'emp', 'ts', 'events', 'fc', 'hemisphere']

NxN_dim = ['weights', 'distances', 'delays', 'speeds', 'fc']
Nx1_dim = ['times', 'areas', 'volumes', 'hemisphere']


class Files:
    def __init__(self, path):
        self.path = path
        self.content = get_files(path)

        # check all json files
        self.check_files()

    def check_files(self):
        for file in self.content:
            if file.endswith('json'):
                jfile = json.load(open(file))
                path, basename = os.path.dirname(file), os.path.basename(file)

                # check if Description field is present
                if 'Description' not in jfile.keys():
                    utils.add_error(18, path, basename,
                                    evidence=f'{basename} does not have the required field `Description`.')

                # check if NumberOfRows & NumberOfColumns is present
                if get_rows_columns(file, ROWS_COLUMNS):
                    if 'NumberOfRows' not in jfile.keys():
                        utils.add_error(18, path, basename,
                                        evidence=f'`{basename}` does not have the required field `NumberOfRows`.')
                    if 'NumberOfColumns' not in jfile.keys():
                        utils.add_error(18, path, basename,
                                        evidence=f'`{basename}` does not have the required field `NumberOfColumns`.')

                # check nxn dimensions
                if get_rows_columns(file, NxN_dim):
                    rows, columns = file['NumberOfRows'], file['NumberOfColumns']
                    if rows != columns:
                        utils.add_error(19, path, basename, evidence=f'`{basename}` has {rows}x{columns} dimensions. Expected to see nxn dimensions.')

                # check nx1 dimensions
                if get_rows_columns(file, Nx1_dim):
                    rows, columns = file['NumberOfRows'], file['NumberOfColumns']
                    if rows != columns:
                        utils.add_error(19, path, basename, evidence=f'`{basename}` has {rows}x{columns} dimensions. Expected to see nx1 dimensions.')


def get_rows_columns(file, file_names):
    for name in file_names:
        if name in file:
            return True

    return False



def get_files(path):
    contents = []

    for root, dirs, files in os.walk(path):
        for file in files:
            contents.append(os.path.join(root, file))

    return contents


def get_specific(files, name):
    content = []

    for file in files:
        if name in file:
            content.append(file)

    return content
