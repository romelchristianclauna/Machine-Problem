def sepia(oldPixel):
    red = oldPixel.getRed()
    green = oldPixel.getGreen()
    blue = oldPixel.getBlue()
    
    newred = int(red*0.393 + green*0.769 + blue*0.189)
    newgreen = int(red *0.349 + green*0.686 + blue*0.168)
    newblue = int(red*0.272 + green*0.534 + blue*0.131)
    
    newPixel = Pixel(newred,newgreen,newblue)
    return newPixel

def generalScale(oldimage ,widthscale ,heightscale):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    newim = EmptyImage(oldw*widthscale ,oldh*heightscale)
    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col//widthscale
            originalRow = row//heightscale
            oldpixel = oldimage.getPixel(originalCol , originalRow)

            newim.setPixel(col , row , oldpixel)

    return newim

def originalScale():
    for row in range(oldimage.getheight()):
        for col in range(oldimage.getheight()):
            oldpixel = oldimage.getPixel(col, row)
            sepiaImage = sepia(oldpixel)
            oldimage.setPixel(col, row, sepiaImage)

    return oldimage

def displayImage(Image):
    empWin = Image("Image processing", Image.getWidth(), Image.getHeight())
    Image.draw(empWin)

img = Image('')
sepia = originaScale(img)
new =  generalScale(sepia, 1, 2)
displayImage(new)
