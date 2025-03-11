# Pokemon Database

This repository is based on the [Pokemon Database](https://pokemondb.net) website, being a fork of the [pokemon-db](https://github.com/pokemondb/database) repository.

## Data

The original data is stored in the `data/yaml` directory. It is stored in YAML format for easy readability.

## Format Conversion

The `scripts/convert` directory contains the code used to convert the original data into the other formats, like Parquet, CSV and JSON.

To run the transformation code, use the following command:

```bash
# Install the dependencies
uv sync

# Run the data conversion code
uv run python ./scripts/convert/convert_data_into_parquet.py
# or
uv run python ./scripts/convert/convert_data_into_json.py
# or
uv run python ./scripts/convert/convert_data_into_csv.py
```
