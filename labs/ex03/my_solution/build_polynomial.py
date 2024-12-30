# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data

    N = x.shape[0]
    poly = np.ones((N, degree+1))
    for j in range(1, degree+1):
        poly[:,j] = poly[:,j-1]*x
    # print('build_poly log: x.shape, tx.shape', x.shape, poly.shape)
    return poly
    # ***************************************************
    raise NotImplementedError
