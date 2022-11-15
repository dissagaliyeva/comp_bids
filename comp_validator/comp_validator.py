import os
import argparse

from comp_validator.check import global_files, all_files
from comp_validator.issues import issues

ISSUES = {'error': {}, 'warning': {}}


def validate(path):
    global_files.GlobalFiles(path)
    all_files.Files(path)

    # write all issues in one file
    log()


def log():
    # write errors
    for idx, code in enumerate(ISSUES['error'].keys()):
        with open('error.md', 'a') as file:
            file.write(f'Error {idx + 1}: {code}\n')

            for value in ISSUES['error'][code]:
                file.write(value)

    # write warnings
    for idx, code in enumerate(ISSUES['warning'].keys()):
        with open('warnings.md', 'a') as file:
            file.write(f'Warning {idx + 1}: {code}\n')

            for value in ISSUES['warning'][code]:
                file.write(value)

