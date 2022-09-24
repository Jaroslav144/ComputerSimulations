import matplotlib.pyplot as plt

v0 = 0
x0 = float(input("Initial coordinate: "))
dt = float(input("Timestep: "))
N = int(input("Number of iterations: "))

E0 = 0.5 * x0**2
visited = [x0]

x = x0
v = v0

for i in range(N):
    x = x0 + v0*dt
    v = v0 - x0*dt
    visited.append(x)
    x0 = x
    v0 = v

Ef = 0.5*(v**2 + x**2)

print(f"Initial energy: {E0}")
print(f"Final energy: {Ef}")

plt.hist(visited, bins=200)
plt.show()
