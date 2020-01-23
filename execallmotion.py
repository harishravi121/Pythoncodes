import os
strs=['straightball.py', 'hitball.py', 'nukehitball.py', '2Dswingwithbat.py', '2Dswing.py']
for i in range(0,len(strs)):
    if((strs[i]!='execall.py')&(strs[i]!='execphysics.py')) :
        print(strs[i])
        exec(open(strs[i]).read())
        
    
