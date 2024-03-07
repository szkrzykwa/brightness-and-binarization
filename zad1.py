from PIL import Image

def darkening(image: Image):
    darkening = int(input("Set darkening value (%): "))
    if darkening > 99 or darkening < 1:
        print("Wrong darkening value")
        return image
    else:
        for x in range(row):
            for y in range(col):
                MC[x][y] *= (100-darkening)/100
                MC[x][y] = int(MC[x][y])
        for x in range(row):
            for y in range(col):
                image.putpixel((y,x), MC[x][y])
        image.show()
        return image
    
def brightening(image: Image):
    lst = []
    for i in range(3):
        for x in range(row):
                for y in range(col):
                    MC[x][y] *= 1.15
                    MC[x][y] = int(MC[x][y])
                    if MC[x][y] > 255: MC[x][y] = 255
        for x in range(row):
            for y in range(col):
                image.putpixel((y,x), MC[x][y])
        image.show()
        lst.append(image)
    return lst

def binarization(image: Image):
    for x in range(row):
            for y in range(col):
                if MC[x][y] > 127 : MC[x][y] = 255
                else: MC[x][y] = 0
    for x in range(row):
        for y in range(col):
            image.putpixel((y,x), MC[x][y])
    image.show()
    return image

def binarization_threshold(image: Image):
    threshold = int(input("Set threshold value: "))
    if threshold > 254 or threshold < 1:
        print("Wrong threshold value")
        return image
    for x in range(row):
            for y in range(col):
                if MC[x][y] > threshold : MC[x][y] = 255
                else: MC[x][y] = 0
    for x in range(row):
        for y in range(col):
            image.putpixel((y,x), MC[x][y])
    image.show()
    return image

if __name__ == "__main__":
    img = Image.open("Mapa_MD_no_terrain_low_res_Gray.bmp")
    col, row = img.size
    MC = [[0 for _ in range(col)] for _ in range(row)]
    for x in range(row):
        for y in range(col):
            MC[x][y] = img.getpixel((y,x))
    x = int(input("0 - Darkening\n1 - Brightening\n2 - Binarization\n3 - Binarization with threshold\nChoose operation: "))
    if x == 0:
        rst = darkening(img)
    elif x==1:
        rst = brightening(img)
    elif x==2:
        rst = binarization(img)
    elif x==3:
        rst = binarization_threshold(img)
    else:
        print("Wrong input")
    