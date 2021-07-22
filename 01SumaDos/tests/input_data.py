import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["7", "5"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*12[.]?0?$")],
        # Error message
        "Verifica el funcionamiento de tu programa"
    ),
    (
        # Inputs
        ["10", "8"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*18[.]?0?$")],
        # Error message
        "Verifica el funcionamiento de tu programa"
    ),
    (
        # Inputs
        ["1.5", "2.75"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*4[.]25$")],
        # Error message
        "Verifica el funcionamiento de tu programa, recuerda que puede sumar numeros decimales"
    ),
(
        # Inputs
        ["20", "8.9"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*28[.]9$")],
        # Error message
        "Verifica el funcionamiento de tu programa, recuerda que puede sumar numeros decimales"
    ),
]
