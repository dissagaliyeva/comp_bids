import os

from comp_validator.check import global_files
from comp_validator.issues import issues

# set up a global counter for showing number of errors
ERROR = 1

# set up a global counter for showing number of warnings
WARNING = 1


def validate(path):
    pass


def write_error(num, path):
    global ERROR, WARNING

    issue, basename = issues.ISSUE_LIST[num], os.path.basename(path)
    err_type = issue['severity']

    with open(f'{err_type}.txt', 'a') as file:
        error = ERROR if err_type == 'error' else WARNING
        file.write(f"""{err_type.casefold()} {error}: [Code {num}] {issue['key']}
        {issue['reason']}\n

        {basename}
        Location:
        {path}

        Reason:
        {issue['reason']}
        """)

    if err_type == 'error':
        ERROR += 1
    else:
        WARNING += 1
