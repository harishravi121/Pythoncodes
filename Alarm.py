import datetime
import time
import smtplib


while (1):

    print('Checking')



    a=str(datetime.datetime.now().time())
    t=((int(a[0:2:1]))*60)+int(a[3:5:1])

    txt=open('timestamp.txt','r')
    b=str(txt.read())

    txt.close()

    if b[len(b)-2]=='P':
        t2=int(b[len(b)-8:len(b)-6:1])+int(b[len(b)-11:len(b)-9:1])*60+12*60
    elif b[len(b)-2]=='A':
        t2=int(b[len(b)-8:len(b)-6:1])+int(b[len(b)-11:len(b)-9:1])*60
           
    if ((t-t2)>30):
        print('Experiment crashed go check')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("harish.ravishankar@gmail.com", "Bereal12")
        msg = "\nAlarm Labview Not Updating. Please go and check." # The /n separates the message from the headers (which we ignore for this example)
        server.sendmail("harish.ravishankar@gmail.com", "abhilashyd001@gmail.com", msg)

        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("harish.ravishankar@gmail.com", "Bereal12")
        msg = "\nAlarm Labview Not Updating. Please go and check." # The /n separates the message from the headers (which we ignore for this example)
        server.sendmail("harish.ravishankar@gmail.com", "harish.ravishankar@gmail.com", msg)
        print('Emails Sent')
        
        
    else:
        print('Running Fine')

    minsdel=30
    time.sleep(60*minsdel)
