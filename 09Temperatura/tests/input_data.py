import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["-40"],
        # Outputs
        [re.compile(".*"), re.compile(".*-40[.]?0?")],
        # Error message
        "Revisa la formula de conversion y recuerda que hay temeperaturas negativas y con valores decimales"
    ),
    (
        # Inputs
        ["85.7"],
        # Outputs
        [re.compile(".*"), re.compile(".*29[.]?8?3?")],
        # Error message
        "Revisa la formula de conversion y recuerda que hay temeperaturas negativas y con valores decimales"
    ),
    (
        # Inputs
        ["68"],
        # Outputs
        [re.compile(".*"), re.compile(".*20[.]?0?")],
        # Error message
        "Revisa la formula de conversion y recuerda que hay temeperaturas negativas y con valores decimales"
    ),
    (
        # Inputs
        ["2315.93"],
        # Outputs
        [re.compile(".*"), re.compile(".*1268[.]?8?5?")],
        # Error message
        "Revisa la formula de conversion y recuerda que hay temeperaturas negativas y con valores decimales"
    ),
]
