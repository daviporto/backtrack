def hexToRGB(hex):
    r = (hex & 0xff0000) >> 16
    g = (hex & 0x00ff00) >> 8
    b = (hex & 0x0000ff) >> 0
    return (r, g, b)

black = hexToRGB(0x000000)
red = hexToRGB(0xff0000)