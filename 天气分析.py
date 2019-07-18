import pandas as pd
import matplotlib.pyplot as plt

def ReadExcel():
    '''
    读取天气预报的文件
    :return:
    '''
    f= open('天气预报.csv',encoding='UTF-8')
    data = pd.read_csv(f)
    return data
def printZgd(data):
    '''
    使用dataframe的mean()函数计算最低最高气温的平均值并打印
    :param data:
    :return:
    '''
    print("最低气温平均值：%.2f，最高气温平均值：%.2f" % (data['最低气温'].mean(),data['最高气温'].mean()))


def printPlot(data):
    '''
    画每日天气的折线图
    :param data:
    :return:
    '''
    plt.rcParams['font.sans-serif'] = ['SimHei']
    newdata=pd.DataFrame(columns=['最高气温','最低气温'])
    for i in range(data.shape[0]):
        newdata.loc[i] = [data.iloc[i][1],data.iloc[i][2]]
    plt.plot([i for i in range(1,31)],[newdata.iloc[i][0] for i in range(30)],label='最高气温')
    plt.plot([i for i in range(1, 31)], [newdata.iloc[i][1] for i in range(30)],label='最低气温')
    plt.xticks([i for i in range(1,31)])
    plt.yticks([i for i in range(10,35)])
    plt.xlabel('4月份')
    plt.ylabel('温度')
    plt.legend()
    plt.title('2019年4月份厦门每日温度折线图')
    plt.show()


def printPie(data):
    '''
     饼状图 使用pandas的groupby方法
    :param data:
    :return:
    '''
    plt.rcParams['font.sans-serif'] = ['SimHei']
    tq=data.groupby(data['天气'])
    series=tq.size()
    series.plot.pie(autopct='%1.1f%%')
    plt.title('厦门2019年4月份各种天气饼状图')
    plt.ylabel('    ')
    plt.show()


def toCsv(data):
    '''
    使用pandas的groupby方法
    并将分组统计结果保存为文件'各类天气平均温度.csv'
    :param data:
    :return:
    '''
    newdata=data.groupby(['天气'])
    zg=round(newdata['最高气温'].mean())
    zd =round(newdata['最低气温'].mean())
    z=pd.DataFrame([zg,zd])
    for i in z.columns:
        z[i].to_csv(i+'天气平均温度.csv',index=False)

if __name__ == '__main__':
    data=ReadExcel()
    printZgd(data)
    printPlot(data)
    printPie(data)
    toCsv(data)