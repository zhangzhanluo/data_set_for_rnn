import pandas as pd
from matplotlib import pyplot as plt

file_path = 'Raw Data/Dataset_Photovoltaic_power_prediction_PV_data_all_2020_08_18.csv'
raw_data = pd.read_csv(file_path, header=0, index_col=0, parse_dates=[0])

# 验证光伏电池功率=电压×电流
raw_data['PowerCal'] = raw_data.Current_V * raw_data.Voltage
power_data = raw_data[['TruePower', 'PowerCal']].copy()
power_data['20180301':'20180303'].plot()
plt.show()
# 结论：有一定的出入，但基本正确

# 查看光伏电池功率的周期性
raw_data.TruePower['20180801':'20180807'].plot()
plt.show()
# 结论：呈现明显的周期性

# 分析其他先关信息，例如功率与温度、辐照强度的关系，与历史数据的关系...
