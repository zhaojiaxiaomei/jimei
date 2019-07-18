import pandas as pd
import matplotlib.pyplot as plt
import wordcloud

f= open('new厦门金融招聘信息.csv')
data = pd.read_csv(f)
plt.rcParams['font.sans-serif'] = ['SimHei']

# 1.厦门不同区域薪酬比    思明区、湖里区、集美区、海沧区、同安区、翔安区   用到工作地点 和参考月薪
data['工作地点']=data['工作地点'].fillna('8888888888')
nulllist=data[data['工作地点']=='8888888888'].index.tolist()
print(nulllist)
newdata=data.drop(nulllist)
ql=[]
for i in ['思明区','湖里区','集美区','海沧区','同安区','翔安区']:
    qdf=newdata[newdata.工作地点.str.contains(i)]
    qxc=sum(qdf['参考月薪'])/len(qdf)
    ql.append([i,qxc])
plt.bar([i[0] for i in ql],[i[1] for i in ql],width=0.5)
plt.title('厦门不同区域薪酬比')
plt.show()


# 2.词云图统计金融行业主要招聘职位要求
l=list(data['岗位职责'].dropna().values)
l=''.join(l)
w=wordcloud.WordCloud(width=1000,height=700,background_color='white',font_path='msyh.ttc'
                      ,stopwords={"岗位职责","任职要求","工作职责","任职资格","岗位职责1","岗位要求","工作内容"})
w.generate(l)
w.to_file('岗位职责.png')

# 3.统计不同学历薪酬比
xl=data.学历要求.dropna().unique()
print(xl)
xlxcb=[]
for i in xl:
    df=data[data.学历要求==i]
    xlxc=sum(df['参考月薪'])/len(df)
    xlxcb.append([i,xlxc])
plt.bar([i[0] for i in xlxcb],[i[1] for i in xlxcb],width=0.5)
plt.title('统计不同学历薪酬比')
plt.show()
