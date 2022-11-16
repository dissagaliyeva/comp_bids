import os
from pathlib import Path

from comp_validator.issues.issues import ISSUE_LIST
from comp_validator import comp_validator as val


def add_error(code, path, fname, evidence=None):
    path = str(Path(os.path.join(path, fname)))
    issue = ISSUE_LIST[code]
    name, severity, reason = issue['key'], issue['severity'], issue['reason']
    end = '\n=============================\n\n'

    # append new issue
    code_name = f'[Code {code}] {name}\n'

    if len(val.ISSUES[severity]) == 0:
        val.ISSUES[severity] = {}

    if code_name not in val.ISSUES[severity]:
        val.ISSUES[severity][code_name] = []

    if evidence:
        val.ISSUES[severity][code_name].append(f'{fname}\nLocation:\n{path}\nReason:\n{reason}\nEvidence:\n{evidence}{end}')
    else:
        val.ISSUES[severity][code_name].append(f'{fname}\nLocation:\n{path}\nReason:\n{reason}{end}')


def check_file_exists(path, file):
    files = os.listdir(path)

    for f in files:
        ext = f.split('.')[-1]

        if file in ['README', 'CHANGES'] and file in f and ext in ['txt', 'rst', 'md']:
            return os.path.join(path, f)

        if file == f:
            return os.path.join(path, f)

    return None
