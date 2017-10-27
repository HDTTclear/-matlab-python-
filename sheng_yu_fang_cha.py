import math,numpy
def average(x):#平均值
    sum2=0
    for i in x:
        sum2=sum2+i
    return  sum2/len(x)
def RSS(a_list_x,a_list_y,a_line):#求RSS
    sum=0
    for i in range(len(a_list_x)):
        h = 0
        for j in range(len(a_line)):  # line列表的长度=n+1
            h = h + a_line[j] * pow(a_list_x[i], (len(a_line) - j - 1))  # 根据拟合曲线算出来的那个值

        sum = sum + (a_list_y[i] - h) * (a_list_y[i] - h)# 算剩余方差
    return sum
def TSS(a_list):#求TSS
    sum3=0
    for i in a_list:
        sum3 = sum3 + (i - average(a_list)) * (i - average(a_list))
    return sum3
def Mod_eff(rss,tss):
    return (1 - (rss / tss))

def polyfit(x, y, degree):#线性回归代码
    results = {}
    coeffs = numpy.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()
# r-squared
    p = numpy.poly1d(coeffs)
# fit values, and mean
    yhat = p(x)# or [p(z) for z in x]
    ybar = numpy.sum(y)/len(y)# or sum(y)/len(y)
    ssreg = numpy.sum((yhat-ybar)**2)# or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)# or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot #准确率

    return results#使用方式：返回值是一个集合，包括'polynomial'，是一个含有斜率和截距的列表 'determination'是置信度
def nihe_fun(list_x,list_y,n,bx,by):# x,y是两个列表，x默认作为横坐标n是你要拟合几次方函数
    z1 = polyfit(list_x, list_y, n)
    a_line = []
    for i in range(n + 1):
        a_line.append(z1['polynomial'][i])
    rss=RSS(list_x, list_y, a_line)
    tss=TSS(list_y)
    Mod_Eff=Mod_eff(rss,tss)
    if bx==[] or by==[]:
        return [n,a_line,rss,tss,Mod_Eff]
    else:
        rss2 = RSS(bx, by, a_line)
        tss2 = TSS(by)
        Mod_Eff_pg = Mod_eff(rss2, tss2)
        return [n,a_line,rss,tss,Mod_Eff,Mod_Eff_pg]

x=[30.432	,34.892	,39.242	,43.609,	48.290,	52.513	,56.893	,61.252,	65.750	,70.153]
y=[6.96,	6.48	,6.24,	6.08	,5.76,	5.28	,4.88	,4.48,	4.16	,3.68]

bx=[30.718 ,34.732 ,39.215 ,43.549 ,48.220,52.350,56.868,61.281,65.665,70.139]
by=[6.96,6.48,6.24,6,5.52,5.28,4.96,4.48,4.08,3.68]
for i in range(11):
    print(nihe_fun(x,y,i,bx,by))
    #print()
