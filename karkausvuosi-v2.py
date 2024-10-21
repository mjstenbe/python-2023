vuosi = 2000
# Karkausvuosia ovat kaikki 400:lla jaolliset vuodet
if vuosi % 400 == 0 or ( vuosi % 4 == 0 and vuosi % 100 != 0 ):
    print("Oli karkausvuosi")
else:
    print("Ei ole karkausvuosi")