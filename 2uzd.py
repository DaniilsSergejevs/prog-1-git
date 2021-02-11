apdruka_teksts = int (5)
apdruka_zime = int (7)
apdruka_foto = int (20)
tkreklus_skaits = int (3)
tkreklus_apdruka = int (apdruka_foto)
summa = int (tkreklus_apdruka*tkreklus_skaits)
if summa > 100:
    print("Summa ar atlaidi:",summa/100*95)
elif summa < 100:
    print("Summa bez atlaides:",summa)

if summa < 50:
    print("Summa ar 15 eiro piegadi:",summa+15)
elif summa > 50:
    print("Summa ar bezmaksas piegadi:",summa)
