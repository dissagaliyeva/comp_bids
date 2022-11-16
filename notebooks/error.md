Error 1: [Code 8] PARTICIPANTS_FILE_NOT_UNIQUE

participants.tsv
Location:
C:\Users\dinar\Desktop\test\output\participants.tsv
Reason:
The recommended file `participants.tsv` contains non-unique `participant_id` values. Each row must have a unique participant id. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.
=============================

Error 2: [Code 9] PARTICIPANTS_FILE_WRONG_NAMING

participants.tsv
Location:
C:\Users\dinar\Desktop\test\output\participants.tsv
Reason:
The recommended file `participants.tsv`'s `participant_id` column has a wrong naming convention. It should start with `sub-` and end with alphanumeric values. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file">Section 03 (Modality agnostic file)</a> of the BIDS specification.
Evidence:
Line: 2, subject: s-01
=============================

Error 3: [Code 15] DATASET_DESCRIPTION_MISSING

dataset_description.json
Location:
C:\Users\dinar\Desktop\test\output\dataset_description.json
Reason:
The required file `dataset_description.json` is missing or has a wrong extension. See <a href="https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#dataset_descriptionjson">Section 03 (Modality agnostic files)</a> of the BIDS specificaiton.
=============================

Error 4: [Code 21] WRONG_DESTINATION

labels.json
Location:
coord\labels.json
Reason:
The required TSV or JSON file is incorrectly placed.
Evidence:
coordinates (nodes/labels) must be in the global `coord` folder.
=============================

Error 5: [Code 20] WRONG_TYPE

code.json
Location:
C:\Users\dinar\Desktop\test\output\code\code.json
Reason:
The required JSON file has a wrong field type.
Evidence:
SoftwareVersion field must be of type string.
=============================

eq.json
Location:
C:\Users\dinar\Desktop\test\output\eq\eq.json
Reason:
The required JSON file has a wrong field type.
Evidence:
SoftwareVersion field must be of type string.
=============================

param.json
Location:
C:\Users\dinar\Desktop\test\output\param\param.json
Reason:
The required JSON file has a wrong field type.
Evidence:
SoftwareVersion field must be of type string.
=============================

sub-01_sim_fc.json
Location:
C:\Users\dinar\Desktop\test\output\sub-01\spatial\sub-01_sim_fc.json
Reason:
The required JSON file has a wrong field type.
Evidence:
SoftwareVersion field must be of type string.
=============================

Error 6: [Code 18] JSON_FILE_ISSUES

labels.json
Location:
C:\Users\dinar\Desktop\test\output\coord\labels.json
Reason:
The required file misses required fields in JSON file.
Evidence:
labels.json does not have the required `Units` field.
=============================

nodes.json
Location:
C:\Users\dinar\Desktop\test\output\coord\nodes.json
Reason:
The required file misses required fields in JSON file.
Evidence:
nodes.json does not have the required `Units` field.
=============================

eq.json
Location:
C:\Users\dinar\Desktop\test\output\eq\eq.json
Reason:
The required file misses required fields in JSON file.
Evidence:
eq.json does not have the required `ModelParam` field.
=============================

