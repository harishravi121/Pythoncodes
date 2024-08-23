
#Not working yet keyboard code
interrupt pin 1:
    k1=1.3
    k2=2.9

interrupt pin 2:
    k1 = 1.9
    k3=4

#changing instruments
while 1:
    if(pin3=1):
        for(t in range(200)):
            pin3=DAC(5sint(k1wt)+5sint(k2wt))
#2007 dream done in 2024
