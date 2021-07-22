import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["1024"],
        # Outputs
        [re.compile(".*"), re.compile(".*1048576[.]?0?"), re.compile(".*1073741824[.]?0?"), re.compile(".*1099511627776[.]?0?")],
        # Error message
        "Revisa las equivalencias. Recuerda imprimir al menos dos decimales en caso de ser necesario"
    ),
    (
        # Inputs
        ["64"],
        # Outputs
        [re.compile(".*"), re.compile(".*65536[.]?0?"), re.compile(".*67108864[.]?0?"), re.compile(".*68719476736[.]?0?")],
        # Error message
        "Revisa las equivalencias. Recuerda imprimir al menos dos decimales en caso de ser necesario"
    ),
    (
        # Inputs
        ["8"],
        # Outputs
        [re.compile(".*"), re.compile(".*8192[.]?0?"), re.compile(".*8388608[.]?0?"), re.compile(".*8589934592[.]?0?")],
        # Error message
        "Revisa las equivalencias. Recuerda imprimir al menos dos decimales en caso de ser necesario"
    ),
    (
        # Inputs
        ["0.5"],
        # Outputs
        [re.compile(".*"), re.compile(".*512[.]?0?"), re.compile(".*524288[.]?0?"), re.compile(".*536870912[.]?0?")],
        # Error message
        "Revisa las equivalencias. Recuerda imprimir al menos dos decimales en caso de ser necesario"
    ),
(
        # Inputs
        ["1.24"],
        # Outputs
        [re.compile(".*"), re.compile(".*1269[.]76$"), re.compile(".*1300234[.]24$"), re.compile(".*1331439861[.]?7?6?")],
        # Error message
        "Revisa las equivalencias. Recuerda imprimir al menos dos decimales en caso de ser necesario"
    )
]
