import pandas as pd
import matplotlib.pyplot as plt
import wordcloud
import re


def readExcel():
    data = pd.read_excel('厦门金融招聘信息.xlsx')
    return data


def cleanData(data):
    '''
    取6000-10000(底薪：3000-3500+提成)中最低值6000作为参考月薪
    :param data:
    :return:
    '''
    nulllist=[]
    for i in range(data.shape[0]):
        pattern = re.compile('[0-9]+')
        match=pattern.findall(str(data.iloc[i][3]))
        if match:
            if '-' in str(data.iloc[i][3]):
                pass
            else:
                nulllist.append(i)
        else:
            nulllist.append(i)
    newdata=data.drop(nulllist)
    newdata['参考月薪']=newdata['参考月薪'].str.split('-').map(lambda x:x[0]).astype('int32')
    return newdata


def xcb(data):
    '''
    厦门不同区域薪酬比
    :param data:
    :return:
    '''
    data['工作地点'] = data['工作地点'].fillna('xxxxxxxxxxxxxx')
    nulllist = data[data['工作地点'] == 'xxxxxxxxxxxxxx'].index.tolist()
    print(nulllist)
    newdata = data.drop(nulllist)
    ql = []
    xmql=['思明区', '湖里区', '集美区', '海沧区', '同安区', '翔安区']
    for i in xmql:
        qdf = newdata[newdata.工作地点.str.contains(i)]
        qxc = sum(qdf['参考月薪']) / len(qdf)
        ql.append([i, qxc])
    plt.barh([i[0] for i in ql], [i[1] for i in ql], height=0.5)
    plt.title('厦门不同区域薪酬比')
    plt.show()


def cy(data):
    '''
    词云图
    :param data: 未经过清洗的dataframe
    :return:
    '''
    gw=list(data['岗位职责'].dropna().values)
    gwstr=''.join(gw)
    stopwords={"岗位职责","任职要求","工作职责","任职资格","岗位职责1","岗位要求","工作内容"}
    w=wordcloud.WordCloud(width=700,height=1000,background_color='white',font_path='msyh.ttc',stopwords=stopwords)
    w.generate(gwstr)
    w.to_file('职责.jpg')


def xlxcb(data):
    '''
    不同学历薪酬比
    :param data: 经过清洗的dataframe
    :return:
    '''
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


if __name__ == '__main__':
    data=readExcel()
    ndata=cleanData(data)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    xcb(ndata)
    cy(data)
    xlxcb(ndata)