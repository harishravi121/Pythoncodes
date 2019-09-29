from multiprocessing import Process
s=0
a=0
def fun1():
   for i in range(1,10):
       s=s+i

def fun2():
    for j in range(1,10):
        a=a+j

 
if __name__ == '__main__':
    Process(target=fun1).start()
    Process(target=fun2).start()

print(a+s)
