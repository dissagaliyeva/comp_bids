import json
import os
import re
from pathlib import Path

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

COORDS = ['weights', 'distances', 'delays', 'speeds', 'emp', 'ts', 'events', 'fc', 'vars', 'stimuli', 'noise', 'raster']


class Files:
    def __init__(self, path):
        self.path = path
        self.content = get_files(path)

        # check all json files
        self.check_files()

        # check where nodes/labels are
        self.coords = None
        self.coords_is_global = None
        self.find_coords()

    def find_coords(self):
        coords = []

        for file in self.content:
            if 'nodes' in file:
                coords.append(file)
            if 'labels' in file:
                coords.append(file)

        if coords:
            self.coords = coords
            path, basename = os.path.dirname(coords[0]), os.path.basename(coords[0])

            if 'sub-' not in coords[0].lower():
                p = os.path.basename(os.path.dirname(coords[0]))

                if os.path.exists(os.path.join(path, 'nodes.json')) or os.path.exists(os.path.join(path, 'labels.json')) \
                    or os.path.exists(os.path.join(path, 'nodes.tsv')) or os.path.exists(os.path.join(path, 'labels.tsv')):
                    self.coords = ['../coord/nodes.json', '../coord/labels.json']
                    self.coords_is_global = True
                else:
                    utils.add_error(21, p, basename, f'{", ".join(self.coords)} must be in the global `coord` folder.')
            else:
                p = os.path.basename(os.path.dirname(coords[0]))

                if self.check_nodes_labels():
                    utils.add_error(22, p, basename, 'Nodes/Labels are not unique. Therefore they must be placed in the global `coord` folder.')
                else:
                    self.coords = ['../coord/nodes.json', '../coord/labels.json']
                    self.coords_is_global = False

    def check_nodes_labels(self):
        unique = False

        nodes = get_specific(self.content, 'nodes.tsv')
        node0 = pd.read_csv(nodes[0], header=None, sep='\t')

        if len(nodes) > 1:
            unique = node0.equals(pd.read_csv(nodes[1], header=None, sep='\t'))
            return unique
        return unique

    def check_files(self):
        desc = '{} has {}x{} dimensions. Expected to see {}x{} dimensions.'
        coord_desc = '{} does not have the required field `CoordsRows` or `CoordsColumns`.'

        for file in self.content:
            file = str(file)
            path, basename = os.path.dirname(file), os.path.basename(file)

            if file.endswith('json'):
                jfile = json.load(open(file))

                # check if Description field is present
                if 'Description' not in jfile.keys() and (not 'participants' in file and not 'dataset' in file):
                    utils.add_error(18, path, basename,
                                    evidence=f'{basename} does not have the required field `Description`.')

                # check if NumberOfRows & NumberOfColumns is present
                if get_rows_columns(file, ROWS_COLUMNS):
                    check_rows_columns(jfile, path, basename)

                # check dimensions
                for idx, (dims, dim) in enumerate(zip([NxN_dim, Nx1_dim, Nx2_dim, Nx3_dim, NxM_dim],
                                                      ['n', 1, 2, 3, 'm'])):
                    if get_rows_columns(file, dims):
                        if 'NumberOfRows' in jfile.keys() and 'NumberOfColumns' in jfile.keys():
                            rows, columns = jfile['NumberOfRows'], jfile['NumberOfColumns']

                            if (dim == 'n' and rows != columns) or (dim != 'n' and rows == columns):
                                utils.add_error(19, path, basename, desc.format(basename, rows, columns, 'n', dim))
                        else:
                            check_rows_columns(jfile, path, basename)

                # check if CoordsRows and CoordsColumns are present
                if get_rows_columns(file, COORDS):
                    if 'CoordsRows' in jfile.keys() and 'CoordsColumns' in jfile.keys():
                        rows, columns = jfile['CoordsRows'], jfile['CoordsColumns']

                        if not isinstance(rows, list) or not isinstance(columns, list):
                            utils.add_error(20, path, basename,
                                            f'{basename}\'s `CoordsRows` and `CoordsColumns` must be of type array.')
                    else:
                        utils.add_error(18, path, basename, coord_desc.format(basename))

                # check coordinates folder
                if 'coord' in file:
                    # TODO: check where global nodes/labels are located
                    pass

                if 'code' in file:
                    types = ['arr/str', 'str', 'arr/str', 'str', 'str', 'arr/str', 'arr/str', 'arr/str', 'arr/str']

                    # check fo required fields
                    for idx, field in enumerate(['ModelParam', 'SourceCode', 'SourceCodeVersion', 'SoftwareVersion',
                                                 'SoftwareName', 'SoftwareRepository', 'Network', 'ModelEq']):
                        if field not in jfile.keys():
                            utils.add_error(18, path, basename, f'{basename} does not have the required `{field}` field.')

                        if types[idx] == 'arr/str' and field in jfile.keys():
                            if type(jfile[field]) == str:
                                continue
                            elif type(jfile[field]) == list:
                                continue
                            else:
                                utils.add_error(20, path, basename, f'{basename}\'s {field} must be of type array or string.')
                        elif types[idx] == 'str' and field in jfile.keys():
                            if not isinstance(jfile[field], str):
                                utils.add_error(20, path, basename, f'{basename}\'s {field} must be of type string.')

                    # check recommended field
                    if 'CoordsSeries' in jfile.keys():
                        if type(jfile['CoordsSeries']) == str:
                            continue
                        elif type(jfile['CoordsSeries']) == list:
                            continue
                        else:
                            utils.add_error(20, path, basename, f'{basename}\'s CoordsSeries must be of type array or string.')

                if 'param' in file or 'eq' in file:
                    types = ['arr/str', 'arr/str', 'str', 'str', 'arr/str', 'arr/str']
                    field0 = 'ModelEq' if 'param' in file else 'ModelParam'

                    for idx, field in enumerate([field0, 'SourceCode', 'SourceCodeVersion', 'SoftwareVersion',
                                                 'SoftwareName', 'SoftwareRepository']):
                        # check required field
                        if field not in jfile.keys() and idx == 0:
                            utils.add_error(18, path, basename, f'{basename} does not have the required `{field}` field.')

                        # check recommended field
                        if field in jfile.keys():
                            if types[idx] == 'arr/str':
                                if type(jfile[field]) == str:
                                    continue
                                elif type(jfile[field]) == list:
                                    continue
                                else:
                                    utils.add_error(20, path, basename,
                                                    f'{basename}\'s {field} must be of type array or string.')
                            elif types[idx] == 'str':
                                if not isinstance(jfile[field], str):
                                    utils.add_error(20, path, basename,
                                                    f'{basename}\'s {field} must be of type string.')



            if file.endswith('.tsv'):
                # check dimensions
                pfile = pd.read_csv(file, sep='\t', header=None)
                rows, columns = pfile.shape

                for idx, (dims, dim) in enumerate(zip([NxN_dim, Nx1_dim, Nx2_dim, Nx3_dim, NxM_dim], ['n', 1, 2, 3, 'm'])):
                    if get_rows_columns(file, dims):
                        if (dim == 'n' and rows != columns) or (dim != 'n' and rows == columns) or \
                                (rows == 1):
                            utils.add_error(19, path, basename, desc.format(basename, rows, columns, 'n', dim))


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
            contents.append(str(Path(os.path.join(root, file))))

    return contents


def get_specific(files, name):
    content = []

    for file in files:
        if name in file:
            content.append(file)

    return content
