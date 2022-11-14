from comp_validator.issues.issues import ISSUE_LIST
from comp_validator import comp_validator as val


def add_error(code, path, fname, evidence=None):
    issue = ISSUE_LIST[code]
    name, severity, reason = issue['key'], issue['severity'], issue['reason']
    end = '\n=============================\n\n'

    # if len(val.ISSUES[severity]) > 0 and code not in val.ISSUES[severity]:
    #     if severity == 'error':
    #         val.ERROR += 1
    #     else:
    #         val.WARNING += 1

    # append new issue
    code_name = f'[Code {code}] {name}'

    if code_name not in val.ISSUES[severity]:
        val.ISSUES[severity] = {}
        val.ISSUES[severity][code_name] = []

    if evidence:
        val.ISSUES[severity][code_name].append(f'{fname}\nLocation:\n{path}/{fname}\nReason:\n{reason}\nEvidence:\n{evidence}{end}')
    else:
        val.ISSUES[severity][code_name].append(f'{fname}\nLocation:\n{path}/{fname}\nReason:\n{reason}{end}')
