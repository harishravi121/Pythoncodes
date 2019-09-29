import datetime
import time
a=str(datetime.datetime.now().time())
t=((int(a[0:2:1]))*60)+int(a[3:5:1])

txt=open('timestamp.txt','r')

if int(a[0:2:1])==0 and int(a[3:5:1])<30:
    time.sleep(60*(30-int(a[3:5:1])))

b=str(txt.read())

txt.close()

if b[len(b)-2]=='P':
    t2=int(b[len(b)-8:len(b)-6:1])+int(b[len(b)-11:len(b)-9:1])*60+12*60
elif b[len(b)-2]=='A':
    t2=int(b[len(b)-8:len(b)-6:1])+int(b[len(b)-11:len(b)-9:1])*60
       
if ((t-t2)>40):
    print(1)
else:
    print(0)

