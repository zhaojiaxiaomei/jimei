import pandas as pd
import matplotlib.pyplot as plt


def readFile():
    f = open('测试成绩统计.csv')
    df = pd.read_csv(f,dtype={'学号': str})
    return df


def calAvg(df):
    newdf=pd.DataFrame(columns=['学号','平均成绩'])
    stuavglist=[]
    for i in range(df.shape[0]):
        sum=0
        for j in range(1, 10):
            sum=sum+df.iloc[i][j]
        avg=round(sum/9,2)
        # newdf=pd.concat([],ignore_index = True)
        newdf.loc[i] = [df.iloc[i][0],avg]
        stuavglist.append([str(df.iloc[i][0]),avg])
    return stuavglist,newdf


def divideAvg(stuavglist):
    divideavglist=[['60分以下',0],['60-70',0],['70-80',0],['80-90',0],['90分以上',0]]
    for stuavg in stuavglist:
        if stuavg[1]<60:
            divideavglist[0][1]+=1
        elif stuavg[1]>=60 and stuavg[1]<70:
            divideavglist[1][1] += 1
        elif stuavg[1]>=70 and stuavg[1]<80:
            divideavglist[2][1] += 1
        elif stuavg[1]>=80 and stuavg[1]<90:
            divideavglist[3][1] += 1
        else:
            divideavglist[4][1] += 1
    return divideavglist


def printAvgbar(divideavglist):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.bar([i for i in range(5)], [i[1] for i in divideavglist], width=0.3)
    for i in range(5):
        plt.text(i-0.1,divideavglist[i][1]+0.3,divideavglist[i][1])
    plt.xticks([i for i in range(5)], [i[0] for i in divideavglist], rotation=30)
    plt.title('各个分数段人数条形图')
    plt.ylabel('人数')
    plt.xlabel('分数段')
    plt.show()


def toCsv(df):
    df.to_csv("成绩平均分.csv",index=False)



if __name__ == '__main__':
    df=readFile()
    stuavglist=calAvg(df)
    divideavglist=divideAvg(stuavglist[0])
    printAvgbar(divideavglist)
    toCsv(stuavglist[1])



