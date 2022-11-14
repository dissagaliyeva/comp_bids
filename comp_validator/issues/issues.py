"""
List of issues as specified in BIDS-validator:
https://github.com/bids-standard/bids-validator/blob/1c9598538929e4c067ca714ccea7f8778760938e/bids-validator/utils/issues/list.js
"""


ISSUE_LIST = {
    # All files that need to be fixed (severity='error')
    1: dict(key='NOT_INCLUDED', severity='error', reason=''),
    2: dict(key='README_FILE_MISSING', severity='error', reason='The required file `README` is missing or has wrong extension (accepted extensions: `md`, `txt`, and `rst`). See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#readme">Section 03 (Modality agnostic files)</a> of the BIDS specification.'),
    3: dict(key='PARTICIPANTS_FILE_MISSING', severity='warning', reason='The recommended file `participants.json` or `participants.tsv` is missing. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    4: dict(key='CHANGES_FILE_MISSING', severity='warning', reason='The recommended file `CHANGES` is missing. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#changes">Section 03 (Modality agnostic files)</a> of the BIDS specification.'),
    5: dict(key='EMPTY_FILE', severity='warning', reason='Empty files not allowed.'),
    6: dict(key='CHANGES_FILE_WRONG_EXT', severity='warning', reason='The recommended file `CHANGES` has an incorrect extension. The accepted extension is `txt`. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#changes">Section 03 (Modality agnostic files)</a> of the BIDS specification.'),

}
