import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_excel("大学生薪酬.xlsx")
print(data.iloc[0])
plt.rcParams['font.sans-serif'] = ['SimHei']
# 不同年份薪酬前5的柱状图
for i in [2013,2015,2017]:
    plt.figure()
    ysn = data.sort_values(by=i, ascending=False).iloc[:5]
    plt.bar(ysn['university'], ysn[i], width=0.5)
    print(ysn['university'],ysn[i])
    plt.title(str(i)+'年薪酬前5学校柱状图')
    plt.show()


#不同年份薪酬平均值变化折线图
n=data.shape[0]
ys=round(sum(data[2013])/n,2)
yw=round(sum(data[2015])/n,2)
yq=round(sum(data[2017])/n,2)
print(ys,yw,yq)
nf=[2013,2015,2017]
jz=[ys,yw,yq]
plt.figure()
plt.plot([i for i in nf],[i for i in jz])
plt.title('不同年份薪酬平均值变化折线图')
for i in range(3):
    plt.text(nf[i],jz[i],jz[i])
plt.show()

# 不同省份薪酬均值比较柱状图
pros=data['province'].unique()
pro_jz=[]
for pro in pros:
    prodata=data[data.province==pro]
    n=prodata.shape[0]
    pros=sum(prodata[2013])+sum(prodata[2015]+sum(prodata[2017]))
    jz=round(pros/n/3,2)
    pro_jz.append([pro,jz])
print(pro_jz)
plt.figure()
plt.barh([i[0] for i in pro_jz],[i[1] for i in pro_jz], height=0.3)
plt.title('不同省份薪酬均值比较柱状图')
plt.show()
