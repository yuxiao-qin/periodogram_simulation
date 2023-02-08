import numpy as np

LAMBDA = 0.0031  # [m]
R0 = 700 * 1000 # [m]
INCIDENCE_ANGLE = 30 * np.pi / 180  # [rad]


def simulate_phase(dv: float, dh:float, noise_level:float) -> np.ndarray:
    return v2ph(dv) + h2ph(dh) + noise(noise_level)


def v2ph(v: float, temporal_baseline:np.ndarray=np.arange(30) * 12 / 365) -> np.ndarray:
    distance = v * temporal_baseline
    return 4 * np.pi * distance / LAMBDA

def h2ph(h: float, spatial_baseline:np.ndarray=np.random.randint(0, 200, size=30)) -> np.ndarray:
    h2ph_coef = h * spatial_baseline / (R0 * np.sin(INCIDENCE_ANGLE))
    return  4 * np.pi * h2ph_coef / LAMBDA

def noise(noise_level:float, size: int = 30) -> np.ndarray:
    return np.random.normal(0, 1, size=size) * noise_level

def wrap_phase(phase: np.ndarray) -> np.ndarray:
    return np.mod(phase + np.pi, 2 * np.pi) - np.pi
