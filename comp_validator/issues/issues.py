"""
List of issues as specified in BIDS-validator:
https://github.com/bids-standard/bids-validator/blob/1c9598538929e4c067ca714ccea7f8778760938e/bids-validator/utils/issues/list.js
"""


ISSUE_LIST = {
    # All files that need to be fixed (severity='error')
    1: dict(key='NOT_INCLUDED', severity='error', reason='The required TSV or JSON file is missing.'),
    2: dict(key='README_FILE_MISSING', severity='error', reason='The required file `README` is missing or has a wrong extension (accepted extensions: `md`, `txt`, and `rst`). See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#readme">Section 03 (Modality agnostic files)</a> of the BIDS specification.'),
    3: dict(key='PARTICIPANTS_FILE_MISSING', severity='warning', reason='The recommended file `participants.json` or `participants.tsv` is missing. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    4: dict(key='CHANGES_FILE_MISSING', severity='warning', reason='The recommended file `CHANGES` is missing. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#changes">Section 03 (Modality agnostic files)</a> of the BIDS specification.'),
    5: dict(key='EMPTY_FILE', severity='warning', reason='Empty files not allowed.'),
    6: dict(key='CHANGES_FILE_WRONG_EXT', severity='warning', reason='The recommended file `CHANGES` has an incorrect extension. The accepted extension is `txt`. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#changes">Section 03 (Modality agnostic files)</a> of the BIDS specification.'),
    7: dict(key='PARTICIPANTS_FILE_MISSING_PARTICIPANT_ID_COLUMN', severity='error', reason='The recommended file `participants.tsv` does not have the required `participant_id` column. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    8: dict(key='PARTICIPANTS_FILE_NOT_UNIQUE', severity='error', reason='The recommended file `participants.tsv` contains non-unique `participant_id` values. Each row must have a unique participant id. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    9: dict(key='PARTICIPANTS_FILE_WRONG_NAMING', severity='error', reason='The recommended file `participants.tsv`\'s `participant_id` column has a wrong naming convention. It should start with `sub-` and end with alphanumeric values. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    10: dict(key='PARTICIPANTS_FILE_WRONG_SPECIES', severity='warning', reason=f'The recommended file `participants.tsv`\'s `species` column does not have the correct species. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    11: dict(key='PARTICIPANTS_FILE_WRONG_AGE', severity='warning', reason=f'The recommended file `participants.tsv`\'s `age` column has to be either integer or float. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    12: dict(key='PARTICIPANTS_FILE_WRONG_SEX_TYPE', severity='warning', reason='The recommended file `participants.tsv`\'s `sex` columns has to be of type string. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    13: dict(key='PARTICIPANTS_FILE_WRONG_SEX_NAME', severity='warning', reason='The recommended file `participants.tsv`\'s `sex` columns has to have one of the following values: male, m, M, MALE, Male, female, f, F, FEMALE, Female, other, o, O, OTHER, Other, n/a. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    14: dict(key='PARTICIPANTS_FILE_WRONG_HANDEDNESS_TYPE', severity='warning', reason='The recommendedfile `participants.tsv`\'s `handedness` columns has to have one of the following values: left, l, L, LEFT, Left, right, r, R, RIGHT, Right, ambidextrous, a, A, AMBIDEXTROUS, Ambidextrous, n/a. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    15: dict(key='DATASET_DESCRIPTION_MISSING', severity='error', reason='The required file `dataset_description.json` is missing or has a wrong extension. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#dataset_descriptionjson">Section 03 (Modality agnostic files)</a> of the BIDS specificaiton.'),
    16: dict(key='PARTICIPANTS_FILE_MISSING_FIELDS', severity='warning', reason='The recommended file `participants.json` has missing values. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.'),
    17: dict(key='DATASET_DESCRIPTION_MISSING_FIELDS', severity='warning', reason='The required file `dataset_description.json` has missing values. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#dataset_descriptionjson">Section 03 (Modality agnostic files)</a> of the BIDS specification.'),
    18: dict(key='JSON_FILE_ISSUES', severity='error', reason='The required file misses required fields in JSON file.'),
    19: dict(key='DIMENSIONS_MISMATCH', severity='error', reason='The required JSON file has a mismatch in dimensions.'),
    20: dict(key='WRONG_TYPE', severity='error', reason='The required JSON file has a wrong field type.'),
    21: dict(key='WRONG_DESTINATION', severity='error', reason='The required TSV or JSON file is incorrectly placed.'),



}
