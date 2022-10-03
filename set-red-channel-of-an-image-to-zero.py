#Name: Maximilian Jaramazovic
#Email: maximilian.jaramazovic08@myhunter.cuny.edu
#Date: 10/3/2022

import matplotlib.pyplot as plt
import numpy as np

img = plt.imread(input("Enter name of the input file: "))
nameOfNewFile = input("Enter name of the output file: ")


img2 = img.copy()
img2[:,:, 0] = 0
plt.imshow(img2)
plt.show()

plt.imsave(nameOfNewFile, img2)
