import math,numpy
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
#在这里把x,y数据改了
x=[0,1,2,3,4,5,6,7,8,9]
y=[20.630,29.665,	38.620	,47.513	,56.371	,65.118,	73.613,	82.430	,91.219	,100.001]
#y=[30.432,	34.892	,39.242,	43.609,	48.290	,52.513,	56.893,	61.252	,65.750,	70.153]
#y=[6.96	,6.48,	6.24,	6.08,	5.76,	5.28,	4.88	,4.48,	4.16	,3.68]

n=1#n是你要拟合几次方函数
z1 = polyfit(x, y, n)
line=[]
for i in range(n+1):
    line.append(z1['polynomial'][i])
#line=[,z1['polynomial'][1]]#line是一个保存由n次到0次系数的列表
print('回归曲线的信息',line)#

sum=0

for i in range(len(x)):
    h=0
    for j in range(len(line)):#line列表的长度=n+1
        h=h+line[j]*pow(x[i],(len(line)-j-1))#根据拟合曲线算出来的那个值


    sum=sum+(y[i]-h)*(y[i]-h)#算剩余方差
result=sum/(len(x)-2) #剩余方差
print("剩余方差是",result);
def average(x):#平均值
    sum2=0
    for i in x:
        sum2=sum2+i
    return  sum2/len(x)
sum3=0
for i in x:
    sum3=sum3+(i-average(x))*(i-average(x))
print(sum3)
print(average(x))
#for i in y:
xigema_a1= math.sqrt(result / sum3)#这是斜率的不确定度
print("斜率的不确定度是",xigema_a1)#是给一次式算的，高次勿用
