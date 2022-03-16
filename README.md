# Antibiotic Discovery Using Graph Deep Learning

## Goal

Getting an understanding of drug discovery using machine learning and getting experience using [Chemprop](https://chemprop.readthedocs.io/en/latest/).
Chemprop is a tool which allows for modeling of molecules using message passing graph neural networks.

This is done as the final project in the course [ID2223 Scalable Machine Learning and Deep Learning](https://id2223kth.github.io) at [KTH](https://kth.se).

## Data

The datasets used in this project are available in the `data` folder. We used `article_training.csv` for training our model and assessing it. And then used the obtained model in order to predict novel antibiotic candidates using the `coco_test.csv` dataset.

Our training dataset comes from the article which we used as inspiration for this project: [A Deep Learning Approach to Antibiotic Discovery](https://www.sciencedirect.com/science/article/pii/S0092867420301021).

Our dataset used for predictions consists of SMILES strings collected from [COCONUT](https://coconut.naturalproducts.net), a database of natural compounds, by filtering for compounds with 0-5 carbons. Our conversion script `sdf_to_csv.py` is then used in order to convert the COCONUT data from SDF to CSV.

## Training and Prediction

At first, we tried to make a notebook in Google Colab, then DeepNote and Databricks:, but we faced severe issues while trying to install and/or use Miniconda on them. We should have tried to make a minimum viable product first, locally. In the end, we decided to do the project locally, using the terminal and Jupyter Notebooks.

## Report

The project report, along with a list of our antibiotic candidates, is available in PDF format in this repository.

## Reproducibility

The commands that we ran in order to obtain our results can be found in the `commands.md` file.
