import pytest
import numpy as np
from periodogram_simulation.main import LAMBDA, v2ph


def test_v2ph():
    v = 0.0031
    temporal_baseline = np.array([0, 1, 2])
    desired = 4 * np.pi * np.array([0, 1, 2])
    actual = v2ph(v, temporal_baseline)
    assert (actual == desired).all()