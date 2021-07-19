import pytest
import re
import src.exercise
from tests.input_data import input_values

# Define the parametrization based on the inputs from the input_data file
@pytest.mark.parametrize('value, result, message', input_values)

def test_exercise(value, result, message):
    output = []

    def mock_input(input_s=None):
        if input_s is not None:
            output.append(input_s)
        else:
            output.append("")

        return value.pop(0)

    src.exercise.input = mock_input

    src.exercise.print = lambda *args: output.append(" ".join(map(str, args)))

    src.exercise.main()

    for i in range(0, len(result)):
        assert result[i].match(output[i]) is not None, message #is not None

