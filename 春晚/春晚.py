import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1.读文件
data=pd.read_excel('春晚节目单.xlsx')
print(data.iloc[0])

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 2.分析每年节目数量变化
datayear=data.groupby('year')
plt.figure()
year=list(datayear.size().index)
values=list(datayear.size().values)
print(values)
plt.bar(year,values)
for i in range(len(year)):
    plt.text(year[i]-0.2,values[i]+0.2,values[i])
plt.xticks(datayear.size().index,rotation=60)
plt.title('春晚每年节目数量变化')
plt.show()

# 3.分析歌曲、小品、相声类节目数量对比
gqdf = data[data['category'].str.contains("歌曲")]
xpdf = data[data['category'].str.contains("小品")]
xsdf = data[data['category'].str.contains("相声")]
gqnum=gqdf.shape[0]
xpnum=xpdf.shape[0]
xsnum=xsdf.shape[0]
l=[['歌曲',gqnum],['小品',xpnum],['相声',xsnum]]
plt.figure()
plt.pie([i[1] for i in l],labels=[i[0]+str(i[1]) for i in l],autopct='%1.1f%%')
plt.title('春晚歌曲、小品、相声类节目数量对比饼状图')
plt.show()

# 4.分析演员出现次数前5名的明星
yyList=[]
for i in data['actor'].values:
    if isinstance(i, float):
        continue
    else:
        if '、' in i:
            r=i.split('、')
            for j in r:
                yyList.append(j)
        else:
            yyList.append(i)
print(yyList)
l=np.array(yyList)
ls=list(set(l))
newList=[]
for i in ls:
    newList.append([i,np.sum(l==i)])


def takeSecond(elem):
    return elem[1]


newList.sort(key=takeSecond,reverse=True)
print(newList)
# 找出前10个
kq=newList[:10]
newkq=[]
print(kq)
for i in range(10):
    n=0
    for j in yyList:
        if kq[i][0] in j:
            n+=1
    newkq.append([kq[i][0],n])
newkq.sort(key=takeSecond,reverse=True)
print(newkq)
l=newkq[:5]
print(l)

