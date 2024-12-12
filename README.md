# Python Function: Average Calculation with Empty List Handling

This repository demonstrates a common error in Python functions: improper handling of empty input lists. The `calculate_average` function initially returns 0 when an empty list is passed, but this can mask errors and lead to unexpected behavior.

The solution provides a more robust approach by raising a `ValueError` when an empty list is given. This improves clarity and ensures that errors are handled gracefully. This example showcases the importance of robust error handling in Python.

## Bug
The original `calculate_average` function returns 0 when the input list is empty. This behavior may be unexpected, as it can mask errors in other parts of a program.