import pandas as pd
import os

def read_tsv_file(file_path):
    try:
        data = []
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            # Using the CSV reader with the tab delimiter
            reader = csv.reader(file, delimiter='\t')

            # Reading headers
            headers = next(reader)
            print("Headers:", headers)

            # Reading data rows
            for row in reader:
                data.append(row)

        # Create a Pandas DataFrame using the headers and data
        df = pd.DataFrame(data, columns=headers)
        return df

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Absolute Path
dataset_path = '/mnt/biobert/side_effect_predictor/review_dataset/'
file_path = dataset_path + 'drugsComTrain_raw.tsv'

dataset_df = pd.read_csv(file_path, sep='\t')

# Split DataFrame into subsets based on drug name
drug_subsets = {drug: dataset_df[dataset_df['drugName'] == drug] for drug in dataset_df['drugName'].unique()}

# output dir
output_dir = '/mnt/biobert/drug_subsets/'
os.makedirs(output_dir, exist_ok=True)

for drug, subset in drug_subsets.items():
    safe_drug_name = drug.replace('/', '_').replace('\\', '_')
    filename = f'subset_{safe_drug_name}.csv'
    file_path = os.path.join(output_dir, filename)
    subset.to_csv(file_path, index=False)
    print(f'Saved {file_path}')

