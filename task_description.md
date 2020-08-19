##数据来源
http://www.industrial-bigdata.com/Data  
进入到该网站的数据分析系统后，在我的数据-数据查看里面搜索Photovoltaic即可找到导出选项。

##数据描述
t: 时间变量  
TruePower：光伏电池功率  
AmbiTemp：环境温度  
Irradiance：辐照  
ModuleTemp：光伏模组温度  
InclAngle：倾斜角  
Current：电流  
Voltage：电压  
Humidity：湿度  

##任务描述
预测未来3天的光伏电池功率（每3小时一个预测值，共24个预测值）。其中使用前9个月的数据作为训练集，后3个月的数据作为测试集。

##特别说明
使用原始数据中的环境温度，人为构造未来3天的环境温度预报数据。

##处理后的数据说明
文件夹Processed_Data里面存放了处理好可以直接用来建模的数据，其中以train结尾的为训练集，以test结尾的是测试集。
起名为features的为原始数据中筛选后的特征数据，起名为target的是需要预测的值，起名为temperature prediction的是认为够早的温度预测数据。
需要注意的是最终比赛时只预测一次，即最终的任务只会基于已有的数据去预测未来7天的，这里稍有不同，不过不影响评判模型的质量。