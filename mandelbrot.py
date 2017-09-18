import numpy as np
import matplotlib.pyplot as plt

def mandel(N):

    M = np.empty([N,N],int)

    for y in range(N):
        for x in range(N):
            z = 0
            c_real = -2 + 4.*x/N
            c_imag = -2 + 4.*y/N
            c = c_real + c_imag*1j

            for n in range(100):
                if z.real**2 + z.imag**2 <= 4:
                    z = z*z + c
                else:
                    M[y,x] = n
                    break

            if z.real**2 + z.imag**2 <= 4:
                M[y,x] = 1

    plt.imshow(M, cmap="jet", extent=[-2,2,-2,2])
    cbar = plt.colorbar()
    cbar.set_label("iterations")
    plt.xlabel("x")
    plt.ylabel("iy")
    plt.show()

mandel(1000)
