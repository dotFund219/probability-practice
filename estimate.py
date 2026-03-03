import numpy as np

x = np.array([1, 2, 3, 4, 5])
mean_manual = x.sum() / len(x)
mean_np = x.mean()
print(mean_np)
print(mean_manual)

x = np.array([1, 2, 3, 4, 5], dtype=float)
mu = x.sum() / len(x)

var_def = np.mean((x - mu) ** 2)
print(var_def)

ex2 = np.mean(x ** 2)
var_fast = ex2 - mu ** 2
print(var_fast)

n = 100_000
x = np.random.binomial(1, 0.3, n)

mean = np.cumsum(x) / np.arange(1, n + 1)

print("mean:" , mean)
print("distribution", np.var(x))