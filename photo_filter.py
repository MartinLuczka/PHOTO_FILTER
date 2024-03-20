from PIL import Image
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
                obrazek.putpixel((x,y), (29, 113, 186))
            elif prumer >= 120 and prumer < 150:
                obrazek.putpixel((x,y), (237,196,0))
            elif prumer >= 150 and prumer < 170:
                obrazek.putpixel((x,y), (178,86,144))
            else:
                obrazek.putpixel((x,y), (113,179,121))
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
                obrazek.putpixel((x,y), (182,230,150))
            elif prumer >= 120 and prumer < 150:
                obrazek.putpixel((x,y), (169,94,163))
            elif prumer >= 150 and prumer < 170:
                obrazek.putpixel((x,y), (220,58,121))
            else:
                obrazek.putpixel((x,y), (22,134,205))
            y += 1
        x += 1

print("Vítejte v programu pro úpravu fotek.")

volba = input(
"""Vyberte si jednu z následujících možností:
1) filtr barev č.1
2) filtr barev č.2
3) filtr barev č.3""")

if volba == "1":
    barevne_schema1()

#display(obrazek) - nefunguje ve VS code

barevne_schema1()
obrazek.show()

