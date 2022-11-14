import os
import argparse

from comp_validator.check import global_files
from comp_validator.issues import issues

# initiate argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('path', help='path to the converted folder', type=str)

# set up a global counter for showing number of errors
ERROR = 1

# set up a global counter for showing number of warnings
WARNING = 1

ISSUES = {'error': {}, 'warning': {}}


def validate(path):
    global_files.GlobalFiles(path)

    # write all issues in one file
    log()


def log():
    # write errors
    for idx, code in enumerate(ISSUES['error'].keys()):
        with open('error.md', 'a') as file:
            file.write(f'Error {idx + 1}: [Code {code}]')

            for value in ISSUES['error'][code]:
                file.write(value)

    # write warnings
    for idx, code in enumerate(ISSUES['warning'].keys()):
        with open('warnings.md', 'a') as file:
            file.write(f'Warning {idx + 1}: {code}\n')

            for value in ISSUES['warning'][code]:
                file.write(value)


    # for issue in ISSUES.keys():
    #     with open(f'{issue}.txt', 'a') as file:
    #         for code in ISSUES[issue]:
    #             file.write(f'### Error {ERROR}')
    #             for value in ISSUES[issue][code]:

        


# def write_error(num, path):
#     global ERROR, WARNING
#
#     issue, basename = issues.ISSUE_LIST[num], os.path.basename(path)
#     err_type = issue['severity']
#
# #     with open(f'{err_type}.txt', 'a') as file:
# #         error = ERROR if err_type == 'error' else WARNING
# #         file.write(f"""
# # {err_type.casefold()} {error}: [Code {num}] {issue['key']}
# # {issue['reason']}\n
# #
# # {basename}
# # Location:
# # {path}
# #
# # Reason:
# # {issue['reason']}
# # =============================================================\n\n\n
# #         """)
#
#     if err_type == 'error':
#         ERROR += 1
#     else:
#         WARNING += 1

