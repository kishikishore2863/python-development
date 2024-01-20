from sympy import *
var('t,i,j,k')
f=t*i-t**2;f3=sin(t)*k
f1=t;f2=-t**2;f3=sin(t)
df=diff(f1,t)*i+diff(f2,t)*j+diff(f3,t)*k
df=df.subs(t,0)
df2=diff(f1,t,2)*i+diff(f2,t,2)*j+diff(f3,t,2)*k
df2=df2.subs(t,0)
print("df=",df,"\ndf2",df2)