
  #### Files:
-  **split_dataset.py**: split the dataset into subsets based on drug name
-  **subset_ner.py**: do NER work on each of the subsets
-  **drug_subsets.tar.gz**: processed patient profile based on drug names
  #### How to use:
  1. modify the file path in **split_dataset.py** and run `python split_dataset.py`
  2. modify the file path in **subset_ner.py** and run `subset_ner.py`
  #### Environment:
 `transformer 4.37.2`, `pytorch 2.3.0`
