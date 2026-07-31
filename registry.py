from mechanics import *
from thermo import *
from converters import *

from constants import *



CALCULATORS = {
    "Mechanics": [
        ("Axial Stress (sigma = F/A)",
         [("F", "Force", "float", 5000.0), ("A", "Cross-sectional Area (m^2)", "float", 0.0005)],
         calc_axial_stress),

        ("Axial Strain (epsilon = dL/L)",
         [("dL", "Change in Length (m)", "float", 0.002), ("L", "Original Length (m)", "float", 1.0)],
         calc_axial_strain),

        ("Young's Modulus (E = sigma/epsilon)",
         [("stress", "Stress (Pa)", "float", 2.0e8), ("strain", "Strain (dimensionless)", "float", 0.001)],
         calc_youngs_modulus),

        ("Shear Stress (tau = V/A)",
         [("V", "Shear Force (N)", "float", 3000.0), ("A", "Area (m^2)", "float", 0.0004)],
         calc_shear_stress),

        ("Bending Stress (sigma = Mc/I)",
         [("M", "Bending Moment (N-m)", "float", 500.0), ("c", "Distance to Neutral Axis (m)", "float", 0.05),
          ("I", "Moment of Inertia (m^4)", "float", 8.33e-6)],
         calc_bending_stress),

        ("Torsional Shear Stress (tau = Tr/J)",
         [("T", "Torque (N-m)", "float", 200.0), ("r", "Radius (m)", "float", 0.02),
          ("J", "Polar Moment of Inertia (m^4)", "float", 2.5e-7)],
         calc_torsional_shear),

        ("Torque (T = F x r)",
         [("F", "Force (N)", "float", 150.0), ("r", "Lever Arm Radius (m)", "float", 0.3)],
         calc_torque),

        ("Spring Force - Hooke's Law (F = kx)",
         [("k", "Spring Constant (N/m)", "float", 2500.0), ("x", "Displacement (m)", "float", 0.05)],
         calc_spring_force),

        ("Factor of Safety (FoS = Sy/sigma)",
         [("Sy", "Yield Strength (Pa)", "float", 2.5e8), ("sigma", "Applied Stress (Pa)", "float", 1.0e8)],
         calc_factor_of_safety),

        ("Beam Deflection - Simply Supported, Center Load  [plot]",
         [("P", "Point Load (N)", "float", 1000.0), ("L", "Beam Length (m)", "float", 2.0),
          ("E", "Elastic Modulus (Pa)", "float", 2.0e11), ("I", "Moment of Inertia (m^4)", "float", 8.33e-6)],
         calc_beam_deflection),

        ("Free Fall Motion  [plot]",
         [("h", "Drop Height (m)", "float", 20.0), ("g", "Gravity (m/s^2)", "float", G_EARTH)],
         calc_free_fall),

        ("Projectile Motion  [plot]",
         [("v0", "Launch Speed (m/s)", "float", 25.0), ("angle", "Launch Angle (deg)", "float", 45.0),
          ("g", "Gravity (m/s^2)", "float", G_EARTH)],
         calc_projectile),

        ("Work Done by a Force (W = Fd*cos(theta))",
         [("F", "Force (N)", "float", 100.0), ("d", "Displacement (m)", "float", 5.0),
          ("theta", "Angle Between F and d (deg)", "float", 0.0)],
         calc_work),

        ("Kinetic Energy (KE = 0.5mv^2)",
         [("m", "Mass (kg)", "float", 10.0), ("v", "Velocity (m/s)", "float", 8.0)],
         calc_kinetic_energy),

        ("Power (P = W/t)",
         [("W", "Work / Energy (J)", "float", 5000.0), ("t", "Time (s)", "float", 10.0)],
         calc_power),

        ("Friction Force (f = mu*N)",
         [("mu", "Coefficient of Friction", "float", 0.3), ("N", "Normal Force (N)", "float", 500.0)],
         calc_friction),

        ("Gear Ratio & Output Speed/Torque",
         [("N1", "Driver Gear Teeth", "float", 20.0), ("N2", "Driven Gear Teeth", "float", 60.0),
          ("w1", "Input Speed (rpm)", "float", 1200.0), ("T1", "Input Torque (N-m)", "float", 15.0)],
         calc_gear_ratio),
    ],

    "Thermodynamics": [
        ("Ideal Gas Law (PV = nRT)",
         [("solve_for", "Solve for", "choice", ["P", "V", "n", "T"]),
          ("P", "Pressure (Pa)", "float", 101325.0), ("V", "Volume (m^3)", "float", 0.024),
          ("n", "Moles (mol)", "float", 1.0), ("T", "Temperature (K)", "float", 293.15)],
         calc_ideal_gas),

        ("Carnot Efficiency",
         [("Th", "Hot Reservoir Temp (K)", "float", 600.0), ("Tc", "Cold Reservoir Temp (K)", "float", 300.0)],
         calc_carnot),

        ("Heat Conduction (Fourier's Law)",
         [("k", "Thermal Conductivity (W/m-K)", "float", 45.0), ("A", "Area (m^2)", "float", 1.0),
          ("dT", "Temperature Difference (K)", "float", 50.0), ("L", "Thickness (m)", "float", 0.01)],
         calc_conduction),

        ("Convective Heat Transfer",
         [("h", "Convection Coefficient (W/m^2-K)", "float", 25.0), ("A", "Area (m^2)", "float", 2.0),
          ("dT", "Temperature Difference (K)", "float", 30.0)],
         calc_convection),

        ("Sensible Heat (Q = mcdT)",
         [("m", "Mass (kg)", "float", 2.0), ("c", "Specific Heat (J/kg-K)", "float", 4186.0),
          ("dT", "Temperature Change (K)", "float", 15.0)],
         calc_sensible_heat),

        ("Linear Thermal Expansion",
         [("alpha", "Coefficient of Expansion (1/K)", "float", 1.2e-5),
          ("L0", "Original Length (m)", "float", 2.0), ("dT", "Temperature Change (K)", "float", 40.0)],
         calc_thermal_expansion),

        ("First Law of Thermodynamics (dU = Q - W)",
         [("Q", "Heat Added to System (J)", "float", 2000.0), ("W", "Work Done by System (J)", "float", 800.0)],
         calc_first_law),

        ("Enthalpy Change (dH = m*cp*dT)",
         [("m", "Mass (kg)", "float", 1.5), ("cp", "Specific Heat at Const. Pressure (J/kg-K)", "float", 1005.0),
          ("dT", "Temperature Change (K)", "float", 25.0)],
         calc_enthalpy),

        ("Isothermal Process P-V Diagram  [plot]",
         [("P1", "Initial Pressure (Pa)", "float", 200000.0), ("V1", "Initial Volume (m^3)", "float", 0.01),
          ("V2", "Final Volume (m^3)", "float", 0.03)],
         calc_isothermal_pv),

        ("Otto Cycle Efficiency",
         [("r", "Compression Ratio", "float", 8.0), ("gamma", "Specific Heat Ratio (cp/cv)", "float", 1.4)],
         calc_otto_cycle),

        ("Reynolds Number (Fluid Flow Regime)",
         [("rho", "Fluid Density (kg/m^3)", "float", 998.0), ("vel", "Flow Velocity (m/s)", "float", 1.5),
          ("D", "Pipe Diameter (m)", "float", 0.05), ("mu", "Dynamic Viscosity (Pa-s)", "float", 0.001)],
         calc_reynolds),
    ],

    "Unit Conversion": [
        ("Length Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(LENGTH_UNITS)),
          ("to_unit", "To", "choice", list(LENGTH_UNITS))],
         make_linear_converter(LENGTH_UNITS)),

        ("Mass Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(MASS_UNITS)),
          ("to_unit", "To", "choice", list(MASS_UNITS))],
         make_linear_converter(MASS_UNITS)),

        ("Force Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(FORCE_UNITS)),
          ("to_unit", "To", "choice", list(FORCE_UNITS))],
         make_linear_converter(FORCE_UNITS)),

        ("Pressure Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(PRESSURE_UNITS)),
          ("to_unit", "To", "choice", list(PRESSURE_UNITS))],
         make_linear_converter(PRESSURE_UNITS)),

        ("Temperature Converter",
         [("value", "Value", "float", 25.0), ("from_unit", "From", "choice", ["C", "F", "K"]),
          ("to_unit", "To", "choice", ["C", "F", "K"])],
         compute_temperature),

        ("Energy Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(ENERGY_UNITS)),
          ("to_unit", "To", "choice", list(ENERGY_UNITS))],
         make_linear_converter(ENERGY_UNITS)),

        ("Power Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(POWER_UNITS)),
          ("to_unit", "To", "choice", list(POWER_UNITS))],
         make_linear_converter(POWER_UNITS)),

        ("Torque Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(TORQUE_UNITS)),
          ("to_unit", "To", "choice", list(TORQUE_UNITS))],
         make_linear_converter(TORQUE_UNITS)),

        ("Area Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(AREA_UNITS)),
          ("to_unit", "To", "choice", list(AREA_UNITS))],
         make_linear_converter(AREA_UNITS)),

        ("Volume Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(VOLUME_UNITS)),
          ("to_unit", "To", "choice", list(VOLUME_UNITS))],
         make_linear_converter(VOLUME_UNITS)),

        ("Velocity Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(VELOCITY_UNITS)),
          ("to_unit", "To", "choice", list(VELOCITY_UNITS))],
         make_linear_converter(VELOCITY_UNITS)),

        ("Density Converter",
         [("value", "Value", "float", 1.0), ("from_unit", "From", "choice", list(DENSITY_UNITS)),
          ("to_unit", "To", "choice", list(DENSITY_UNITS))],
         make_linear_converter(DENSITY_UNITS)),
    ],
}

TOTAL_CALCULATORS = sum(len(v) for v in CALCULATORS.values())
