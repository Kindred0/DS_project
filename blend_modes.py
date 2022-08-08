def addition(img1 , img2):
    rimg = []
    temp = []
    for i in range(0,img1.len()):
        for k in range(0, img1.len()):
            pixel = (img1[i][k][1] + img2[i][k][1] , img2[i][k][2] + img2[i][k][2], img1[i][k][3] + img2[i][k][3] , 255)
            temp.append(pixel)
        rimg.append(temp)
        temp = []
    return rimg


