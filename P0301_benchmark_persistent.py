import math
import pandas as pd
from sklearn.metrics import mean_squared_error

features_train_path = 'Processed Data/ features train.csv'
features_test_path = 'Processed Data/ features test.csv'
features_train = pd.read_csv(features_train_path, header=0, index_col=0, parse_dates=[0])
features_test = pd.read_csv(features_test_path, header=0, index_col=0, parse_dates=[0])

target_test_path = 'Processed Data/ target test.csv'
target_test = pd.read_csv(target_test_path, header=0, index_col=0, parse_dates=[0])

# 使用持续法建立基准模型。此处使用同时刻的功率值作为预测值。例如使用1号3点的值作为2/3/4号3点值得预测。
features_data = pd.concat([features_train, features_test], axis=0)
prediction_data = features_data.loc[:, ['TruePower']]
for i in range(3):
    for j in range(8):
        prediction_data['TruePower(+{})'.format(i*24+(j+1)*3)] = prediction_data['TruePower'].shift(7-j)
prediction_data.drop(['TruePower'], axis=1, inplace=True)
target_prediction = prediction_data.reindex(target_test.index)

# 评估模型
rmse = math.sqrt(mean_squared_error(target_test, target_prediction))
print('持续法建立的模型，其预测结果rmse为{:.2f}'.format(rmse))
