import numpy
import math
a = int(input('Введите значение А: '))
b = int(input('Введите значение B: '))
c = int(input('Введите значение C: '))
d = int(input('Введите значение D: '))
a=a/a
b=b/a
c=c/a
d=d/a
Q=(b**2-3*c)/9
R=((2*b**3)-(9*b*c)+(27*d))/54
S=(Q**3)-(R**2)
if R**2<Q**3:
    t=math.acos(R/math.sqrt(Q**3))/3
    x1=-2*math.sqrt(Q)*math.cos(t)-b/3
    x2=-2*math.sqrt(Q)*math.cos(t+(2*math.pi/3))-b/3
    x3=-2*math.sqrt(Q)*math.cos(t-(2*math.pi/3))-b/3
    print(round(x1))
    print(round(x2))
    print(round(x3))
elif R**2>=Q**3:  
    r=abs(R)
    A=-numpy.sinh(R)*(r+math.sqrt(R**2-Q**3))**1/3
    if A!=0:
        B=Q/A
        x1=(A+B)-a/3
        print(round(x1))
    else:
        B=0
        x1=(A+B)-b/3
        print(round(x1))
        x2=-A-a/3
        print(x2)




# if S>0:
#     f=cmath.acos(R/Q**(3/2))/3
#     x1=-2*(Q**(1/2))*cmath.cos(f)-a/3
#     x2=-2*(Q**(1/2))*cmath.cos(f+2*((cmath.pi)/3)) - a/3
#     x3=-2*(Q**(1/2))*cmath.cos(f-2*((cmath.pi)/3)) - a/3
#     print(x1)
#     print(x2)
#     print(x3)
# elif S<0:
#         m=abs(Q)
#         n=abs(R)
#         f=(cmath.acosh(n/m**(3/2)))/3
#         x1=(-2*R*m**(1/2)*cmath.cosh(f)-a/3)
#         print(x1)
# elif S==0:
#     x1=-2*R**(1/3)-a/3
#     x2=x3=R**1/3-a/3
#     print(x1)
#     print(x2=x3)
