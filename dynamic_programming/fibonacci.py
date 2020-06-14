import time
import helper

"""
    Fibonacci Function using dynamic programming
    The Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

    In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
"""


def fibonacci_without_dynamic(number) -> int:
    """
    This function calculate in recursive mode the value of the required position.
    E.g.: position 10 result 55
    E.g.: position 35 result 9227465

    Parameters:
        int number

    Returns:
        int
    """
    if type(number) != int or number < 0:
        raise ValueError('Number must be integer and positive')

    if number <= 1:
        return number
    elif number == 2:
        return 1
    else:
        return fibonacci_without_dynamic(number - 1) + fibonacci_without_dynamic(number - 2)


fibonacci_sequence = {}

def fibonacci_with_dynamic(number) -> int:
    """
    This function calculate in recursive mode the value of the required position.
        E.g.: position 10 result 55
        E.g.: position 35 result 9227465

    The difference from this function and the one without the dynamic programing is:
    We store the result of the calculations into a variable, in this way, we don't need to calculate
    more than 1 time the same result.
    Once a specific position is calculated is stored and used all the times that is required.

    Parameters:
        int number (must be positive number)

    Returns:
        int
    """
    if type(number) != int or number < 0:
        raise ValueError('Number must be integer and positive')

    if number in fibonacci_sequence:
        return fibonacci_sequence[number]

    if number <= 1:
        return number
    elif number == 2:
        return 1
    else:
        calculation = fibonacci_with_dynamic(number - 1) + fibonacci_with_dynamic(number - 2)

    fibonacci_sequence[number] = calculation

    return calculation


# without dynamic programming
start = time.time()
print(fibonacci_without_dynamic(35))
helper.execution_time(start)

# with dynamic programing
start = time.time()
print(fibonacci_with_dynamic(35))
helper.execution_time(start)
