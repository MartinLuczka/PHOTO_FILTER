from PIL import Image
from PIL import ImageFilter
import random
obrazek = Image.open("oblicej.jpg")
sirka, vyska = obrazek.size

def barevne_schema1():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer < 120:
                obrazek.putpixel((x,y), (20, 64, 88))
            elif prumer >= 120 and prumer < 150:
                obrazek.putpixel((x,y), (221, 103, 30))
            elif prumer >= 150 and prumer < 170:
                obrazek.putpixel((x,y), (252, 169, 27))
            else:
                obrazek.putpixel((x,y), (238, 222, 86))
            y += 1
        x += 1

def barevne_schema2():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer < 120:
                obrazek.putpixel((x,y), (57,136,164))
            elif prumer >= 120 and prumer < 150:
                obrazek.putpixel((x,y), (203,98,95))
            elif prumer >= 150 and prumer < 170:
                obrazek.putpixel((x,y), (103,194,212))
            else:
                obrazek.putpixel((x,y), (208,148,77))
            y += 1
        x += 1

def barevne_schema3():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer < 120:
                obrazek.putpixel((x,y), (169,94,163))
            elif prumer >= 120 and prumer < 150:
                obrazek.putpixel((x,y), (220,58,121))
            elif prumer >= 150 and prumer < 170:
                obrazek.putpixel((x,y), (22,134,205))
            else:
                obrazek.putpixel((x,y), (182,230,150))
            y += 1
        x += 1

def cerna_bila():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r + g + b) / 3)
            obrazek.putpixel((x,y), (prumer, prumer, prumer))
            y += 1
        x += 1

def negativni_filtr():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            novy_r = 255 - r
            novy_g = 255 - g
            novy_b = 255 - b
            obrazek.putpixel((x,y), (novy_r, novy_g, novy_b))
            y += 1
        x += 1

def stara_fotografie_filtr():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            novy_r = int(0.393 * r + 0.769 * g + 0.189 * b)
            novy_g = int(0.349 * r + 0.686 * g + 0.168 * b)
            novy_b = int(0.272 * r + 0.534 * g + 0.131 * b)
            obrazek.putpixel((x,y), (min(novy_r, 255), min(novy_g, 255), min(novy_b, 255)))
            y += 1
        x += 1

def rozostreni_filtr():
    radius = 3
    for x in range(radius, sirka - radius):
        for y in range(radius, vyska - radius):
            sousedni_pixely = []
            for i in range(-radius, radius + 1):
                for j in range(-radius, radius + 1):
                    sousedni_pixely.append(obrazek.getpixel((x + i, y + j)))
            novy_r = sum(p[0] for p in sousedni_pixely) // len(sousedni_pixely)
            novy_g = sum(p[1] for p in sousedni_pixely) // len(sousedni_pixely)
            novy_b = sum(p[2] for p in sousedni_pixely) // len(sousedni_pixely)
            obrazek.putpixel((x, y), (novy_r, novy_g, novy_b))

def detekce_hran_filtr():
    obrazek_bw = obrazek.convert("L")
    hrany_obrazku = obrazek_bw.filter(ImageFilter.FIND_EDGES)
    obrazek.paste(hrany_obrazku, (0, 0))

def nahodna_barva():
    x = 0
    barva1 = random.randint(0,255)
    barva2 = random.randint(0,255)
    barva3 = random.randint(0,255)
    barva4 = random.randint(0,255)
    barva5 = random.randint(0,255)
    barva6 = random.randint(0,255)
    barva7 = random.randint(0,255)
    barva8 = random.randint(0,255)
    barva9 = random.randint(0,255)
    barva10 = random.randint(0,255)
    barva11 = random.randint(0,255)
    barva12 = random.randint(0,255)
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer < 120:
                obrazek.putpixel((x,y), (barva1, barva2, barva3))
            elif prumer >= 120 and prumer < 150:
                obrazek.putpixel((x,y), (barva4, barva5, barva6))
            elif prumer >= 150 and prumer < 170:
                obrazek.putpixel((x,y), (barva7, barva8, barva9))
            else:
                obrazek.putpixel((x,y), (barva10, barva11, barva12))
            y += 1
        x += 1

def efekt_olejove_malby(radius=5):
    for x in range(radius, sirka - radius):
        for y in range(radius, vyska - radius):
            histogram = {}
            for i in range(-radius, radius + 1):
                for j in range(-radius, radius + 1):
                    r, g, b = obrazek.getpixel((x+i, y+j))
                    barva = (r, g, b)
                    if barva in histogram:
                        histogram[barva] += 1
                    else:
                        histogram[barva] = 1
            nejcastejsi_barva = max(histogram, key=histogram.get)
            obrazek.putpixel((x, y), nejcastejsi_barva)

print("Vítejte v programu pro úpravu fotek.")

volba = input(
"""Vyberte si jednu z následujících možností:\n
1) filtr barev č.1
2) filtr barev č.2
3) filtr barev č.3
4) černobílý filtr
5) negativní filtr
6) stará fotografie filtr
7) filtr rozostření
8) filtr detekce hran
9) náhodně barevný filtr
10) filtr olejomalby\n""")

if volba == "1":
    barevne_schema1()

elif volba == "2":
    barevne_schema2()

elif volba == "3":
    barevne_schema3()

elif volba == "4":
    cerna_bila()

elif volba == "5":
    negativni_filtr()

elif volba == "6":
    stara_fotografie_filtr()

elif volba == "7":
    rozostreni_filtr()

elif volba == "8":
    detekce_hran_filtr()

elif volba == "9":
    nahodna_barva()

else:
    barevne_schema1()
    print("Chyba vstupu...Aplikuje se defaultní filtr")

print("Vaše volba se připravuje...")

obrazek.show()

# Program se neukončuje hned, bez volby se zvolí nějaký defaultní filtr, generování náhodného filtru, jak by to šlo urychlit ? - velmi vítaný projekt - dobré ohodnocení, v pythonu můžeme měřit dobu vykonání

