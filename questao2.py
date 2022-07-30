import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("../lena_gray.bmp")
pixels = img.load()

histogram = {}

for i in range(256):
  histogram[i] = 0

for line in range(img.width):
  for column in range(img.height):
    if pixels[line, column] in histogram:
      histogram[pixels[line, column]] += 1

normalizedHistogram = histogram.copy()

for key in normalizedHistogram:
  normalizedHistogram[key] = normalizedHistogram[key] / (img.width * img.height)

accumulatedHistogram = histogram.copy()

for key in accumulatedHistogram:
  if key == 0:
    continue
  accumulatedHistogram[key] += accumulatedHistogram[key - 1]

plt.figure(figsize=(10, 5))
plt.title('Histograma lenagray')
plt.hist(list(histogram.keys()), bins=256, weights=list(histogram.values()), color="blue")
plt.xlabel('Nível de intensidade do pixel')
plt.ylabel('Frequência')
plt.savefig('./images/histogramLena2.png')
plt.close()

plt.figure(figsize=(10, 5))
plt.title('Histograma lenagray normalizado')
plt.hist(list(normalizedHistogram.keys()), bins=256, weights=list(normalizedHistogram.values()), color="green")
plt.xlabel('Nível de intensidade do pixel')
plt.ylabel('Frequência')
plt.savefig('./images/normalizedHistogramLena2.png')
plt.close()

plt.figure(figsize=(10, 5))
plt.title('Histograma lenagray acumulado')
plt.hist(list(accumulatedHistogram.keys()), bins=256, weights=list(accumulatedHistogram.values()), color="red")
plt.xlabel('Nível de intensidade do pixel')
plt.ylabel('Frequência')
plt.savefig('./images/accumulatedHistogramLena2.png')
plt.close()
