import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["5"],
        # Outputs
        [re.compile(".*"), re.compile(".*25[.]?0?$")],
        # Error message
        "Revisa la formula del area del cuadrado"
    ),
    (
        # Inputs
        ["8"],
        # Outputs
        [re.compile(".*"), re.compile(".*64[.]?0?$")],
        # Error message
        "Revisa la formula del area del cuadrado"
    ),
    (
        # Inputs
        ["1.5"],
        # Outputs
        [re.compile(".*"), re.compile(".*2[.]25$")],
        # Error message
        "Revisa la formula del area del cuadrado y el tipo de variable, recuerda que el resultado puede incluir decimales"
    ),
(
        # Inputs
        ["0.6"],
        # Outputs
        [re.compile(".*"), re.compile(".*0[.]36")],
        # Error message
        "Revisa la formula del area del cuadrado y el tipo de variable, recuerda que el resultado puede incluir decimales"
    ),
]
