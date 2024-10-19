# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    w = np.linalg.solve(tx.T @ tx, tx.T @ y)
    
    # Calculate the mean squared error
    e = y - tx @ w
    mse = (1 / (2 * len(y))) * np.sum(e**2)
    
    return w, mse
    # ***************************************************

