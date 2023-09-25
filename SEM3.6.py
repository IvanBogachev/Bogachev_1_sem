def mnk(x, y):
    if len(x)!=len(y):
        return None
    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    numerator=0
    denominator=0
    for i in range(len(x)):
        xymean+=x[i]*y[i]
        sqmean+=x[i]**2
    a=(xymean/len(x))/(sqmean/len(x)-x_mean**2)
    b=y_mean-a*x_mean
    return a, b
x=list(map(float, input().split()))
y=list(map(float, input().split()))
a, b=mnk(x, y)
print(a,b)