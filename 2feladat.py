nyelvek = []
with open('adatok/fajl.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        year = int(adatok[0])
        language = adatok[1]
        first_name = adatok[2]
        last_name = adatok[3]
        nyelvek.append([year, language, first_name, last_name])
        
print(nyelvek)