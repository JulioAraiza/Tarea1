import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["20"],
        # Outputs
        [re.compile(".*"), re.compile(".*1[.]?0?0?$")],
        # Error message
        "Recuerda que un dolar equivale a 20 pesos. No imprimas nada despues de escribir la cantidad de dolares"
    ),
    (
        # Inputs
        ["789"],
        # Outputs
        [re.compile(".*"), re.compile(".*39[.]45$")],
        # Error message
        "Recuerda que un dolar equivale a 20 pesos. No imprimas nada despues de escribir la cantidad de dolares"
    ),    (
        # Inputs
        ["15975"],
        # Outputs
        [re.compile(".*"), re.compile(".*798[.]75$")],
        # Error message
        "Recuerda que un dolar equivale a 20 pesos. No imprimas nada despues de escribir la cantidad de dolares"
    ),    (
        # Inputs
        ["78596"],
        # Outputs
        [re.compile(".*"), re.compile(".*3929[.]80?$")],
        # Error message
        "Recuerda que un dolar equivale a 20 pesos. No imprimas nada despues de escribir la cantidad de dolares"
    ),
]
