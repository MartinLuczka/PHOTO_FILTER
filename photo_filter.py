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
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            prumer = (r + g + b) // 3
            if prumer < 100:
                obrazek.putpixel((x, y), (11, 72, 107))
            elif 100 <= prumer < 140:
                obrazek.putpixel((x, y), (219, 127, 96))
            elif 140 <= prumer < 180:
                obrazek.putpixel((x, y), (235, 193, 150))
            elif 180 <= prumer < 220:
                obrazek.putpixel((x, y), (148, 194, 174))
            else:
                obrazek.putpixel((x, y), (234, 225, 217))

def barevne_schema3():
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            prumer = (r + g + b) // 3
            if prumer < 100:
                obrazek.putpixel((x, y), (82, 45, 128))
            elif 100 <= prumer < 140:
                obrazek.putpixel((x, y), (208, 60, 150))
            elif 140 <= prumer < 180:
                obrazek.putpixel((x, y), (34, 169, 202))
            elif 180 <= prumer < 220:
                obrazek.putpixel((x, y), (149, 191, 90))
            else:
                obrazek.putpixel((x, y), (11, 72, 107))

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

def pixelizace_filtr(velikost=10):
    for x in range(0, sirka, velikost):
        for y in range(0, vyska, velikost):
            r_total, g_total, b_total = 0, 0, 0
            pocet_pixelu = 0
            for i in range(velikost):
                for j in range(velikost):
                    if x + i < sirka and y + j < vyska:
                        r, g, b = obrazek.getpixel((x + i, y + j))
                        r_total += r
                        g_total += g
                        b_total += b
                        pocet_pixelu += 1
            prumer_r = int(r_total / pocet_pixelu)
            prumer_g = int(g_total / pocet_pixelu)
            prumer_b = int(b_total / pocet_pixelu)
            for i in range(velikost):
                for j in range(velikost):
                    if x + i < sirka and y + j < vyska:
                        obrazek.putpixel((x + i, y + j), (prumer_r, prumer_g, prumer_b))

print("Vítejte v programu pro úpravu fotek.")

volba = input(
"""Vyberte si jednu z následujících možností:\n
0) z nabízených možností vybrat náhodně
1) filtr barev č.1
2) filtr barev č.2
3) filtr barev č.3
4) černobílý filtr
5) negativní filtr
6) stará fotografie filtr
7) filtr rozostření
8) filtr detekce hran
9) náhodně barevný filtr
10) filtr pixelizace
\n""")

if volba == "0":
    volba = str(random.randint(1, 10))
    print(volba)

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

elif volba == "10":
    pixelizace_filtr()

else:
    barevne_schema1()
    print("Chyba vstupu...Aplikuje se defaultní filtr")

print("Vaše volba se připravuje...")

obrazek.show()

# Program se neukončuje hned, bez volby se zvolí nějaký defaultní filtr, generování náhodného filtru, jak by to šlo urychlit ? - velmi vítaný projekt - dobré ohodnocení, v pythonu můžeme měřit dobu vykonání

