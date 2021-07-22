import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["10"],
        # Outputs
        [re.compile(".*"), re.compile(".*314[.]15?")],
        # Error message
        "Revisa los tipos de dato de tus variables y recuerda utilizar el valor de pi en la formula"
    ),
    (
        # Inputs
        ["14"],
        # Outputs
        [re.compile(".*"), re.compile(".*615[.]7")],
        # Error message
        "Revisa los tipos de dato de tus variables y recuerda utilizar el valor de pi en la formula"
    ),
    (
        # Inputs
        ["8.5"],
        # Outputs
        [re.compile(".*"), re.compile(".*226[.]98?")],
        # Error message
        "Revisa los tipos de dato de tus variables y recuerda utilizar el valor de pi en la formula"
    ),
(
        # Inputs
        ["1.55"],
        # Outputs
        [re.compile(".*"), re.compile(".*7[.]54?")],
        # Error message
        "Revisa los tipos de dato de tus variables y recuerda utilizar el valor de pi en la formula"
    ),
]
