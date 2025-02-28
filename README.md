# Pokemon Database

This repository is based on the [Pokemon Database](https://pokemondb.net) website, being a fork of the [pokemon-db](https://github.com/pokemondb/database) repository.

## Data

The original data is stored in the `data/yaml` directory. It is stored in YAML format for easy readability.

## Transformation

The `transformation` directory contains the code used to transform the original data into the other formats, like Parquet.

To run the transformation code, use the following command:

```bash
# Install the dependencies
uv sync

# Run the transformation code
uv run python ./transformation/convert_data_into_parquet.py
```