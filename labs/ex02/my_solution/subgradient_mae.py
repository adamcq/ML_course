import numpy as np


def compute_subgradient_mae(y, tx, w):
    """Compute a subgradient of the MAE at w.

    Args:
        y: shape=(N, )
        tx: shape=(N,2)
        w: shape=(2, ). The vector of model parameters.

    Returns:
        An array of shape (2, ) (same shape as w), containing the subgradient of the MAE at w.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE
    # TODO: compute subgradient gradient vector for MAE
    N = y.shape[0]
    e = y - tx.dot(w)

    # Replace the indices i, where e[i] == 0 with a random number from uniform[-1,1)
    e[e==0] = np.random.uniform(-1, 1, np.sum(e==0))

    return -1/N * tx.T.dot(e)
    # ***************************************************
    raise NotImplementedError
