x=[1,2,3,4,5]
y=x
print('a) Suma primelor trei componente ale var. x este', sum(x[0:3]))
print('b) Suma tuturor componentelor var. y este', sum(y))
p=1
for i in range(0,len(x)):
    p=p*x[i]
    i+=1
print('c) Produsul tuturor componentelor var. x este', p)
print('d) Valoarea absoluta a componentei a 3 a var. y este', abs(x[2]))
print('e) Suma primelor componente ale var. x si y este', x[0]+y[0])