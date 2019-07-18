# 1.分析每年不同班级平均成绩情况
# 2.不同年份总体平均成绩情况
# 3.不同性别学生成绩情况
import pandas as pd
import matplotlib.pyplot as plt
df_dict=pd.read_excel('课程成绩.xlsx',None)
plt.rcParams['font.sans-serif'] = ['SimHei']


for key in df_dict.keys():
    df_key=df_dict[key]
    df_key['总评']=df_key['总评'].replace('缺考\xa0',0).astype('int32')
    df_dict[key]=df_key


# 1.分析每年不同班级平均成绩情况
for key in df_dict.keys():
    mean=df_dict[key].groupby('班级')['总评'].mean()
    mean.plot(kind='bar')
    plt.title(key+'年不同班级平均成绩情况')
    plt.show()

# 2.不同年份总体平均成绩情况
mean_list=[]
for key in df_dict.keys():
    mean=df_dict[key]['总评'].mean()
    mean_list.append([key,mean])
print(mean_list)
plt.bar([i[0] for i in mean_list],[i[1] for i in mean_list],width=0.3)
plt.title('不同年份总体平均成绩情况柱状图')
plt.show()

# 3.不同性别学生成绩情况
dfz=pd.DataFrame()
for v in df_dict.values():
    dfz=pd.concat([dfz, v], axis=0, ignore_index=True)
mean=dfz.groupby('性别')['总评'].mean()
print(mean)
mean.plot(kind='bar')
plt.title('不同性别学生成绩情况')
plt.show()