from audioop import add
from PIL import Image
"""from blend_modes import addition"""

def addition(img1 , img2):
    rimg = []
    temp = []
    for i in range(0,100):
        for k in range(0,100):
            r = img1[i][k][1] + img2[i][k][1]
            if r > 255 :
                r = 255
            g = img2[i][k][2] + img2[i][k][2]
            if g > 255 :
                g = 255
            b = img1[i][k][3] + img2[i][k][3]
            if b > 255 :
                b = 255
            pixel = (r, g, b ,255)
            temp.append(pixel)
        rimg.append(temp)
        temp = []
    return rimg


img1 = Image.open(r'smile.png')
img1 = img1.resize((100, 100))
img2 = Image.open(r'circles.png')
img2 = img2.resize((100, 100))
temp = list(img1.getdata())
rgb_1 = []
temp1 = []
for i in range(0,10000):
    temp1.append(temp[i])
    if (i+1)%100 == 0 :
        rgb_1.append(temp1)
        temp1 = []
"""for i in range(0,100):
    print("row", i)
    print(rgb_1[i])"""

temp = list(img2.getdata())
rgb_2 = []
temp1 = []
for i in range(0,10000):
    temp1.append(temp[i])
    if (i+1)%100 == 0 :
        rgb_2.append(temp1)
        temp1 = []


rgb_3 = addition(rgb_1, rgb_2)
for i in rgb_3 :
    n = 1
    print("Row\t: ", n + 1)
    for k in i :
        print(i)
    n = n + 1