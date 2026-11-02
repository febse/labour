"""Shared calibration and helpers for the Borjas Ch. 2-4 model notebooks.

Every parameter used in the notebooks (and in the Desmos guides) is defined
here, so that the three notebooks and the Desmos instructions stay consistent.
"""

from types import SimpleNamespace

import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------------
# Plot style
# ---------------------------------------------------------------------------
plt.rcParams.update(
    {
        "figure.figsize": (6, 4.2),
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "legend.frameon": False,
    }
)

BLUE, RED, GREEN, GREY, ORANGE = "#1f6fb2", "#c0392b", "#2e8b57", "#7f8c8d", "#e08a1e"

# ---------------------------------------------------------------------------
# Chapter 2: labor supply (numbers follow the worked example in Borjas 2-5)
# ---------------------------------------------------------------------------
supply = SimpleNamespace(
    T=110.0,  # non-sleeping hours per week
    V=100.0,  # non-labor income ($ / week)
    w=10.0,  # hourly wage ($)
    a=0.6,  # weight on leisure in U = L^a C^(1-a)
    sigma=0.5,  # elasticity of substitution in the CES variant
    # Household production (2-9): Z = x^beta H^(1-beta); U = Z^gamma L^(1-gamma)
    beta=0.5,
    gamma=0.7,
    # Life cycle (2-13): two periods, ln utility
    disc=0.95,  # beta_t, discount factor
    r=0.03,  # interest rate
    A0=0.0,  # initial assets
)

# ---------------------------------------------------------------------------
# Chapter 3: labor demand
# ---------------------------------------------------------------------------
demand = SimpleNamespace(
    A=50.0,  # total factor productivity
    alpha=0.3,  # capital exponent (q = A K^alpha E^beta)
    beta=0.5,  # labor exponent; alpha + beta < 1 -> decreasing returns
    p=1.0,  # output price
    w=10.0,  # wage
    r=10.0,  # rental rate of capital
    # Industry with constant returns (used for the Hicks-Marshall rules)
    alpha_crs=0.3,
    beta_crs=0.7,
    eta=1.0,  # price elasticity of product demand (absolute value)
)

# ---------------------------------------------------------------------------
# Chapter 4: market equilibrium (constant-elasticity curves through (E0, w0))
# ---------------------------------------------------------------------------
market = SimpleNamespace(
    w0=20.0,  # initial equilibrium wage
    E0=100.0,  # initial equilibrium employment (millions of hours)
    eps_S=0.5,  # supply elasticity
    delta=-0.75,  # demand elasticity
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def cobb_douglas(x, y, a):
    """x^a * y^(1-a)."""
    return x**a * y ** (1 - a)


def indifference_curve(u, a, L):
    """Consumption on the Cobb-Douglas indifference curve L^a C^(1-a) = u."""
    return (u / L**a) ** (1 / (1 - a))


def isoquant(q, A, alpha, beta, E):
    """Capital on the isoquant A K^alpha E^beta = q."""
    return (q / (A * E**beta)) ** (1 / alpha)


def curve_from_elasticity(w0, E0, elasticity):
    """Return E(w) and w(E) for E = E0 (w/w0)^elasticity."""

    def E_of_w(w):
        return E0 * (np.asarray(w, dtype=float) / w0) ** elasticity

    def w_of_E(E):
        return w0 * (np.asarray(E, dtype=float) / E0) ** (1 / elasticity)

    return E_of_w, w_of_E
