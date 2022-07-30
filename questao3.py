import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

imgLena = Image.open("../lena_gray.bmp")
pixelsLena = imgLena.load()

img1 = Image.open("../image1.png")
pixelsImg1 = img1.load()

histogramLena = {}
histogramImg1 = {}

for i in range(256):
  histogramLena[i] = 0
  histogramImg1[i] = 0

for line in range(imgLena.width):
  for column in range(imgLena.height):
    if pixelsLena[line, column] in histogramLena:
      histogramLena[pixelsLena[line, column]] += 1

normalizedHistogramLena = histogramLena.copy()

for key in normalizedHistogramLena:
  normalizedHistogramLena[key] = normalizedHistogramLena[key] / (imgLena.width * imgLena.height)

normalizedAccumulatedHistogramLena = normalizedHistogramLena.copy()

for key in normalizedAccumulatedHistogramLena:
  if key == 0:
    continue
  normalizedAccumulatedHistogramLena[key] += normalizedAccumulatedHistogramLena[key - 1]

mappingToEqualizeLena = histogramLena.copy()

for key in normalizedHistogramLena:
  mappingToEqualizeLena[key] = round(normalizedAccumulatedHistogramLena[key] * 255)

imgLenaEqualized = Image.new("L", (imgLena.width, imgLena.height))
pixelsLenaEqualized = imgLenaEqualized.load()

for line in range(imgLena.width):
  for column in range(imgLena.height):
    if pixelsLena[line, column] in mappingToEqualizeLena:
      pixelsLenaEqualized[line, column] = mappingToEqualizeLena[pixelsLena[line, column]]

imgLenaEqualized.save("./images/lena_equalized.png")

# ------------------------------ #

for line in range(img1.width):
  for column in range(img1.height):
    if pixelsImg1[line, column] in histogramImg1:
      histogramImg1[pixelsImg1[line, column]] += 1

normalizedHistogramImg1 = histogramImg1.copy()

for key in normalizedHistogramImg1:
  normalizedHistogramImg1[key] = normalizedHistogramImg1[key] / (img1.width * img1.height)

normalizedAccumulatedHistogramImg1 = normalizedHistogramImg1.copy()

for key in normalizedAccumulatedHistogramImg1:
  if key == 0:
    continue
  normalizedAccumulatedHistogramImg1[key] += normalizedAccumulatedHistogramImg1[key - 1]

mappingToEqualizeImg1 = histogramImg1.copy()

for key in normalizedHistogramImg1:
  mappingToEqualizeImg1[key] = round(normalizedAccumulatedHistogramImg1[key] * 255)

img1Equalized = Image.new("L", (img1.width, img1.height))
pixelsImg1Equalized = img1Equalized.load()

for line in range(img1.width):
  for column in range(img1.height):
    if pixelsImg1[line, column] in mappingToEqualizeImg1:
      pixelsImg1Equalized[line, column] = mappingToEqualizeImg1[pixelsImg1[line, column]]

img1Equalized.save("./images/image1_equalized.png")


# ------------------------------ #

pixelsImgLenaEqualized = imgLenaEqualized.load()
pixelsImg1Equalized = img1Equalized.load()

histogramLenaEqualized = {}
histogramImg1Equalized = {}

for i in range(256):
  histogramLenaEqualized[i] = 0
  histogramImg1Equalized[i] = 0

for line in range(imgLenaEqualized.width):
  for column in range(imgLenaEqualized.height):
    if pixelsImgLenaEqualized[line, column] in histogramLenaEqualized:
      histogramLenaEqualized[pixelsImgLenaEqualized[line, column]] += 1

for line in range(img1Equalized.width):
  for column in range(img1Equalized.height):
    if pixelsImg1Equalized[line, column] in histogramImg1Equalized:
      histogramImg1Equalized[pixelsImg1Equalized[line, column]] += 1

normalizedHistogramLenaEqualized = histogramLenaEqualized.copy()
normalizedHistogramImg1Equalized = histogramImg1Equalized.copy()

for key in normalizedHistogramLenaEqualized:
  normalizedHistogramLenaEqualized[key] = normalizedHistogramLenaEqualized[key] / (imgLenaEqualized.width * imgLenaEqualized.height)

for key in normalizedHistogramImg1Equalized:
  normalizedHistogramImg1Equalized[key] = normalizedHistogramImg1Equalized[key] / (img1Equalized.width * img1Equalized.height)

normalizedAccumulatedHistogramLenaEqualized = normalizedHistogramLenaEqualized.copy()
normalizedAccumulatedHistogramImg1Equalized = normalizedHistogramImg1Equalized.copy()

for key in normalizedAccumulatedHistogramLenaEqualized:
  if key == 0:
    continue
  normalizedAccumulatedHistogramLenaEqualized[key] += normalizedAccumulatedHistogramLenaEqualized[key - 1]

for key in normalizedAccumulatedHistogramImg1Equalized:
  if key == 0:
    continue
  normalizedAccumulatedHistogramImg1Equalized[key] += normalizedAccumulatedHistogramImg1Equalized[key - 1]

mappingToEqualizeLenaEqualized = histogramLenaEqualized.copy()
mappingToEqualizeImg1Equalized = histogramImg1Equalized.copy()

for key in normalizedHistogramLenaEqualized:
  mappingToEqualizeLenaEqualized[key] = round(normalizedAccumulatedHistogramLenaEqualized[key] * 255)

for key in normalizedHistogramImg1Equalized:
  mappingToEqualizeImg1Equalized[key] = round(normalizedAccumulatedHistogramImg1Equalized[key] * 255)

equalizedLenaEqualized = Image.new("L", (imgLenaEqualized.width, imgLenaEqualized.height))
pixelsEqualizedLenaEqualized = equalizedLenaEqualized.load()

for line in range(equalizedLenaEqualized.width):
  for column in range(equalizedLenaEqualized.height):
    if pixelsImgLenaEqualized[line, column] in mappingToEqualizeLenaEqualized:
      pixelsEqualizedLenaEqualized[line, column] = mappingToEqualizeLenaEqualized[pixelsImgLenaEqualized[line, column]]

equalizedImg1Equalized = Image.new("L", (img1Equalized.width, img1Equalized.height))
pixelsEqualizedImg1Equalized = equalizedImg1Equalized.load()

for line in range(equalizedImg1Equalized.width):
  for column in range(equalizedImg1Equalized.height):
    if pixelsImg1Equalized[line, column] in mappingToEqualizeImg1Equalized:
      pixelsEqualizedImg1Equalized[line, column] = mappingToEqualizeImg1Equalized[pixelsImg1Equalized[line, column]]

equalizedLenaEqualized.save("./images/lena_equalized_equalized.png")
equalizedImg1Equalized.save("./images/image1_equalized_equalized.png")

for line in range(imgLenaEqualized.width):
  for column in range(imgLenaEqualized.height):
    if pixelsImgLenaEqualized[line, column] != pixelsEqualizedLenaEqualized[line, column]:
      print(f"Error: pixel {line} {column}")
      exit(1)

for line in range(img1Equalized.width):
  for column in range(img1Equalized.height):
    if pixelsImg1Equalized[line, column] != pixelsEqualizedImg1Equalized[line, column]:
      print(f"Error: pixel {line} {column}")
      exit(1)

plt.figure(figsize=(10, 5))
plt.hist(histogramLenaEqualized.keys(), bins=256, weights=list(histogramLenaEqualized.values()), color="blue")
plt.title('Histograma Lenagray equalizado')
plt.xlabel('Nível de intensidade do pixel')
plt.ylabel('Frequência')
plt.savefig("./images/histogramLenaEqualized3.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.hist(histogramLena.keys(), bins=256, weights=list(histogramLena.values()), color="blue")
plt.title('Histograma Lenagray')
plt.xlabel('Nível de intensidade do pixel')
plt.ylabel('Frequência')
plt.savefig("./images/histogramLena3.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.hist(histogramImg1Equalized.keys(), bins=256, weights=list(histogramImg1Equalized.values()), color="red")
plt.title('Histograma image1 equalizado')
plt.xlabel('Nível de intensidade do pixel')
plt.ylabel('Frequência')
plt.savefig("./images/histogramImg1Equalized3.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.hist(histogramImg1.keys(), bins=256, weights=list(histogramImg1.values()), color="red")
plt.title('Histograma image1')
plt.xlabel('Nível de intensidade do pixel')
plt.ylabel('Frequência')
plt.savefig("./images/histogramImg13.png")
plt.close()
