
desires = ['love','one nighter','group enter','settle down']
for x in range(0,len(desires)):
    print(x)
    print(desires[x])
    print('\n')


a1=input("What do you want? ");
a=int(a1)
print(desires[a])

group=['Conformal','Compliant','Obediant','Attitude','Social Identity','norms'];
negotiation=['Good-bad','Bogey','Chicken','Strategy development','Auction','Deadlines'];
base=['Open','Transcendant','hedonism', 'Benovalance','Conformal']
Techniques=['Fish','Rapid','OODA','Neo','Morphological']

social=['group','negotiation','base','Techniques']
            

if a==0:
    ans1=[[0,1],[2,1],[0,3,4],[0,1]]

if a==1:
    ans1=[[3,2],[1,5],[3,2],[1,2]]

if a==2:
    ans1=[[1,2,5],[3,4],[3,4],[3,4]]

if a==3:
    ans1=[[1,2,3],[3,4],[1,3,4],[2,4]]

for c in range(0,len(ans1[0])):
    print(group[c])
    print('  ')

for c in range(0,len(ans1[1])):
    print(negotiation[c])
    print('  ')

for c in range(0,len(ans1[2])):
    print(base[c])
    print('  ')

for c in range(0,len(ans1[3])):
    print(Techniques[c])
    print('  ')               
        
        
