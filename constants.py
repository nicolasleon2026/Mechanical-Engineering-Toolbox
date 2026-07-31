R_UNIVERSAL = 8.314  
G_EARTH = 9.81       


LENGTH_UNITS = {
    "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
    "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mile": 1609.34,
}
MASS_UNITS = {
    "g": 0.001, "kg": 1.0, "metric ton": 1000.0,
    "lb": 0.453592, "oz": 0.0283495, "slug": 14.5939,
}
FORCE_UNITS = {
    "N": 1.0, "kN": 1000.0, "lbf": 4.44822, "dyne": 1e-5, "kgf": 9.80665,
}
PRESSURE_UNITS = {
    "Pa": 1.0, "kPa": 1000.0, "MPa": 1.0e6, "bar": 1.0e5,
    "atm": 101325.0, "psi": 6894.76, "mmHg": 133.322,
}
ENERGY_UNITS = {
    "J": 1.0, "kJ": 1000.0, "cal": 4.184, "kcal": 4184.0,
    "BTU": 1055.06, "kWh": 3.6e6, "ft-lb": 1.35582,
}
POWER_UNITS = {
    "W": 1.0, "kW": 1000.0, "hp (mech)": 745.7, "BTU/hr": 0.293071,
}
TORQUE_UNITS = {
    "N-m": 1.0, "lbf-ft": 1.35582, "lbf-in": 0.112985, "kgf-m": 9.80665,
}
AREA_UNITS = {
    "mm^2": 1e-6, "cm^2": 1e-4, "m^2": 1.0, "in^2": 0.00064516, "ft^2": 0.092903,
}
VOLUME_UNITS = {
    "mL": 1e-6, "L": 0.001, "m^3": 1.0, "gal (US)": 0.00378541, "ft^3": 0.0283168,
}
VELOCITY_UNITS = {
    "m/s": 1.0, "km/h": 0.277778, "mph": 0.44704, "ft/s": 0.3048,
}
DENSITY_UNITS = {
    "kg/m^3": 1.0, "g/cm^3": 1000.0, "lb/ft^3": 16.0185,
}
