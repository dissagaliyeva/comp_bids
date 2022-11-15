Error 1: [Code 8] PARTICIPANTS_FILE_NOT_UNIQUE

participants.tsv
Location:
C:\Users\dinar\Desktop\test\output/participants.tsv
Reason:
The recommended file `participants.tsv` contains non-unique `participant_id` values. Each row must have a unique participant id. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.
=============================

Error 2: [Code 9] PARTICIPANTS_FILE_WRONG_NAMING

participants.tsv
Location:
C:\Users\dinar\Desktop\test\output/participants.tsv
Reason:
The recommended file `participants.tsv`'s `participant_id` column has a wrong naming convention. It should start with `sub-` and end with alphanumeric values. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.
Evidence:
Line: 2, subject: s-01
=============================

Error 3: [Code 15] DATASET_DESCRIPTION_MISSING

dataset_description.json
Location:
C:\Users\dinar\Desktop\test\output/dataset_description.json
Reason:
The required file `dataset_description.json` is missing or has a wrong extension. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#dataset_descriptionjson">Section 03 (Modality agnostic files)</a> of the BIDS specificaiton.
=============================

Error 4: [Code 18] JSON_FILE_ISSUES

keycloak_config.json
Location:
C:\Users\dinar\Desktop\test\output\code\tvb-framework-2.6\tvb_framework\tvb\interfaces\rest\server\dev_resources/keycloak_config.json
Reason:
The required file misses required fields in JSON file.
Evidence:
keycloak_config.json does not have the required field `Description`.
=============================

myrealm-realm.json
Location:
C:\Users\dinar\Desktop\test\output\code\tvb-framework-2.6\tvb_framework\tvb\interfaces\rest\server\dev_resources/myrealm-realm.json
Reason:
The required file misses required fields in JSON file.
Evidence:
myrealm-realm.json does not have the required field `Description`.
=============================

tvb-rest.json
Location:
C:\Users\dinar\Desktop\test\output\code\tvb-framework-2.6\tvb_framework\tvb\interfaces\rest\server\dev_resources/tvb-rest.json
Reason:
The required file misses required fields in JSON file.
Evidence:
tvb-rest.json does not have the required field `Description`.
=============================

Error 5: [Code 19] DIMENSIONS_MISMATCH

sub-01_ts.json
Location:
C:\Users\dinar\Desktop\test\output\sub-01\ts/sub-01_ts.json
Reason:
The required JSON file has a mismatch in dimensions.
Evidence:
sub-01_ts.json has 4096x76 dimensions. Expected to see nxn dimensions.
=============================

sub-01_ts_bold.json
Location:
C:\Users\dinar\Desktop\test\output\sub-01\ts/sub-01_ts_bold.json
Reason:
The required JSON file has a mismatch in dimensions.
Evidence:
sub-01_ts_bold.json has 10x76 dimensions. Expected to see nxn dimensions.
=============================

