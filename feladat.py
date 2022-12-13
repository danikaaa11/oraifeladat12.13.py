import string
sz ="Ha itt a nyár, ugye komám, a szív a víznek szalutál és vígan lépked, akár a tornász így megy a nagy ho-ho-ho horgász. Bátran rikkant, puhányok ho-ho-ho-ho-ho, megint csak ho-ho-ho-ho. Van itt csali és egy két horog, az eszem pedig jól forog, cselt a cselre kiválón sorjáz, ravasz a nagy ho-ho-ho horgász. Városbéli puhányok, nyavalyások ha gyötör a láz, fületek nyissátok gyorsan, hallgassátok, amit most néktek, hallgassátok, amit most néktek eldalol a ho-ho-ho nagy horgász. Ha itt a nyár, ugye komám, a szív a víznek szalutál, és vígan lépked, akár a tornász így megy a nagy ho-ho-ho horgász. Bátran rikkant, puhányok ho-ho-ho-ho-ho, megint csak ho-ho-ho-ho. Van itt csali és egy két horog, az eszem pedig jól forog, cselt a cselre kiválón sorjáz, ravasz a nagy ho-ho-ho horgász. Városbéli puhányok, nyavalyások ha gyötör a láz, fületek nyissátok gyorsan, hallgassátok, ű amit most néktek, hallgassátok, amit most néktek eldalol a ho-ho-ho nagy horgász."

#1.feladat:

result = len(sz.split())

print("Ennyi szó van : " + str(result))

#2.feladat:

horgasz = print("Ennyiszer található a horgász szó a szövegben: ",sz.count("horgász"))

#3.feladat:

ho = sz.replace("ho-ho-ho","HO-HO-HO")
print(ho)

#4.feladat:

print("Található-e szám szövegben?")

#szam = []

#for i in sz:
    #elif
szam = []
for i in sz.split():
   if i.isdigit():
      szam.append(int(z))    
else:
    print("Nem találhátó szám a szövegben.")          
    
#5.feladat:










