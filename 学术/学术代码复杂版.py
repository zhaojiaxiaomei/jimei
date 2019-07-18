import pandas as pd
import matplotlib.pyplot as plt

def readExcel():
    dataDict=pd.read_excel('大学学术排名.xlsx',None)
    return dataDict

def dif_country_cj(dataDict):
    '''
    1.列出不同年份美国(USA)、中国(China)、日本(Japan)、德国(Germany)、加拿大(Canada) 5个国家平均成绩（柱状图）
    :param dataDict:
    :return:
    '''
    for i in range(2009,2019):
        year=str(i)
        df=dataDict[year]
        coun_dict={}
        df['country']=df['country'].str.replace('UnitedStates','USA')
        for country in ['USA','China','Japan','Germany','Canada']:
            coudf=df[df['country'].str.contains(country)]
            coun_dict[country]=coudf['index_rank'].mean()
        plt.bar(coun_dict.keys(),coun_dict.values(),width=0.5)
        plt.title(year + '年5个国家平均成绩柱状图')
        plt.show()


def top_china(dataDict):
    '''
    列出中国2018年排名前10名的大学
    :return:
    '''
    df2018=dataDict['2018']
    df_ch=df2018[df2018.country=='China']
    ch_10 = df_ch.sort_values(by='index_rank').iloc[:10]
    print(ch_10[['university', 'index_rank']])


def far_uni(dataDict):
    '''
    找出5个感兴趣的大学画出2016-2018年排名变化折线图
    哈佛大学 斯坦福大学 剑桥大学 麻省理工学院 牛津大学
    :param dfDict:
    :return:
    '''
    df2016=dataDict['2016']
    df2017=dataDict['2017']
    df2018=dataDict['2018']
    for dx in ['哈佛大学','斯坦福大学','剑桥大学','麻省理工学院','牛津大学']:
        y6=df2016[df2016['university']==dx].iloc[0,3]
        y7=df2017[df2017['university']==dx].iloc[0,3]
        y8=df2018[df2018['university']==dx].iloc[0,3]
        plt.plot(['2016', '2017', '2018'], [y6,y7,y8], label=dx)
    plt.legend()
    plt.title('感兴趣的5所大学2016-2018排名折线图')
    plt.show()


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dataDict=readExcel()
    dif_country_cj(dataDict)
    top_china(dataDict)
    far_uni(dataDict)