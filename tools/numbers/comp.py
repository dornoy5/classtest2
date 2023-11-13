from .simp import simp_function_called

def sumofdigits(number):
    if not simp_function_called:
        raise Exception("A function from simp module must be called first")
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total


def ispal(number):
    if not simp_function_called:
        raise Exception("A function from simp module must be called first")
    num_str = str(number)
    return num_str == num_str[::-1]

