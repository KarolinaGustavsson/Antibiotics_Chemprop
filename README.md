# Antibiotics_Chemprop

## Goal

### Getting an understanding for drug discovery using machine learning and getting experience using chemprop

## Datasets 

### Datasets can be found in the datasets folder: we used article_training for traning our model and assessing it, then we wanted to predict something novel — for that we used coco_test

### Article-traning is the traning dataset used in the article we used as inspiration for this project: https://www.sciencedirect.com/science/article/pii/S0092867420301021 

### Coco_test is smiles strings collected from a database of natural compunds by filtering for compunds with 0-5 carbons https://coconut.naturalproducts.net
### In order to get the data we want, as well as convert it from an sdf file into a csv we used the code in Converting_SDF_Files

## Training and Predicting

### At first we tried to make a notebook in colab, then deepnote and databricks: we had issues with installing conda inside of them. We should have tried to make a minimum viable product locally first. 

### In the end we did the project locally in the terminal 

### Code can be found in Terminal_Script
