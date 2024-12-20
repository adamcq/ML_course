# -*- coding: utf-8 -*-
"""a function used to compute the loss."""

import numpy as np


def compute_loss(y, tx, w, MAE=False):
    """Calculate the loss using either MSE or MAE.

    Args:
        y: shape=(N, )
        tx: shape=(N,2)
        w: shape=(2,). The vector of model parameters.

    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE
    # TODO: compute loss by MSE
    N = len(y)
    e = y - tx.dot(w)
    if MAE:
        loss = 1 / N * sum(abs(e))
    else:
        loss = 1 / (2 * N) * e.T.dot(e)
    return loss
    # ***************************************************
    raise NotImplementedError