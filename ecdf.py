
import numpy as np

# Empirical cumulative distribution function


def ecdf(data):

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y


if __name__=="__main__":
    ecdf()