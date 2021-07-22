import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["1", "2", "3", "4"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*8[.]50?")],
        # Error message
        "Recuerda aplicar el descuento y que los precios pueden tener centavos"
    ),
    (
        # Inputs
        ["156", "4564", "4664", "45"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*8014[.]65$")],
        # Error message
        "Recuerda aplicar el descuento y que los precios pueden tener centavos"
    ),
    (
        # Inputs
        ["500", "700", "96.85", "78.15"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*1168[.]75$")],
        # Error message
        "Recuerda aplicar el descuento y que los precios pueden tener centavos"
    ),
    (
        # Inputs
        ["7898", "956", "452", "52"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*7954[.]30?$")],
        # Error message
        "Recuerda aplicar el descuento y que los precios pueden tener centavos"
    ),
]
