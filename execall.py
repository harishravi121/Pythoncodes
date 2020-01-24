import os
strs=os.listdir()

for i in range(0,len(strs)):
    if(strs[i]!='execall.py') :
        exec(open(strs[i]).read())
    
