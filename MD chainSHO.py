import numpy as np
import matplotlib.pyplot as plt
import random

seed = random.seed
K = 1.0


def hamiltonian(p, q, n):
    e = 0
    for i in range(n):
        e += p[i+1]**2 / 2 + 0.5*K*(q[i+1] - q[i])**2
    return e


def force(q):
    f = [0]
    for j in range(1, len(q) - 1):
        f.append(-K * (q[j+1] - q[j-1]))
    f.append(-K * (q[-1] - q[-2]))
    return np.asarray(f)


def potential_energy_pp(q, n):
    e = []
    for i in range(n):
        e.append(0.5*K*(q[i+1] - q[i])**2)
    return np.asarray(e)


N = 2
v0 = [np.random.randn() for x in range(N+1)]
v0[0] = 0.0
x0 = [0.2 for i in range(N+1)]
x0[0] = 0
v0 = np.asarray(v0, dtype=np.float64)
x0 = np.asarray(x0, dtype=np.float64)
dt = 0.00000005 #float(input("Timestep: "))
I = 2000000 #int(input("Number of iterations: "))

print(v0)
print(x0)

k = 1

E0 = hamiltonian(v0, x0, N)
visited = [x0]

X = np.arange(-1.1, 1.1, 0.01)

x = x0
v = v0

K_av = 0.5 * np.sum(v0 * v0)
U_av = sum(potential_energy_pp(x0, N))
U2_av = sum(potential_energy_pp(x0, N) ** 2)

for i in range(I):
    x = x0 + v0*dt
    v = v0 + force(x0)*dt
    K_av += 0.5 * np.sum(v*v)
    U_av += sum(potential_energy_pp(x, N))
    U2_av += sum(potential_energy_pp(x, N) ** 2)
    visited.append(x)
    x0 = x
    v0 = v

Ef = hamiltonian(v, x, N)

K_av = K_av / (I*N)
U_av = U_av / (I*N)
U2_av = U2_av / (I*N)
T = K_av / k
Cv = (U2_av - U_av ** 2)/(N * k * T**2)
print(f"Effective temperature: {T}")
print(f"Specific heat: {Cv}")
print(f"Initial energy: {E0}")
print(f"Final energy: {Ef}")

# visited = np.asarray(visited).transpose()

# fig, ax = plt.subplots(2)
# ax[0].hist(visited[1], bins=200)
# ax[1].hist(visited[4] - visited[3], bins=200)
# plt.show()
