import math
import numpy as np

from plots import new_figure, style_axes
from constants import R_UNIVERSAL


def calc_ideal_gas(v):
    solve_for = v["solve_for"]
    P, V, n, T = v["P"], v["V"], v["n"], v["T"]
    if solve_for == "P":
        P = n * R_UNIVERSAL * T / V
        line = f"P = nRT/V = {P:,.4f} Pa"
    elif solve_for == "V":
        V = n * R_UNIVERSAL * T / P
        line = f"V = nRT/P = {V:.6e} m^3"
    elif solve_for == "n":
        n = P * V / (R_UNIVERSAL * T)
        line = f"n = PV/RT = {n:.6f} mol"
    else:
        T = P * V / (n * R_UNIVERSAL)
        line = f"T = PV/nR = {T:,.4f} K"
    return f"Ideal Gas Law (R = 8.314 J/mol-K)\n{line}", None


def calc_carnot(v):
    Th, Tc = v["Th"], v["Tc"]
    if Th <= 0:
        raise ValueError("Th must be > 0 K.")
    eta = 1 - Tc / Th
    return f"Carnot efficiency = 1 - Tc/Th = {eta:.4f}  ({eta*100:.2f} %)", None


def calc_conduction(v):
    k, A, dT, L = v["k"], v["A"], v["dT"], v["L"]
    if L == 0:
        raise ValueError("Thickness L cannot be zero.")
    q = k * A * dT / L
    return f"Heat conduction rate q = k*A*dT / L = {q:,.4f} W", None


def calc_convection(v):
    h, A, dT = v["h"], v["A"], v["dT"]
    q = h * A * dT
    return f"Convective heat transfer q = h*A*dT = {q:,.4f} W", None


def calc_sensible_heat(v):
    m, c, dT = v["m"], v["c"], v["dT"]
    Q = m * c * dT
    return f"Sensible heat Q = m*c*dT = {Q:,.4f} J", None


def calc_thermal_expansion(v):
    alpha, L0, dT = v["alpha"], v["L0"], v["dT"]
    dL = alpha * L0 * dT
    return (f"Change in length dL = alpha*L0*dT = {dL:.6e} m  "
            f"({dL*1000:.5f} mm)"), None


def calc_first_law(v):
    Q, W = v["Q"], v["W"]
    dU = Q - W
    return (f"First Law: dU = Q - W = {dU:,.4f} J\n"
            f"(Q = heat added to system, W = work done by system)"), None


def calc_enthalpy(v):
    m, cp, dT = v["m"], v["cp"], v["dT"]
    dH = m * cp * dT
    return f"Enthalpy change dH = m*cp*dT = {dH:,.4f} J", None


def calc_isothermal_pv(v):
    P1, V1, V2 = v["P1"], v["V1"], v["V2"]
    n_R_T = P1 * V1  
    W = n_R_T * math.log(V2 / V1)

    V = np.linspace(min(V1, V2) * 0.8, max(V1, V2) * 1.2, 200)
    P = n_R_T / V

    fig, ax = new_figure()
    ax.plot(V, P, color="#0891b2", linewidth=2)
    ax.scatter([V1, V2], [P1, n_R_T / V2], color="#0f172a", zorder=5)
    ax.annotate("State 1", (V1, P1), textcoords="offset points", xytext=(6, 6), fontsize=8)
    ax.annotate("State 2", (V2, n_R_T / V2), textcoords="offset points", xytext=(6, 6), fontsize=8)
    style_axes(ax, "Isothermal Process (P-V Diagram)", "Volume (m^3)", "Pressure (Pa)")
    fig.tight_layout()

    return (f"P2 = P1*V1/V2 = {n_R_T/V2:,.4f} Pa\n"
            f"Work done by gas W = nRT*ln(V2/V1) = {W:,.4f} J"), fig


def calc_otto_cycle(v):
    r, gamma = v["r"], v["gamma"]
    eta = 1 - 1 / (r ** (gamma - 1))
    return (f"Otto cycle efficiency = 1 - (1/r)^(gamma-1) = {eta:.4f} "
            f"({eta*100:.2f} %)"), None


def calc_reynolds(v):
    rho, vel, D, mu = v["rho"], v["vel"], v["D"], v["mu"]
    if mu == 0:
        raise ValueError("Viscosity cannot be zero.")
    Re = (rho * vel * D) / mu
    regime = "Laminar" if Re < 2300 else ("Transitional" if Re < 4000 else "Turbulent")
    return f"Reynolds number Re = rho*v*D/mu = {Re:,.2f}  -> {regime} flow", None

