# Commands used for obtaining our results

Please have a look at the [Chemprop documentation](https://chemprop.readthedocs.io/en/latest/) for details about these commands.

## Data

The data used are:
  -  For model training and validation: `data/article_training.csv`
  -  For predictions: `data/coco_test.csv`

## Training

Training using Chemprop's default settings, and `data/article_training.csv` as our data:

```
chemprop_train --data_path data/article_training.csv --dataset_type classification --save_dir article_checkpoints
```

## Hyperparameter optimization (for coco, n=20)

One first needs to make sure that there is a file available for the optimization script to save its results to.
The number of different models explored is sepecified through `--num_iters`.

```
# Create empty file for storing the hyperopt results
touch hyperopt_configs.json

# Run hyperopt
chemprop_hyperopt --data_path data/article_training.csv --dataset_type classification --num_iters 20 --config_save_path hyperopt_configs.json
```

## Prediction

The checkpointed model used is the same as the one from the training phase, but the data is now different: `data/coco_test.csv`.

```
chemprop_predict --test_path data/coco_test.csv --checkpoint_dir article_checkpoints --preds_path coco_preds.csv
```

## Interpretation

Model interprability: Understanding which chemical groups might be responsible for various properties.

```
chemprop_interpret --data_path <path> --checkpoint_dir <dir> --property_id 1
```
