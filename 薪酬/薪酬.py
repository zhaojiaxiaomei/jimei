import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

df=pd.read_excel('大学生薪酬.xlsx')

# 1）不同年份薪酬前5名学校（柱状图）
for i in [2013,2015,2017]:
    plt.figure()
    ndf = df.sort_values(by=i,ascending=False).iloc[:5]
    plt.bar(ndf['university'], ndf[i], width=0.5)
    print(ndf[['university',i]])
    plt.title(str(i) + '年薪酬前5学校柱状图')
    plt.show()

# 2）不同年份薪酬平均值变化（折线图）
y17=df[2017].mean()
y15=df[2015].mean()
y13=df[2013].mean()
ydict={2013:y13,2015:y15,2017:y17}
print(ydict)
plt.plot([i for i in ydict.keys()],[i for i in ydict.values()])
plt.title('不同年份薪酬平均值变化折线图')
plt.show()

# 3）不同省份薪酬均值比较（柱状图）
prodict={}
provinces=df['province'].unique()
for province in provinces:
    pro_df=df[df.province==province]
    pro_mean=(pro_df[2013].mean()+pro_df[2015].mean()+pro_df[2017].mean())/3
    pro_mean=round(pro_mean,2)
    prodict[province]=pro_mean
print(prodict)
plt.plot([i for i in prodict.keys()],[i for i in prodict.values()])
plt.xticks(rotation=50)
plt.title('不同省份薪酬均值比较柱状图')
plt.show()