import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["100", "200", "300"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*60[.]?0?$")],
        # Error message
        "Revisa la variable donde guardas el acumulado de las ventas"
    ),
    (
        # Inputs
        ["20", "15", "60"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*9[.]5$")],
        # Error message
        "La comision incluye los centavos"
    ),
    (
        # Inputs
        ["2000", "500", "70"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*257[.]?0?")],
        # Error message
        "Revisa la variable donde guardas el acumulado de las ventas"
    ),
(
        # Inputs
        ["10", "80", "20"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*11[.]?0?")],
        # Error message
        "Recuerda que la comision es el 10% del total de las ventas"
    ),
]
