print(40*"-","\n","Boucle for :","\n",40*"-")
s=0
for i in range(10):
    s+=i
    print(s)
ss=0
print(40*"-","\n","Boucle et condition inbriquées :","\n",40*"-")
for i in range(10):
    ss+=i
    if ss<5:
        print("La valeur de s est:", s)
    elif ss==6:
        print("La bonne valeur est :", ss)
    else:
        print(ss)
print(40*"-","\n","Boucle while :","\n",40*"-")
i=0
d=0
while i<50:
   d+=i
   i+=2
print(d)