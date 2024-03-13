import tarfile
import os

# Replace 'your_dataset.tar' with the actual path to your .tar dataset
tar_file_path = "D:\\Documents\\Qua môn\\Datawarehouse&BI\\dvdrental.tar"

# Extract the .tar file
extract_folder = 'extracted_dataset'
with tarfile.open(tar_file_path, 'r') as tar:
    tar.extractall(extract_folder)

# Process the extracted files (assuming they are text files)
for root, dirs, files in os.walk(extract_folder):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'r') as f:
            # Process the contents of the file
            content = f.read()
            # You can perform further processing based on your dataset's format
            print(f"Contents of {file_path}:\n{content}")

# Cleanup: Optionally, you can remove the extracted folder after processing
import shutil
shutil.rmtree(extract_folder)
