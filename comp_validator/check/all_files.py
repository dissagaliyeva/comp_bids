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
Nx2_dim = ['cartesian2d', 'polar2d']
Nx3_dim = ['nodes', 'vertices', 'vnormals', 'fnormals', 'sensors', 'orientations', 'cartesian3d', 'polar3d']
NxM_dim = ['map', 'faces']
TxN_dim = ['vars', 'stimuli', 'noise', 'raster', 'emp', 'ts', 'events']


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
                    check_rows_columns(jfile, path, basename)

                # check dimensions

                desc = '{} has {}x{} dimensions. Expected to see {}x{} dimensions.'
                for idx, (dims, dim) in enumerate(zip([NxN_dim, Nx1_dim, Nx2_dim, Nx3_dim, NxM_dim],
                                                      ['n', 1, 2, 3, 'm'])):
                    if get_rows_columns(file, dims):
                        if 'NumberOfRows' in jfile.keys() and 'NumberOfColumns' in jfile.keys():
                            rows, columns = jfile['NumberOfRows'], jfile['NumberOfColumns']

                            if (dim == 'n' and rows != columns) or (dim != 'n' and rows == columns):
                                utils.add_error(19, path, basename, desc.format(basename, rows, columns, 'n', dim))
                        else:
                            check_rows_columns(jfile, path, basename)

                if get_rows_columns(file, TxN_dim):
                    if 'NumberOfRows' in jfile.keys() and 'NumberOfColumns' in jfile.keys():
                        rows, columns = jfile['NumberOfRows'], jfile['NumberOfColumns']

                        if rows == columns:
                            utils.add_error(19, path, basename, desc.format(basename, rows, columns, 't', 'n'))
                    else:
                        check_rows_columns(jfile, path, basename)


def check_rows_columns(jfile, path, basename):
    if 'NumberOfRows' not in jfile.keys():
        utils.add_error(18, path, basename,
                        evidence=f'`{basename}` does not have the required field `NumberOfRows`.')
    if 'NumberOfColumns' not in jfile.keys():
        utils.add_error(18, path, basename,
                        evidence=f'`{basename}` does not have the required field `NumberOfColumns`.')


def get_rows_columns(file, file_names):
    for name in file_names:
        if name in file and 'tvb-framework' not in file:
            if name == 'ts':
                if len(os.path.basename(file)) != 2 or '_ts.' not in file or '/ts' not in file:
                    continue
                else:
                    return True
            else:
                return True

    return False


def get_files(path):
    contents = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if 'tvb-framework' in root:
                continue
            contents.append(os.path.join(root, file))

    return contents


def get_specific(files, name):
    content = []

    for file in files:
        if name in file:
            content.append(file)

    return content
