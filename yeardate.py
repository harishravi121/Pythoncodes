import random

year1=random.randint(2013,2020)
year2=year1+random.randint(0,2)

month1=random.randint(1,8)
month2=month1+random.randint(0,1)
import pyperclip

handles=['moneycontrolcom','TiffanyATrump','taylorswift13','iitmadras','caltechalumni']
handle=random.choice(handles)
'''(from:moneycontrolcom) until:2020-07-23 since:2017-01-04'''

sent='(from:'+handle+') until:'+str(year2)+'-0'+str(month2)+'-01 since:'+str(year1)+'-0'+str(month1)+'-01'

print(sent)
pyperclip.copy(sent)
