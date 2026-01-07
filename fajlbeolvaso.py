autok = []
with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

print(f'{autok=}')

for auto in autok:
    print(f"{auto["rendszam"]} - {auto["tipus"]} - {auto["kor"]}")
    
legidosebb_auto_kor = autok[0]["kor"]
for auto in autok:
    if auto["kor"] > legidosebb_auto_kor:
        legidosebb_auto_kor = auto["kor"]
        legidosebb_auto = auto
print(legidosebb_auto_kor)
print(legidosebb_auto)

legfiatalabb_auto_kor = autok[0]["kor"]
for auto in autok:
    if auto["kor"] < legfiatalabb_auto_kor:
        legfiatalabb_auto_kor = auto["kor"]
        legfiatalabb_auto = auto
print(legfiatalabb_auto_kor)
print(legfiatalabb_auto)