import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mp

data = np.loadtxt("millikan.txt")
data[:,0] = data[:,0] / 1.0e15

N = len(data)

E_x = np.sum(data[:,0]) / N
E_y = np.sum(data[:,1]) / N
E_xx = np.sum(data[:,0]**2) / N
E_xy = np.sum(data[:,0]*data[:,1]) / N

m = (E_xy - E_x*E_y)/(E_xx - E_x**2)
c = (E_xx*E_y - E_x*E_xy)/(E_xx - E_x**2)

elec = 1.602e-19 #Coulombs
h_exp = m * elec
h_act = 6.62607004e-34 #J*s

print "slope:", m, "V*s"
print  "y-int:", c, "V"
print "Experimental Planck's constant: ", h_exp/1.0e15, "J*s"
print "Accepted Planck's constant: ", h_act, "J*s"

fit = data
for i in range(N):
    fit[i][1] = m * data[i][0] + c

plt.plot(fit[:,0], fit[:,1], "k", linestyle="-")
plt.plot(data[:,0], data[:,1], marker="o", linestyle="")
plt.xlabel("Frequency [PHz]")
plt.ylabel("Voltage [V]")
plt.suptitle("Fitted Millikan Data")
red_patch = mp.Patch(color='black', label="V=%.4fF%.4f" %(m,c))
plt.legend(handles=[red_patch])
plt.show()
