import subprocess
import random

C=['4','C','R','S','T','To']
a="START .\\"+random.choice(C)+'.lnk'
print(a)

subprocess.run(a,shell=True)
