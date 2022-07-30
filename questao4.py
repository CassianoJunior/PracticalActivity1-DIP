from math import exp, log2

from PIL import Image

img = Image.open("../lena_gray.bmp")
pixels = img.load()

constantsA = {"c": [0.5, 1.2, 1.5], "b": [10, 20, 30]}
constantsB = {"c": [10, 20, 30]}
constantsC = {"c": [5, 10, 15], "y": [0.3, 0.7, 1]}

for i in range(3):
  newImage = Image.new("L", (img.width, img.height))
  pixelsNewImage = newImage.load()

  for line in range(newImage.width):
    for column in range(newImage.height):
      pixelsNewImage[line, column] = round(constantsA["c"][i] * pixels[line, column] + constantsA["b"][i])
  
  newImage.save(f"./images/lena_gray_c-{constantsA['c'][i]}b-{constantsA['b'][i]}.png")

for i in range(3):
  newImage = Image.new("L", (img.width, img.height))
  pixelsNewImage = newImage.load()

  for line in range(newImage.width):
    for column in range(newImage.height):
      pixelsNewImage[line, column] = round(constantsB["c"][i] * log2(pixels[line, column] + 1))
  
  newImage.save(f"./images/lena_gray_c-{constantsB['c'][i]}-log.png")

for i in range(3):
  newImage = Image.new("L", (img.width, img.height))
  pixelsNewImage = newImage.load()

  for line in range(newImage.width):
    for column in range(newImage.height):
      pixelsNewImage[line, column] = round(constantsC["c"][i] * (pixels[line, column]**constantsC["y"][i]))
  
  newImage.save(f"./images/lena_gray_c-{constantsC['c'][i]}_y-{constantsC['y'][i]}-exp.png")

