garums_metros = float (input("Ievadi garumu metros:"))
garums_centimetros = float (garums_metros*100)
svars = int (input("Ievadi svaru:"))
optimalais_svars = int (garums_centimetros-svars)
if (optimalais_svars-svars>7):
    print("Jusu svars ir nepietiekams")
elif (svars-optimalais_svars<=7):
    print("Jusu svars ir normals")
else:
    print("Jusu svars ir parak daudz")