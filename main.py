import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("test.tiff")
npimg = np.array(img, dtype=float)

# get the red rgb from for all pixels and collect them to one list
red = []
green = []
blue = []
for zeile in range(len(npimg)):
    for spalten in range(len(npimg[zeile])):
        red.append(npimg[zeile][spalten][0])
        green.append(npimg[zeile][spalten][1])
        blue.append(npimg[zeile][spalten][2])

fix, ax = plt.subplots(nrows=1, ncols=1)
ax.grid(which='both', color="0.65", linestyle='--')
h = ax.hist(red, bins=256, range=(-0.5, 255), histtype="step", color="r")
h = ax.hist(green, bins=256, range=(-0.5, 255), histtype="step", color="g")
h = ax.hist(blue, bins=256, range=(-0.5, 255), histtype="step", color="b")
plt.show()


def PrintColor(name, color):
    print(name, ":   ","Pixel=  ", len(color)
          ,"Min=   ",min(color),
          "Max=  ", max(color),
          "Mean=  ", np.average(color),
          "Signma= ", np.std(color, dtype=np.float64))


PrintColor("Red",red)
PrintColor("Green",green)
PrintColor("Blue",blue)