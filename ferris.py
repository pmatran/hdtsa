import numpy as np


def attenuation2hd(alpha: float, x: float, T: float) -> float:
    """
    Compute the diffusivity from the 1D Ferris based on signal attenuation.

    Arguments:
    ----------
    alpha (float) : signal attenuation [-]
    x (float) : shortest distance from the cost to the observation well [m]
    T (float) : aquifer transimissivity [m²/s]

    """
    d_alpha = (2 * np.pi * (x ** 2)) / (T * np.log2(alpha))
    return d_alpha


def shift2hd(phi: float, x: float, T: float) -> float:
    """
    Compute the diffusivity from the 1D Ferris based on signal shift

    Arguments:
    ----------
    phi (float) : signal shift [s]
    x (float) : shortest distance from the cost to the observation well [m]
    T (float) : aquifer transimissivity [m²/s]

    """
    d_phi = (np.pi * (x ** 2)) / (T * (phi ** 2))
    return d_phi
