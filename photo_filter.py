from PIL import Image
obrazek = Image.open("oblicej.jpg")
sirka, vyska = obrazek.size
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
display(obrazek) #obrazek.show()