# Notebooks
This folder will contain the bulk of the work. Initially, as you explore the dataset, there will most likely be a loose connection of notebooks here. As you start working towards a consistent narrative, take the time to structure the notebooks into a logical series. This should also be reflected by the notebooks' filenames: `01-first-logical-notebook.ipynb`, `02-second-logical-notebook.ipynb`, and so on. Ideally, each notebook should produce some kind of output (stored in the appropriate project folder), that the next notebook uses as input. For example:

```
01-data-cleaning.ipynb       # Reads '../data/raw/data_raw.scv' and produces '../data/cleaned/data_clean.csv'
02-data-preprocessing.ipynb  # Reads '../data/cleaned/data_clean.csv' and produces '../data/processed/data_processed.csv'
03-model-selection.ipynb     # Reads '../data/processed/data_processed.csv' and produces '../models/model.pkl'
04-model-evaluation.ipynb    # Reads '../models/model.pkl' and produces tables and figures stored in '../results/'

```