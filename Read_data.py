import tarfile
import os
import pandas as pd

# Replace 'your_dataset.tar' with the actual path to your .tar dataset
tar_file_path = "D:\\Documents\\Qua môn\\Datawarehouse&BI\\dvdrental.tar"

# Extract the .tar file
extract_folder = "D:\\ocuments\\Qua môn\\Datawarehouse&BI\\extracted_data"
with tarfile.open(tar_file_path, 'r') as tar:
    tar.extractall(extract_folder)

# Process the extracted files and convert to Excel
excel_file_path = "D:\Documents\\Qua môn\\Datawarehouse&BI\\Dataset.xlsx"
df_list = []

for root, dirs, files in os.walk(extract_folder):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'r') as f:
            # Assuming the dataset is in CSV format
            df = pd.read_csv(f)
            df_list.append(df)

# Combine all DataFrames into a single Excel file
with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
    for i, df in enumerate(df_list):
        df.to_excel(writer, sheet_name=f'Sheet{i+1}', index=False)

# Cleanup: Optionally, you can remove the extracted folder after processing
import shutil
shutil.rmtree(extract_folder)

print(f'Dataset successfully converted to Excel: {excel_file_path}')
