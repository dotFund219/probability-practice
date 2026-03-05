import matplotlib.pyplot as plt
import numpy as np

n = 100_000

rolls = np.random.randint(1, 7, size=n)

running_mean = np.cumsum(rolls) / np.arange(1, n + 1)

plt.figure()
plt.plot(running_mean)
plt.axhline(3.5, color='r')
plt.xlabel('Number of rolls')
plt.ylabel('Running Mean')
plt.title('Law of Large Numbers - Dice simulation')
plt.show()