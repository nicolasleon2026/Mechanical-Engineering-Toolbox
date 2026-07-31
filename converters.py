def make_linear_converter(units):
    """Builds a compute() function for a simple linear unit conversion."""
    def compute(v):
        value, u_from, u_to = v["value"], v["from_unit"], v["to_unit"]
        base = value * units[u_from]
        result = base / units[u_to]
        return f"{value:g} {u_from}  =  {result:.6g} {u_to}", None
    return compute


def compute_temperature(v):
    value, u_from, u_to = v["value"], v["from_unit"], v["to_unit"]


    if u_from == "C":
        k = value + 273.15
    elif u_from == "F":
        k = (value - 32) * 5 / 9 + 273.15
    else:
        k = value

    if u_to == "C":
        result = k - 273.15
    elif u_to == "F":
        result = (k - 273.15) * 9 / 5 + 32
    else:
        result = k

    return f"{value:g} deg{u_from}  =  {result:.4f} deg{u_to}", None



