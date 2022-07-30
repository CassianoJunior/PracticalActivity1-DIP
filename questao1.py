from PIL import Image

im = Image.open("../folha.png")
pixels = im.load()

frontierPixelsAd4 = []
frontierPixelsAd8 = []

def rightIsBlack(line, column):
  return pixels[line, column-1] == (0, 0, 0, 255)

def leftIsBlack(line, column):
  return pixels[line, column+1] == (0, 0, 0, 255)

def upIsBlack(line, column):
  return pixels[line-1, column] == (0, 0, 0, 255)

def downIsBlack(line, column):
  return pixels[line+1, column] == (0, 0, 0, 255)

def upLeftIsBlack(line, column):
  return pixels[line-1, column-1] == (0, 0, 0, 255)

def downLeftIsBlack(line, column):
  return pixels[line+1, column-1] == (0, 0, 0, 255)

def upRightIsBlack(line, column):
  return pixels[line-1, column+1] == (0, 0, 0, 255)

def downRightIsBlack(line, column):
  return pixels[line+1, column+1] == (0, 0, 0, 255)

def isFrontierAd4(line, column):
  return rightIsBlack(line, column) or leftIsBlack(line, column) or upIsBlack(line, column) or downIsBlack(line, column)

def isFrontierAd8(line, column):
  return isFrontierAd4(line, column) or upLeftIsBlack(line, column) or downLeftIsBlack(line, column) or upRightIsBlack(line, column) or downRightIsBlack(line, column)

for line in range(im.width):
  for column in range(im.height):
    if pixels[line, column] == (255, 255, 255, 255):
      if isFrontierAd4(line, column):
        frontierPixelsAd4.append([line, column])

      if isFrontierAd8(line, column):
        frontierPixelsAd8.append([line, column])

imgAd4 = Image.new("RGBA", (im.width, im.height), (0, 0, 0, 255))
pixelsImageAd4 = imgAd4.load()

imgAd8 = Image.new("RGBA", (im.width, im.height), (0, 0, 0, 255))
pixelsImageAd8 = imgAd8.load()

for p in frontierPixelsAd4:
  pixelsImageAd4[p[0], p[1]] = (255, 255, 255, 255)

for p in frontierPixelsAd8:
  pixelsImageAd8[p[0], p[1]] = (255, 255, 255, 255)
    
imgAd4.save("./images/folha_ad4.png")
imgAd8.save("./images/folha_ad8.png")
    

