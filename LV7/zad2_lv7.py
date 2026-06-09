import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs/test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

uniqueColors = np.unique(img_array, axis=0)
print(len(uniqueColors))

km = KMeans(2, init='k-means++')
km.fit(img_array)

labels = km.predict(img_array)

img_array_aprox = km.cluster_centers_[labels]

new_img = np.reshape(img_array_aprox, (w, h, d))

plt.figure()
plt.imshow(new_img)
plt.show()

K = range(1, 15)
inertia = []

for k in K:
    kmeans = KMeans(k)
    kmeans.fit(img_array)
    inertia.append(kmeans.inertia_)

plt.plot(K, inertia)
plt.show()
