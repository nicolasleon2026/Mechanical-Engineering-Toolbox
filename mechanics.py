import math
import numpy as np

from plots import new_figure, style_axes
from matplotlib.figure import Figure


def calc_axial_stress(v):
    F, A = v["F"], v["A"]
    sigma = F / A
    return (f"Axial stress sigma = F / A = {sigma:,.3f} Pa  "
            f"({sigma/1e6:,.4f} MPa)"), None


def calc_axial_strain(v):
    dL, L = v["dL"], v["L"]
    eps = dL / L
    return f"Axial strain epsilon = dL / L = {eps:.6f}  ({eps*100:.4f} %)", None


def calc_youngs_modulus(v):
    stress, strain = v["stress"], v["strain"]
    if strain == 0:
        raise ValueError("Strain cannot be zero.")
    E = stress / strain
    return (f"Young's modulus E = stress / strain = {E:,.3f} Pa  "
            f"({E/1e9:,.4f} GPa)"), None


def calc_shear_stress(v):
    V, A = v["V"], v["A"]
    tau = V / A
    return (f"Shear stress tau = V / A = {tau:,.3f} Pa  "
            f"({tau/1e6:,.4f} MPa)"), None


def calc_bending_stress(v):
    M, c, I_area = v["M"], v["c"], v["I"]
    sigma = M * c / I_area
    return (f"Bending stress sigma = M*c / I_area = {sigma:,.3f} Pa  "
            f"({sigma/1e6:,.4f} MPa)"), None


def calc_torsional_shear(v):
    T, r, J = v["T"], v["r"], v["J"]
    tau = T * r / J
    return (f"Torsional shear stress tau = T*r / J = {tau:,.3f} Pa  "
            f"({tau/1e6:,.4f} MPa)"), None


def calc_torque(v):
    F, r = v["F"], v["r"]
    T = F * r
    return f"Torque T = F * r = {T:,.3f} N-m", None


def calc_spring_force(v):
    k, x = v["k"], v["x"]
    F = k * x
    PE = 0.5 * k * x ** 2
    return (f"Spring force F = k*x = {F:,.3f} N\n"
            f"Elastic PE stored = 0.5*k*x^2 = {PE:,.3f} J"), None


def calc_factor_of_safety(v):
    Sy, sigma = v["Sy"], v["sigma"]
    if sigma == 0:
        raise ValueError("Applied stress cannot be zero.")
    fos = Sy / sigma
    verdict = "SAFE" if fos >= 1 else "NOT SAFE (fails)"
    return f"Factor of Safety = Sy / sigma = {fos:,.3f}  -> {verdict}", None


def calc_beam_deflection(v):
    P, L, E, I_area = v["P"], v["L"], v["E"], v["I"]
    x = np.linspace(0, L, 200)
    y = np.where(
        x <= L / 2,
        (P * x * (3 * L ** 2 - 4 * x ** 2)) / (48 * E * I_area),
        (P * (L - x) * (3 * L ** 2 - 4 * (L - x) ** 2)) / (48 * E * I_area),
    )
    y_max = (P * L ** 3) / (48 * E * I_area)

    fig, ax = new_figure()
    ax.plot(x, -y * 1000, color="#2563eb", linewidth=2)
    ax.axhline(0, color="black", linewidth=0.8)
    style_axes(ax, "Simply Supported Beam Deflection (center point load)",
               "Position along beam (m)", "Deflection (mm)")
    fig.tight_layout()

    return (f"Max deflection at midspan = {y_max*1000:.4f} mm "
            f"({y_max:.6e} m)"), fig


def calc_free_fall(v):
    h, g = v["h"], v["g"]
    t = math.sqrt(2 * h / g)
    v_final = g * t

    tt = np.linspace(0, t, 200)
    yy = h - 0.5 * g * tt ** 2
    vv = g * tt

    fig = Figure(figsize=(5.2, 3.6), dpi=100)
    ax1 = fig.add_subplot(211)
    ax1.plot(tt, yy, color="#16a34a")
    style_axes(ax1, "Height vs Time", "", "Height (m)")
    ax2 = fig.add_subplot(212)
    ax2.plot(tt, vv, color="#dc2626")
    style_axes(ax2, "Velocity vs Time", "Time (s)", "Velocity (m/s)")
    fig.tight_layout()

    return (f"Fall time t = sqrt(2h/g) = {t:.4f} s\n"
            f"Impact velocity v = g*t = {v_final:.4f} m/s"), fig


def calc_projectile(v):
    v0, angle_deg, g = v["v0"], v["angle"], v["g"]
    angle = math.radians(angle_deg)
    t_flight = (2 * v0 * math.sin(angle)) / g
    max_height = (v0 ** 2 * math.sin(angle) ** 2) / (2 * g)
    max_range = (v0 ** 2 * math.sin(2 * angle)) / g

    t = np.linspace(0, t_flight, 200)
    x = v0 * math.cos(angle) * t
    y = v0 * math.sin(angle) * t - 0.5 * g * t ** 2

    fig, ax = new_figure()
    ax.plot(x, y, color="#7c3aed", linewidth=2)
    ax.fill_between(x, y, 0, color="#7c3aed", alpha=0.08)
    style_axes(ax, "Projectile Trajectory", "Horizontal distance (m)", "Height (m)")
    ax.set_ylim(bottom=0)
    fig.tight_layout()

    return (f"Time of flight = {t_flight:.4f} s\n"
            f"Max height = {max_height:.4f} m\n"
            f"Range = {max_range:.4f} m"), fig


def calc_work(v):
    F, d, theta = v["F"], v["d"], v["theta"]
    W = F * d * math.cos(math.radians(theta))
    return f"Work W = F*d*cos(theta) = {W:,.3f} J", None


def calc_kinetic_energy(v):
    m, vel = v["m"], v["v"]
    KE = 0.5 * m * vel ** 2
    return f"Kinetic energy KE = 0.5*m*v^2 = {KE:,.3f} J", None


def calc_power(v):
    W, t = v["W"], v["t"]
    if t == 0:
        raise ValueError("Time cannot be zero.")
    P = W / t
    return (f"Power P = W / t = {P:,.3f} W  ({P/745.7:.4f} hp)"), None


def calc_friction(v):
    mu, N = v["mu"], v["N"]
    f = mu * N
    return f"Friction force f = mu*N = {f:,.3f} N", None


def calc_gear_ratio(v):
    N1, N2, w1, T1 = v["N1"], v["N2"], v["w1"], v["T1"]
    if N2 == 0:
        raise ValueError("N2 cannot be zero.")
    ratio = N1 / N2
    w2 = w1 * ratio
    T2 = T1 / ratio
    return (f"Gear ratio (N1:N2) = {ratio:.4f}\n"
            f"Output speed w2 = {w2:,.3f} rpm\n"
            f"Output torque T2 = {T2:,.3f} N-m"), None

