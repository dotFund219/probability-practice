import numpy as np
import matplotlib.pyplot as plt

n = 10000
coins = np.random.choice(["H", "T"], size=n)

is_head = (coins == "H").astype(int)

cumulative_heads = np.cumsum(is_head)

trials = np.arange(1, n + 1)

cumulative_prob = cumulative_heads / trials

plt.plot(trials, cumulative_prob)
plt.axhline(y=0.5, linestyle="--", color="r")
plt.xlabel("Trials")
plt.ylabel("Cumulative Probability")
plt.title("Cumulative Probability")
plt.show()