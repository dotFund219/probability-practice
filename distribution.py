import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, bernoulli

def normal_distribution(mu=0, sigma=1):
    '''
    normal distribution implemented using random variables

    :param mu: mean of normal distribution
    :param sigma: standard deviation of normal distribution
    :return:
    '''

    samples = np.random.normal(mu, sigma, 10000)

    plt.hist(samples, bins=50, density=True, alpha=0.5, color='red', edgecolor='black', range=(-4, 4), histtype='bar')
    plt.title('normal distribution (μ=0, σ=1)')
    plt.show()

def problem_01():
    samples_01 = np.random.normal(0, 1, 10000)
    samples_02 = np.random.normal(10, 3, 10000)

    plt.hist(samples_01, bins=50, density=True, alpha=0.5, histtype='bar')
    plt.hist(samples_02, bins=50, density=True, alpha=0.5, histtype='bar')
    plt.title('normal distribution')
    plt.show()

if __name__ == '__main__':
    normal_distribution(mu=0, sigma=1)
    problem_01()
