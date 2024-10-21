vuosi = 2000
# Karkausvuosia ovat kaikki 400:lla jaolliset vuodet
if vuosi % 400 == 0:
    print("Oli karkausvuosi")

# 4:llä jaollisista vuosista ne, jotka eivät ole 100:lla jaollisia.

elif vuosi % 4 == 0:
    if vuosi % 100 != 0:
        print("Oli karkausvuosi")
else:
    print("Ei ole karkausvuosi")