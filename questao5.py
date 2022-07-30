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

accumulatedNormalizedHistogramImg1 = normalizedHistogramLena.copy()

for key in accumulatedNormalizedHistogramImg1:
  if key == 0:
    continue
  accumulatedNormalizedHistogramImg1[key] += accumulatedNormalizedHistogramImg1[key - 1]

mappingToEqualizeImg1 = accumulatedNormalizedHistogramImg1.copy()

for key in accumulatedNormalizedHistogramImg1:
  mappingToEqualizeImg1[key] = round(accumulatedNormalizedHistogramImg1[key] * 255)

specifiedImage1 = Image.new("L", (img1.width, img1.height))
pixelsSpecifiedImage1 = specifiedImage1.load()
for line in range(img1.width):
  for column in range(img1.height):
    if pixelsImg1[line, column] in mappingToEqualizeImg1:
      pixelsSpecifiedImage1[line, column] = mappingToEqualizeImg1[pixelsImg1[line, column]]

histogramImg1Specified = {}

for i in range(256):
  histogramImg1Specified[i] = 0

for line in range(specifiedImage1.width):
  for column in range(specifiedImage1.height):
    if pixelsSpecifiedImage1[line, column] in histogramImg1Specified:
      histogramImg1Specified[pixelsSpecifiedImage1[line, column]] += 1

specifiedImage1.save("./images/image1Specified.png")

plt.figure(figsize=(10, 5))
plt.title('Histograma especificado')
plt.xlabel('Nível de intensidade do pixel')
plt.ylabel('Frequência')
plt.hist(list(histogramImg1Specified.keys()), bins=256, weights=list(histogramImg1Specified.values()), color="blue")
plt.savefig("./images/histogramImg1Specified.png")
plt.close()
