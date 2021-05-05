import math
import numpy as np
import matplotlib.pyplot as plt

mu = 0
sigma = 56176151.52
# pos = [0.0, 0.0, 0.0]

# def Step(pos, N, mu, sigma):
#     dx = np.random.normal(mu, sigma, N)
#     dy = np.random.normal(mu, sigma, N)
#     dz = np.random.normal(mu, sigma, N)
#     pos[0] += np.sum(dx)
#     pos[1] += np.sum(dy)
#     pos[2] += np.sum(dz)
#     return pos

# pos = Step(pos, 1E8, mu, sigma)

# print(pos[0], ", ", pos[1], ", ", pos[2])

r = 0 # in meters
N = 100 # number of particles
i = 0
x = 0
y = 0
z = 0
t = 0
mu = 0
sigma = 56176151.52

dx = np.random.normal(mu, sigma, N)
dy = np.random.normal(mu, sigma, N)
dz = np.random.normal(mu, sigma, N)

for c in range(0, N):
    while (r < 6.9634E8):  
        x += dx[i]
        y += dy[i]
        z += dz[i]
        r = np.sqrt(x**2 + y**2 + z**2)
        i += 1
    t_tot = i # in years for one photon
    t += t_tot # in years for all photons in range (0, N)
    t_avg = t/N # average in years per photon

print(t_avg)

# inFile = open("photonDistances2.dat", "r")

# x_avg = 0
# y_avg = 0
# z_avg = 0
# r_avg = 0
# sigma_x = 0
# sigma_y = 0
# sigma_z = 0
# sigma_r = 0
# n = 1

# X = []
# Y = []
# Z = []
# R = []

# for line in inFile:
#     x, y, z, r = line.split(" ")
    
#     x = float(x)
#     y = float(y)
#     z = float(z)
#     r = float(r)
   
#     X.append(x)
#     Y.append(y)
#     Z.append(z)
#     R.append(r)

#     x_avg = float(x_avg)
#     y_avg = float(y_avg)
#     z_avg = float(z_avg)
#     r_avg = float(r_avg)

#     delta = x - x_avg
#     x_avg += delta/n
#     delta2 = x - x_avg
#     sigma_x += delta*delta2
    
#     delta = y - y_avg
#     y_avg += delta/n
#     delta2 = y - y_avg
#     sigma_y += delta*delta2
    
#     delta = z - z_avg
#     z_avg += delta/n
#     delta2 = z - z_avg
#     sigma_z += delta*delta2
    
#     delta = r - r_avg
#     r_avg += delta/n
#     delta2 = r - r_avg
#     sigma_r += delta*delta2
    
#     n += 1

# print(x_avg, "+/-", math.sqrt(sigma_x/n))
# print(y_avg, "+/-", math.sqrt(sigma_y/n))
# print(z_avg, "+/-", math.sqrt(sigma_z/n))
# print(r_avg, "+/-", math.sqrt(sigma_r/n))

# plt.hist(X, bins ='fd', density = True)
# plt.savefig("XHist.pdf")
# plt.clf()
# plt.hist(Y, bins ='fd', density = True)
# plt.savefig("YHist.pdf")
# plt.clf()
# plt.hist(Z, bins ='fd', density = True)
# plt.savefig("ZHist.pdf")
# plt.clf()
# plt.hist(R, bins ='fd', density = True)
# plt.savefig("RHist.pdf")
# plt.clf()