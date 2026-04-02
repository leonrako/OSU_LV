import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")


plt.imshow(img, cmap='gray', alpha=0.75)
plt.title('Posvijetljena slika')
plt.show()


img_quarter = img[:, img.shape[1] // 4 : img.shape[1] // 2]
plt.imshow(img_quarter, cmap='gray')
plt.title('Druga četvrtina slike po širini')
plt.show()


img_rotated = np.rot90(img, k=3)
plt.imshow(img_rotated, cmap='gray')
plt.title('Rotirana slika')
plt.show()

 
img_flipped = np.fliplr(img)
plt.imshow(img_flipped, cmap='gray')
plt.title('Zrcaljena slika')
plt.show()
