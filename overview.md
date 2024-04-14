# Side Effect Predictor

## Overview:
This project explores a dataset containing drug reviews, aiming to predict the side effects that can arise for a new patient based on
the presence of risk factors

## Current Strategy:
1. Extract side effects and patient profiles and construct a subset of patients with extensive patient profiles (verbose reviews)
2. Perform collaborative filtering A on hypothetical new patient with verbose reviews to identify most similar reviews. CF A is based on patient profile characteristics.
3. Perform collaborative filtering B on the outputs of CF A to obtain more diverse review set. CF B is based on document embedding of reviews as a whole.
4. Extract most prevalent side effects.



## Folders and Files:

### ./review_dataset

- **drugsComTest_raw.tsv**: Raw test data
- **drugsComTrain_raw.tsv**: Raw training data

### ./explore
This folder contains scripts to perform exploratory data analysis

<!-- - **scr_explore.ipynb**: scratch notebook with some preliminary work -->

### ./process

<!-- - **scr_process.ipynb**: scratch notebook for processing -->
- **ti_idf_per_med.ipynb**: notebook that does TI-IDF per medication

- Create modular side effect extraction script
- BioBERT tool to increase side effect detection in review
- Patient profile extraction
- Recommendation system
- Coupling recommendation system with reviews