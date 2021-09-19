v=[3478,100,999,5201,8004,2014,7890]
print('a) Venitul saptamanal al interprinderii este ', sum(v))
print('b) Media venitului zilnic este', sum(v)/7)
if v.index(max(v))==0:
    print('c) Ziua in care s-a obtinut cel mai mare venit este Luni')
elif v.index(max(v))==1:
    print('c) Ziua in care s-a obtinut cel mai mare venit este Marti')
elif v.index(max(v))==2:
    print('c) Ziua in care s-a obtinut cel mai mare venit este Miercuri')
elif v.index(max(v))==3:
     print('c) Ziua in care s-a obtinut cel mai mare venit este Joi')
elif v.index(max(v))==4:
     print('c) Ziua in care s-a obtinut cel mai mare venit este Vineri')
elif v.index(max(v))==5:
     print('c) Ziua in care s-a obtinut cel mai mare venit este Sambata')
else:
    print('Duminica')
if v.index(min(v))==0:
    print('d) Ziua cu venitul cel mai mic este Luni')
elif v.index(min(v))==1:
    print('d) Ziua cu venitul cel mai mic este Marti')
elif v.index(min(v))==2:
    print('d) Ziua cu venitul cel mai mic este Miercuri')
elif v.index(min(v))==3:
    print('d) Ziua cu venitul cel mai mic este Joi')
elif v.index(min(v))==4:
     print('d) Ziua cu venitul cel mai mic este Vineri')
elif v.index(min(v))==5:
     print('d) Ziua cu venitul cel mai mic este Sambata')
else:
     print('d) Ziua cu venitul cel mai mic este Duminica')






