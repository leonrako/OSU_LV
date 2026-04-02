import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', skiprows=1, delimiter=',')


print("Mjerenja su izvršena na", len(data), "osoba")


plt.scatter(data[:, 1], data[:, 2], s=2)
plt.title("Zadatak b: Odnos visine i mase")
plt.xlabel("Visina [cm]")
plt.ylabel("Masa [kg]")
plt.show()


plt.scatter(data[::50, 1], data[::50, 2], s=5)
plt.title("Zadatak c: Svaka 50. osoba")
plt.xlabel("Visina [cm]")
plt.ylabel("Masa [kg]")
plt.show()


print("Minimalna visina:", data[:, 1].min())
print("Maksimalna visina:", data[:, 1].max())
print("Srednja visina:", data[:, 1].mean())


muskarci = (data[:, 0] == 1)
zene = (data[:, 0] == 0)

print("Žene - min, max, mean visine:",
      np.min(data[zene, 1]),
      np.max(data[zene, 1]),
      np.mean(data[zene, 1]))

print("Muškarci - min, max, mean visine:",
      np.min(data[muskarci, 1]),
      np.max(data[muskarci, 1]),
      np.mean(data[muskarci, 1]))