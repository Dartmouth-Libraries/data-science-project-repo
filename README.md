# Fashion Classifier

This project trains and evaluates a classifier on the Fashion MNIST dataset.

## Table of Contents

- [Fashion Classifier](#fashion-classifier)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Repository Structure](#repository-structure)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Data](#data)
  - [Methods](#methods)
  - [License](#license)

## Project Overview

This project is used as an example project to illustrate how the template Data Science Project Repo can be adapted to an indiviudal project. It uses a very basic example from the PyTorch documentation: Download and explore the Fashion MNIST dataset, then train a simple neural network on the dataset to classifiy the kind of fashion item (skirt, shoe, shirt, ...).

## Repository Structure

This repository is structured as follows:

```
├── data/                                 # The dataset is rather large and kept outside of the repository.
|   └── README.md                         # See this README to learn how to obtain the dataset.
├── notebooks/
|   ├── 01-model-training.ipynb           # The neural network is trained in this notebook.
|   ├── 02-model-evaluation.ipynb         # The network trained above is evaluated on the test set here.
|   └── archive/
|	  |   └── eda.ipynb                       # Some non-essential code exploring the dataset.
|   └── README.md                         # See this README for more info on the individual notebooks.
├── fashion_classifier/                   # Lightweight package containing code used throughout the project
|   ├── fashion_classifier/
|	  | ├── __init__.py
|	  | ├── config.py
|	  | ├── data.py
|	  | ├── model.py
|   └── setup.py
|   └── README.md                         # See this README for installation instructions.
├── models/
|   ├── trained_model.pt                  # The model trained in the above notebook.
|   └── README.md                         # See this README for more info on the trained model.
├── scripts/
|   ├── get_data.py                       # Retrieves the dataset and places it into the data directory
|   └── README.md                         # See this README for more info on the scripts.
├── .gitignore
├── README.md                             # This README.
└── requirements.txt
```

## Installation

Install the projects requirements using the provided file:

```bash
pip install -r requirements.txt
```

Also install the local package:
```bash
pip install --editable ./fashion_classifier
```

## Usage

Before running any of the notebooks, run the script `scripts/get_data.py` to retrieve the dataset:

```bash
python scripts/get_data.py
```

## Data
The dataset for this project is the [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset. Fashion-MNIST is a dataset of Zalando’s article images consisting of 60,000 training examples and 10,000 test examples. Each example comprises a 28×28 grayscale image and an associated label from one of 10 classes.

## Methods
The trained classifier is a simple neural network implemented in `PyTorch`. For more information on the model structure, refer to `models/README.md`

## License

<table >
<tbody>
  <tr>
    <td style="padding:0px;border-width:0px;vertical-align:center">
    Created by Simon Stone for Dartmouth College Library under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons CC BY-NC 4.0 License</a>.<br>For questions, comments, or improvements, email <a href="mailto:researchdatahelp@groups.dartmouth.edu">Research Data Services</a>.
    </td>
    <td style="padding:0 0 0 1em;border-width:0px;vertical-align:center"><img alt="Creative Commons License" src="https://i.creativecommons.org/l/by/4.0/88x31.png"/></td>
  </tr>
</tbody>
</table>

Except where otherwise noted, the example programs are made available under the OSI-approved MIT license.