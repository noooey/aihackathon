# Train a model using AutoGluon

# Citation:
# Erickson, Nick, et al. "AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data." 
# arXiv preprint arXiv:2003.06505 (2020).

from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd
import os

<<<<<<< Updated upstream
train_df = pd.read_csv('2023_smartFarm_AI_hackathon_dataset.csv') # input for train dataset
=======
train_df = pd.read_csv('./2023_smartFarm_AI_hackathon_dataset.csv') # input for train dataset
>>>>>>> Stashed changes
# test_data = pd.read_csv('./test data location.csv')
train_data = TabularDataset(train_df)
time_limit = 3600 * 1 # hrs
label = 'HeatingEnergyUsage_cumsum'

# 'r2' for r2 score & 'root_mean_squared_error' for RMSE
eval_metric = 'accuracy' 
r2_metric = 'r2'
rmse_metric = 'root_mean_squared_error'

output_directory = './autogluon_model_logs' # output directory
predictor_directory = './autogluon_model_predict' # predictore directory

# autogluon train
predictor = TabularPredictor(
<<<<<<< Updated upstream
    label=label, eval_metric=rmse_metric
=======
    label=label, eval_metric=rmse_metic
>>>>>>> Stashed changes
).fit(
    train_data,
    presets='best_quality', 
    time_limit=time_limit, 
<<<<<<< Updated upstream
    ag_args_fit={'num_gpus': 0, 'num_cpus': 8},
=======
    ag_args_fit={'num_gpus': 0, 'num_cpus': 8}
>>>>>>> Stashed changes
    # training for a specific model ref: 'https://auto.gluon.ai/stable/api/autogluon.tabular.TabularPredictor.fit.html'
    hyperparameters={'GBM': {}},
    num_bag_folds=2,      
    num_stack_levels=2,
    )

# extra train
# additional_hyperparmeter = 'GBM'
# predictor.fit_extra(hyperparameters=additional_hyperparmeter)

### result (leaderboard)
leaderboard = predictor.leaderboard(silent=False)
print(leaderboard)

log_path = os.path.join(output_directory, 'train.log')
with open(log_path, 'w') as f:
    f.write(str(leaderboard))

print(f"Logs saved to {log_path}")

predictor.save(predictor_directory)

#model_to_use = predictor.get_model_best()
#model_pred = predictor.predict(test_data, model=model_to_use)
#model_pred.to_csv('./location to save result csv', index=False)
