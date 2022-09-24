import numpy as np
import matplotlib.pyplot as plt

A = -1.0
B = -1.0
C = 1.0


def hamiltonian(p, q):
    return 0.5 * p**2 + A * q**2 + B * q**3 + C * q**4


def force(q):
    return -(2*A*q + 3*B*q**2 + 4*C*q**3)


v0 = 0
x0 = float(input("Initial coordinate: "))
dt = float(input("Timestep: "))
N = int(input("Number of iterations: "))

E0 = hamiltonian(v0, x0)
visited = [x0]

X = np.arange(-x0-1, x0+1, 0.01)

x = x0
v = v0

for i in range(N):
    x = x0 + v0*dt
    v = v0 + force(x0)*dt
    visited.append(x)
    x0 = x
    v0 = v

Ef = hamiltonian(v, x)

print(f"Initial energy: {E0}")
print(f"Final energy: {Ef}")

fig, ax = plt.subplots(3)
ax[0].hist(visited, bins=200)
ax[1].plot(X, [E0 for i in range(len(X))])
ax[1].plot(X, [hamiltonian(0, j) for j in X])
ax[2].plot(X, [force(j) for j in X])
plt.show()
