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


## Environment Setup


### Install Miniconda and activate conda:

Please have a look at these pages in case you don't have
a working conda installation already.

https://docs.conda.io/en/latest/miniconda.html

https://conda.io/projects/conda/en/latest/user-guide/install/index.html


### Install packages

Make sure to also have a look at the most recent
[Chemprop installation instructions](https://github.com/chemprop/chemprop#installation),
just in case the instructions here have become out-dated.
We are going to install it from PyPi.

Create a new environment for chemprop and activate it.

```
conda create -n chemprop python=3.8
conda activate chemprop
```

Make sure that the current pip is from the current environment.

```
which pip
```

Install Chemprop and other necessary packages.

```
conda install -c conda-forge rdkit
pip install git+https://github.com/bp-kelley/descriptastorus  
pip install chemprop
```

You should now be able to use Chemprop's CLI, with commands
starting with `chemprop_*`. (need to reboot the terminal? or
will they be available right away?)

From here, you should be able to start a Jupyter notebook session,
and start using Chemprop. In our case, however, we've had to also
install jupyter notebook within the current conda environment, so
that the `chemprop` python module would get discovered inside the
notebook.

For solving the problem with `import chemprop` within Jupyter notebooks,
the following steps will help.

```
conda install ipykernel  notebook
conda install -c conda-forge ipywidgets
jupyter notebook .
```

Test your installation by entering `import chemprop`.

Chemprop will show some warnings the first time it gets imported,
but we were unable to find any solutions to them, and they seemed
to be okay to ignore.


### Closing and deactivating the environment

```
jupyter notebook list
jupyter notebook stop <port number>
conda deactivate
```
