# Fantasy-Premier-League-Predictive-Intelligence-Pipeline
Fantasy Premier League (FPL) player performance forecasting pipeline with time-series validation and multi-model benchmarking.

(This file and the overall project is a work in progress, the contents are subject to change).
-Integrate tools to get data up to the current day and process it so that current data is available not just the data added to vaastav's directory.
-(Maybe) expand dataset to include years before 2025 with no NaN values.
-Evaluate model interpretability and expandability.

The data used in this project can be found at: 'https://github.com/vaastav/Fantasy-Premier-League/tree/master/data/2025-26'

Results (temp):
                 Model                                             Params    RMSE     MAE
0         XGB_LinearDF  {'n_estimators': 500, 'learning_rate': 0.03, '...  1.8799  0.9299
1  ExtraTrees_LinearDF  {'n_estimators': 300, 'max_depth': 10, 'min_sa...  1.8861  0.9516
2    MLP_Tabular_Small  {'hidden_layer_sizes': (64, 32), 'activation':...  1.8959  0.9616
3    Ridge_Alpha_100.0                                   {'alpha': 100.0}  1.9012  0.9878
4     Ridge_Alpha_10.0                                    {'alpha': 10.0}  1.9036  0.9908
5      Ridge_Alpha_1.0                                     {'alpha': 1.0}  1.9042  0.9915
6  ElasticNet_Balanced  {'alpha': 0.1, 'l1_ratio': 0.5, 'max_iter': 20...  1.9112  1.0203

          Model                                             Params    RMSE     MAE
0    XGB_TreeDF  {'n_estimators': 500, 'learning_rate': 0.03, '...  1.9226  0.9485
1     LGBM_Deep  {'max_depth': 6, 'learning_rate': 0.05, 'rando...  1.9251  0.9483
2  LGBM_Shallow  {'max_depth': 3, 'learning_rate': 0.05, 'rando...  1.9322  0.9607

