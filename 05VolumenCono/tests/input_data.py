import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["10", "5"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*523[.]59?")],
        # Error message
        "Revisa la formula del cono y recuerda utilizar el valor de pi. Los resultados deben contener al menos un decimal"
    ),
    (
        # Inputs
        ["2", "8"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*33[.]51?")],
        # Error message
        "Revisa la formula del cono y recuerda utilizar el valor de pi. Los resultados deben contener al menos un decimal"
    ),
    (
        # Inputs
        ["1", "2"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*2[.]09?")],
        # Error message
        "Revisa la formula del cono y recuerda utilizar el valor de pi. Los resultados deben contener al menos un decimal"
    ),
(
        # Inputs
        ["1.55", "2.45"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*6[.]16?")],
        # Error message
        "Revisa la formula del cono y recuerda utilizar el valor de pi. Los resultados deben contener al menos un decimal"
    ),
]
