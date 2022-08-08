def to_hsv(color) :
    red = color[0]/255
    green = color[1]/255
    blue = color[2]/255
    alpha = color[3]/255
    if red >= green :
        if red >= blue :
            high = red
            if blue >= green :
                low = green
            else :
                low = blue
        else :
            high = blue
            low = green
    elif green >= blue :
        high = green
        if red >= blue :
            low = blue
        else :
            low = red

    diff = high - low


    """ Hue Calculation"""

    if high == low :
        hue = 0
    elif high == red :
        hue = (60 * ((green - blue) / diff) + 360) % 360
    elif high == green : 
        hue = (60 * ((blue - red) / diff) + 120) % 360
    elif high == blue :
        hue = (60 * ((red - green) / diff) + 240) % 360

    """ Saturation Calculation"""

    if high == 0 :
        saturation = 0
    else :
        saturation = (diff / high) * 100

    """Value Calculation"""

    value = high * 100

    return (hue, saturation, value, alpha)



def to_hsv(red, green, blue) :
    red = red/255
    green = green/255
    blue = blue/255
    if red >= green :
        if red >= blue :
            high = red
            if blue >= green :
                low = green
            else :
                low = blue
        else :
            high = blue
            low = green
    elif green >= blue :
        high = green
        if red >= blue :
            low = blue
        else :
            low = red

    diff = high - low


    """ Hue Calculation"""

    if high == low :
        hue = 0
    elif high == red :
        hue = (60 * ((green - blue) / diff) + 360) % 360
    elif high == green : 
        hue = (60 * ((blue - red) / diff) + 120) % 360
    elif high == blue :
        hue = (60 * ((red - green) / diff) + 240) % 360

    """ Saturation Calculation"""

    if high == 0 :
        saturation = 0
    else :
        saturation = (diff / high) * 100

    """Value Calculation"""

    value = high * 100

    return hue, saturation, value

    
    
        

def to_rgb(color) :
    hue = color[0]
    saturation = color[1]
    value = color[2]
    alpha = color[3] * 255
    hue = hue % 360
    if hue < 0 :
        hue = hue + 360
    huec = hue / 60
    chroma = value * saturation
    y = (huec % 2) - 1
    if y < 0 :
        y = y * -1
    x = chroma * (1 - y)
    if huec >= 0 and huec < 1 :
        RGBc = (chroma, x, 0)
    elif huec >= 1 and huec < 2 :
        RGBc = (x, chroma, 0)
    elif huec >= 2 and huec < 3 :
        RGBc = (0 , chroma , x)
    elif huec >= 3 and huec < 4 :
        RGBc = (0, x, chroma)
    elif huec >= 4 and huec < 5 :
        RGBc = (x, 0, chroma)
    elif huec >= 5 and huec < 6 :
        RGBc = (chroma, 0, x)

    m = value - chroma
    red = RGBc[0] + m
    green = RGBc[1] + m
    blue = RGBc[2] + m
    Color = (red, green, blue, alpha)
    return Color

def to_rgb(hue, saturation, value) :
    hue = hue % 360
    if hue < 0 :
        hue = hue + 360
    huec = hue / 60
    chroma = value * saturation
    y = (huec % 2) - 1
    if y < 0 :
        y = y * -1
    x = chroma * (1 - y)
    if huec >= 0 and huec < 1 :
        RGBc = (chroma, x, 0)
    elif huec >= 1 and huec < 2 :
        RGBc = (x, chroma, 0)
    elif huec >= 2 and huec < 3 :
        RGBc = (0 , chroma , x)
    elif huec >= 3 and huec < 4 :
        RGBc = (0, x, chroma)
    elif huec >= 4 and huec < 5 :
        RGBc = (x, 0, chroma)
    elif huec >= 5 and huec < 6 :
        RGBc = (chroma, 0, x)

    m = value - chroma
    red = RGBc[0] + m
    green = RGBc[1] + m
    blue = RGBc[2] + m
    return red, green, blue