import json
import os
import yaml

DATA_DIR = 'data/yaml'

files = os.listdir(DATA_DIR)

for file in files:
    file_name = file.removesuffix('.yaml')
    file_path = os.path.join(DATA_DIR, file)
    
    print(f"Processing '{file}' file...")
    
    data = None
    
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
   
    with open(f'data/json/{file_name}.json', 'w') as f: 
        json.dump(data, f, indent=4)
    
    print(f"Finished processing {file}.")
    print(f"Saved to data/json/{file_name}.json")
    print()
