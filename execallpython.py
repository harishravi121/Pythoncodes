import os
strs=['taper.py', 'H orbital radius.py', 'Taylorhome.py', 'Calculator_1.py', 'brainshag.py', 'ab.py', 'Calculator_0.py', '2by2cube_dir.py', 'Circle.py', 'sort1.py',  "Stirling's approximation.py",  'Calculator_Gamma.py', 'tapershag.py', '2by2cube_1.py', 'HXY.py',  'Pi2.py', 'start.py',  '2by2cube.py', '2by2cube_2.py', 'brain.py', 'hi.py', 'Calculator2.py', 'Lorentzian.py', 'Solar.py',  'Glucoseandaminoacid.py',  'Taylorhome2.py']
for i in range(0,len(strs)):
    print(strs[i])
    exec(open(strs[i]).read())
        
    
