import pandas as pd
import matplotlib.pyplot as plt
years={}
dfDict=pd.read_excel('大学学术排名.xlsx',None)
plt.rcParams['font.sans-serif'] = ['SimHei']
print(dfDict['2009'].iloc[0])
# 1.列出不同年份美国(USA)、中国(China)、日本(Japan)、德国(Germany)、加拿大(Canada) 5个国家平均成绩（柱状图）
for i in range(2009,2019):
    year=str(i)
    df=dfDict[year]
    gjs=[]
    df['country']=df['country'].str.replace('UnitedStates','USA')
    for gj in ['USA','China','Japan','Germany','Canada']:
        gjdf=df[df['country'].str.contains(gj)]
        if len(gjdf)==0:
            gjs.append([gj,0])
        else:
            gjavg=sum(gjdf['index_rank'])/len(gjdf)
            gjs.append([gj,gjavg])
    plt.bar([i[0] for i in gjs],[i[1] for i in gjs],width=0.5)
    plt.title(year + '年5个国家平均成绩柱状图')
    plt.show()

# 2.列出中国2018年排名前10名的大学
df2018_ch=dfDict['2018'][dfDict['2018']['country']=='China']
ch_10 = df2018_ch.sort_values(by='index_rank').iloc[:10]
print(ch_10.loc[:, ('university', 'index_rank')])

# 找出5个感兴趣的大学画出2016-2018年排名变化折线图
# 清华大学    北京大学      浙江大学    哈佛大学       斯坦福大学
df2016=dfDict['2016']
df2017=dfDict['2017']
df2018=dfDict['2018']
qhs=[]
qhs.append(df2016[df2016['university']=='清华大学'].iloc[0,3])
qhs.append(df2017[df2017['university']=='清华大学'].iloc[0,3])
qhs.append(df2018[df2018['university']=='清华大学'].iloc[0,3])
plt.plot(['2016','2017','2018'],qhs,label='清华大学')
bjs=[]
bjs.append(df2016[df2016['university']=='北京大学'].iloc[0,3])
bjs.append(df2017[df2017['university']=='北京大学'].iloc[0,3])
bjs.append(df2018[df2018['university']=='北京大学'].iloc[0,3])
plt.plot(['2016','2017','2018'],bjs,label='北京大学')
zjs=[]
zjs.append(df2016[df2016['university']=='浙江大学'].iloc[0,3])
zjs.append(df2017[df2017['university']=='浙江大学'].iloc[0,3])
zjs.append(df2018[df2018['university']=='浙江大学'].iloc[0,3])
plt.plot(['2016','2017','2018'],zjs,label='浙江大学')
hfs=[]
hfs.append(df2016[df2016['university']=='哈佛大学'].iloc[0,3])
hfs.append(df2017[df2017['university']=='哈佛大学'].iloc[0,3])
hfs.append(df2018[df2018['university']=='哈佛大学'].iloc[0,3])
plt.plot(['2016','2017','2018'],hfs,label='哈佛大学')
stfs=[]
stfs.append(df2016[df2016['university']=='斯坦福大学'].iloc[0,3])
stfs.append(df2017[df2017['university']=='斯坦福大学'].iloc[0,3])
stfs.append(df2018[df2018['university']=='斯坦福大学'].iloc[0,3])
plt.plot(['2016','2017','2018'],stfs,label='斯坦福大学')
plt.legend()
plt.title('感兴趣的5所大学2016-2018排名折线图')
plt.show()