import pandas as pd

file_path = 'Raw Data/Dataset_Photovoltaic_power_prediction_PV_data_all_2020_08_18.csv'
raw_data = pd.read_csv(file_path, header=0, index_col=0, parse_dates=[0])

# 对数据进行3小时平均操作，将数据记录在中心点，例如6点的数据指的是4:30-7:30这段时间所有数据的平均值
averaged_hour = 3
frequency_min = 10
key_data = raw_data.loc[:, ['TruePower', 'AmbiTemp', 'Irradiance', 'ModuleTemp']]
key_data_rolling = key_data.rolling(window=int(averaged_hour * 60 / frequency_min), center=True).mean()

# 根据实际温度记录，构造温度预报数据
temperature_data = key_data_rolling[['AmbiTemp']].copy()
for i in range(24):
    temperature_data['AmbiTemp(+{})'.format(3 * (i + 1))] = temperature_data['AmbiTemp'].shift(
        (-i - 1) * int((averaged_hour * 60 / frequency_min)))

# 构造目标真实值
target = key_data_rolling[['TruePower']].copy()
for i in range(24):
    target['TruePower(+{})'.format(3 * (i + 1))] = target['TruePower'].shift(
        (-i - 1) * int((averaged_hour * 60 / frequency_min)))
target.drop('TruePower', axis=1, inplace=True)

# 训练集使用1-9月份的数据，测试集使用10-12月份数据，注意到所有数据的开始和末尾会存在nan值，尤其是预测目标需要有预测的真实值，因此去掉前后三天。
train_index = pd.date_range(start='20180104', end='20180930', freq='3h')
test_index = pd.date_range(start='20181001', end='20181228', freq='3h')
key_data_train = key_data_rolling.reindex(train_index)
key_data_test = key_data_rolling.reindex(test_index)
temperature_prediction_train = temperature_data.reindex(train_index)
temperature_prediction_test = temperature_data.reindex(test_index)
target_train = target.reindex(train_index)
target_test = target.reindex(test_index)

# 保存数据
target_train.to_csv('Processed Data/ target train.csv', encoding='utf-8-sig')
target_test.to_csv('Processed Data/ target test.csv', encoding='utf-8-sig')
key_data_train.to_csv('Processed Data/ features train.csv', encoding='utf-8-sig')
key_data_test.to_csv('Processed Data/ features test.csv', encoding='utf-8-sig')
temperature_prediction_train.to_csv('Processed Data/ temperature prediction train.csv',
                                    encoding='utf-8-sig')
temperature_prediction_test.to_csv('Processed Data/ temperature prediction test.csv',
                                   encoding='utf-8-sig')
