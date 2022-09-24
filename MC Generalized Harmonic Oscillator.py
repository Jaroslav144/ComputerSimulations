import numpy as np

a = 4
K = 1
k = 1
T = 2
N = 1000000


def hamiltonian(q):
    return K * np.float_power(np.abs(q), a)


def probability(qf, qi):
    return np.exp(-(hamiltonian(qf) - hamiltonian(qi)) / (k * T))

x0 = 0
E_av = 0
E2_av = 0
for i in range(N):
    x = np.random.rand() * 20 - 10
    p = np.random.rand()
    if hamiltonian(x) <= hamiltonian(x0):
        x0 = x
    else:
        if p < probability(x, x0):
            x0 = x
    E_av += hamiltonian(x0)
    E2_av += hamiltonian(x0) ** 2

E_av /= N
E2_av /= N
c = (E2_av - E_av**2) / (k * (T ** 2))

print("Temperature \t Energy \t Heat capacity")
print(f"{T} \t {E_av} \t {c}")
