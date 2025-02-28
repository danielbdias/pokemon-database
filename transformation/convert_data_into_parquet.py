import os
import yaml
import pandas as pd

DATA_DIR = 'data/yaml'

files = os.listdir(DATA_DIR)

for file in files:
    file_name = file.removesuffix('.yaml')
    file_path = os.path.join(DATA_DIR, file)
    
    print(f"Processing '{file}' file...")
    
    data = None
    
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
        
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_parquet(f'data/parquet/{file_name}.parquet')
    
    print(f"Finished processing {file}.")
    print(f"Saved to data/parquet/{file_name}.parquet")
    print()
