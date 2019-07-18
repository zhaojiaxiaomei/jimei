import pandas as pd
import matplotlib.pyplot as plt
def read_excel():
    df=pd.read_excel("大学生薪酬.xlsx")
    return df


def nfbar(df):
    '''
    不同年份薪酬前5的柱状图
    :param df:
    :return:
    '''
    yeat13=df.sort_values(by=2013, ascending=False).iloc[:5]
    yeat15=df.sort_values(by=2015,ascending=False).iloc[:5]
    yeat17=df.sort_values(by=2017,ascending=False).iloc[:5]
    print(yeat13['university'],yeat13[2013])
    print(yeat15['university'],yeat15[2015])
    print(yeat17['university'],yeat17[2017])
    plt.figure()
    plt.bar(yeat13['university'],yeat13[2013],width=0.5)
    plt.title('2013年薪酬前5学校柱状图')
    plt.show()
    plt.figure()
    plt.bar(yeat15['university'], yeat15[2015], width=0.5)
    plt.title('2015年薪酬前5学校柱状图')
    plt.show()
    plt.figure()
    plt.bar(yeat17['university'], yeat17[2017], width=0.5)
    plt.title('2017年薪酬前5学校柱状图')
    plt.show()


def btbfplot(df):
    '''
    不同年份薪酬平均值变化折线图
    :param df:
    :return:
    '''
    n=df.shape[0]
    year13=round(sum(df[2013])/n,2)
    year15=round(sum(df[2015])/n,2)
    year17=round(sum(df[2017])/n,2)
    years=[2013,2015,2017]
    plt.figure()
    plt.plot(years,[year13,year15,year17])
    print(2013,year13)
    print(2015,year15)
    print(2017,year17)
    plt.title('不同年份薪酬平均值变化折线图')
    plt.show()


def probar(df):
    '''
    不同省份薪酬均值比较柱状图
    :return:
    '''
    provinces=set(df['province'])
    pro_jz=[]
    for pro in provinces:
        prodata=df[df.province==pro]
        n=prodata.shape[0]
        pros=sum(prodata[2013])+sum(prodata[2015]+sum(prodata[2017]))
        avg=round(pros/n/3,2)
        pro_jz.append([pro,avg])
    plt.figure()
    plt.bar([i[0] for i in pro_jz],[i[1] for i in pro_jz],width=0.3)
    plt.xticks(rotation=60)
    print(pro_jz)
    plt.title('不同省份薪酬均值比较柱状图')
    plt.show()


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df=read_excel()
    nfbar(df)
    btbfplot(df)
    probar(df)