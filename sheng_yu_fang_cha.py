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

y=[104.267	,95.350	,86.570	,77.978,	69.208	,60.480	,51.805	,42.969	,34.032,	25.152]
x=[0,1,2,3,4,5,6,7,8,9]
z1 = polyfit(x, y, 1)
line=[z1['polynomial'][0],z1['polynomial'][1]]#line是一个保存斜率和截距的列表
print('回归曲线的斜率和截距',line)#

sum=0
for i in range(len(x)):
    sum=sum+(y[i]-line[1]-line[0]*x[i])*(y[i]-line[1]-line[0]*x[i])
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
print("斜率的不确定度是",xigema_a1)