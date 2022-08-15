import math

import numpy as np


def subtract_mean(matrix: np.ndarray, standardize=False):
    for i in range(matrix.shape[1]):
        matrix[:, i] = matrix[:, i] - np.mean(matrix[:, i])
        if standardize:
            matrix[:, i] = matrix[:, i] / np.std(matrix[:, i])
    return matrix


def project_onto_subspace():
    print("Read exercise 3.5.")


def variance_explained(s: np.ndarray):
    print(s)
    squares = np.ones(shape=s.shape)
    summed = 0
    for i in range(len(s)):
        squares[i] *= s[i] * s[i]
        summed += squares[i]
    for i in range(len(squares)):
        squares[i] = squares[i] / summed
    return squares


def logistic_sigmoid(x):
    return 1 / (1 + math.exp(-x))


def entropy(vector: np.ndarray):
    n = vector.sum()
    result = 0
    for i in range(len(vector)):
        result -= vector[i] / n * math.log(vector[i] / n, 2)
    return result


def gini(vector: np.ndarray):
    n = vector.sum()
    n = n * n
    summed = 0
    for i in range(len(vector)):
        summed += vector[i] * vector[i] / n
    return 1 - summed


def class_error(vector: np.ndarray):
    return 1 - (vector.max(axis=0) / vector.sum())


def purity_gain(root: np.ndarray, vectors: np.ndarray, method):
    result = method(root)
    sum_root = root.sum()
    for i in range(len(vectors)):
        print(vectors[i])
        print(vectors[i].sum())
        print(vectors[i].max(axis=0))
        result -= vectors[i].sum() / sum_root * method(vectors[i])
        print(result)
    return result


r = np.asarray([3, 3, 1])
vs = np.asarray([[1, 1, 0], [2, 3, 0]])
print(purity_gain(r, vs, class_error))
