import numpy as np
import matplotlib.pyplot as plt

data = np.random.uniform(1, 10, 100_000)

sample_means = []

for i in range(100_000):
    sample = np.random.choice(data, size=30)
    sample_means.append(np.mean(sample))

plt.hist(sample_means, bins=50, density=True)
plt.title('Distribution of Sample Mean')
plt.show()