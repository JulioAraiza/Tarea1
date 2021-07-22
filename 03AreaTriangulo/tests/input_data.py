import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["7", "5"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*17[.]5$")],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la fórmula del área del triángulo."
    ),
    (
        # Inputs
        ["10", "8"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*40[.]?0?$")],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la fórmula del área del triángulo."
    ),
    (
        # Inputs
        ["1.5", "2.75"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*2[.]0625$")],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la fórmula del área del triángulo."
    ),
(
        # Inputs
        ["5", "7"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*17[.]5$")],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la fórmula del área del triángulo."
    ),
]
