"""A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!
"""
nyelvek = []
with open('adatok/fajl.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nyelv = {'evszam': int(adatok[0]), 'nyelv': adatok[1], 'elsonev': adatok[2], 'masodiknev': adatok[3]}
        nyelvek.append(nyelv)
        
print(f'{nyelvek}')

for nyelv in nyelvek:
    print(f"{nyelv["evszam"]} - {nyelv["nyelv"]} - {nyelv["elsonev"]} - {nyelv["masodiknev"]}")
    
legidosebb_nyelv_evszam = nyelvek[0]["evszam"]
for nyelv in nyelvek:
    if nyelv["evszam"] > legidosebb_nyelv_evszam:
        legidosebb_nyelv_evszam = nyelv["evszam"]
        legidosebb_nyelv = nyelv
print(legidosebb_nyelv_evszam)
print(legidosebb_nyelv)

legfiatalabb_nyelv_evszam = nyelvek[0]["evszam"]
for nyelv in nyelvek:
    if nyelv["evszam"] < legfiatalabb_nyelv_evszam:
        legfiatalabb_nyelv_evszam = nyelv["evszam"]
        legfiatalabb_nyelv = nyelv
print(legfiatalabb_nyelv_evszam)
print(legfiatalabb_nyelv)