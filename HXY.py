import numpy as np
x1=np.arange(-100,100)
y11=np.ones(200)*-3
y12=np.ones(200)*-2
y13=np.ones(200)*-1
y14=np.ones(200)*0
y15=np.ones(200)*1
y16=np.ones(200)*2
y17=np.ones(200)*2


x11=np.ones(200)*-3-40
x12=np.ones(200)*-2-40
x13=np.ones(200)*-1-40
x14=np.ones(200)*0-40
x15=np.ones(200)*1-40
x16=np.ones(200)*2-40
x17=np.ones(200)*3-40

y=np.arange(-100,100)

x21=np.ones(200)*-3+40
x22=np.ones(200)*-2+40
x23=np.ones(200)*-1+40
x24=np.ones(200)*0+40
x25=np.ones(200)*1+40
x26=np.ones(200)*2+40
x27=np.ones(200)*3+40



x=[*x1,*x1,*x1,*x1,*x1,*x1,*x1,*x11,*x12,*x13,*x14,*x15,*x16,*x17,*x21,*x22,*x23,*x24,*x25,*x26,*x27]
y=[*y11,*y12,*y13,*y14,*y15,*y16,*y17,*y,*y,*y,*y,*y,*y,*y,*y,*y,*y,*y,*y,*y,*y]

thefile = open('x.txt', 'w')
for item in x:
  thefile.write("%s," % item)

thefile = open('y.txt', 'w')
for item in y:
  thefile.write("%s," % item)
