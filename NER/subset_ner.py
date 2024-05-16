from transformers import BertTokenizer, BertModel
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import pandas as pd
import torch
import re
import os
import warnings
import csv
import numpy as np

# init tokenizer
tokenizer_medical = AutoTokenizer.from_pretrained("Clinical-AI-Apollo/Medical-NER")
model_medical = AutoModelForTokenClassification.from_pretrained("Clinical-AI-Apollo/Medical-NER")
nlp_medical = pipeline("ner", model=model_medical, tokenizer=tokenizer_medical, aggregation_strategy="simple")

def get_ner_results(text, nlp_pipeline):
    return nlp_pipeline(text)

def process_datasets(directory_path):
    file_list = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith('.csv')]
    symptom_columns = [f'symptom{i+1}' for i in range(10)]
    columns = ['patient_id', 'age', 'sex', 'duration','disease'] + symptom_columns
    processed_data = pd.DataFrame(columns=columns)

    for file_name in file_list:
        processed_data = pd.DataFrame(columns=columns)
        data = pd.read_csv(file_name, sep=',', on_bad_lines='skip')
        print(f"Processing file: {file_name}")

        all_rows = []
        scores = []
        for index, row in data.iterrows():
            text = row.review
            ner_results_medical = get_ner_results(text, nlp_medical)

            temp_dict = {col: None for col in columns}
            temp_dict['patient_id'] = index
            symptoms = []


            for entity in ner_results_medical:
                entity_type = entity['entity_group']
                if entity_type == 'AGE' and temp_dict['age'] is None:
                    temp_dict['age'] = entity['word']
                    scores.append(entity['score'])
                elif entity_type == 'SEX' and temp_dict['sex'] is None:
                    temp_dict['sex'] = entity['word']
                    scores.append(entity['score'])
                elif entity_type == 'DURATION' and temp_dict['duration'] is None:
                    temp_dict['duration'] = entity['word']
                    scores.append(entity['score'])
                elif entity_type == 'DISEASE_DISORDER' and temp_dict['disease'] is None:
                    temp_dict['disease'] = entity['word']
                    scores.append(entity['score'])
                elif entity_type == 'SIGN_SYMPTOM':
                    symptoms.append(entity['word'])
                    scores.append(entity['score'])

            for i, symptom in enumerate(symptoms):
                if i < 10:  # fill out at most 10 symptoms
                    temp_dict[f'symptom{i+1}'] = symptom

            all_rows.append(temp_dict)

        results_df = pd.DataFrame(all_rows)
        output_path = file_name.replace('.csv', '_ner_results.csv')
        results_df.to_csv(output_path, index=False)
        print(f"Processed and saved NER results for {file_name} to {output_path}")

        average_score = sum(scores) / len(scores) if scores else 0
        print(f"Average score for entities in {file_name}: {average_score}")

file_list = '/mnt/biobert/drug_subsets_top5'
process_datasets(file_list)

