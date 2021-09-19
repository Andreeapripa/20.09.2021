t=[-8,-6,-3,0,1,2,3,4,5,6,7,8,9,10,11,17,18,24,27,31,34,19,15,-9]
print('a) Temperatura medie esste', sum(t)/24)
print('b) Maximul temperaturii este', max(t)) 
print('b) Minimul temperaturii este', min(t))
for i in t:
    if i==max(t):
        print('c) Ora cand s-a inregistrat temperatura maxima este', t.index(i)+1)
for i in t:
    if i==min(t):
        print('c) Ora cand s-a inregistrat temperatura minima este', t.index(i)+1)
n1=0
for i in t:
    if i<0:
        n1+=1
print('d) Nr. de zile in care au fost inregistrate temperturi mai jos de 0 grade este', n1)
n2=0
for i in t:
    if i>sum(t)/24:
        n2+=1
print('e) Nr. de zile in care au fost inregistrate temperaturi mai mari de media saptamanala este', n2)