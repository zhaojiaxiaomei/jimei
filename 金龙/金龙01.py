import pandas as pd
import matplotlib.pyplot as plt



# 读取数据并将日期列作为index
df=pd.read_excel('金龙汽车历史行情.xlsx',index_col='日期',parse_dates=True)


# 1.计算2016-2019每年股价平均涨幅、成交量、收盘价，
pzf=df['涨跌幅'].resample('A').mean()
print(pzf)
pcjl=df['成交量'].resample('A').mean()
print(pcjl)
pspj=df['收盘价'].resample('A').mean()
print(pspj)

# 2.分别绘制2019、2018、2017年每月平均收盘价、最低价、成交量、涨跌幅折线图。
plt.rcParams['font.sans-serif'] = ['SimHei']
for year in ['2019','2018','2017']:
    spdf=df[year]['收盘价'].resample('M').mean()
    zddf=df[year]['最低价'].resample('M').mean()
    cjdf=df[year]['成交量'].resample('M').mean()
    zdfdf=df[year]['涨跌幅'].resample('M').mean()
    plt.figure()
    spdf.plot()
    plt.title(year+'每月平均收盘价')
    plt.show()
    plt.figure()
    spdf.plot()
    plt.title(year + '每月平均最低价')
    plt.show()
    plt.figure()
    spdf.plot()
    plt.title(year + '每月平均成交量')
    plt.show()
    plt.figure()
    spdf.plot()
    plt.title(year + '每月平均涨跌幅')
    plt.show()

# 3.对股票走势做个结论分析