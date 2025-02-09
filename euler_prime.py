import math
import time


def is_prime(number):
    """
    Any factor larger than √n must have a corresponding factor smaller than sqrt(n)
    Only testing odd numbers (step=2) - even divisibility checked first

    :param number: number to check for primality
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    num_sqrt = math.isqrt(number)
    for i in range(3, num_sqrt + 1, 2):
        if number % i == 0:
            return False
    return True


def digits_to_number(digits: list):
    """Convert a list of digits to a number
    e.g. [1, 2, 3] -> 123
    Using power of 10 for each position

    :param digits: list of digits
    """

    number = 0

    power = len(digits) - 1
    for digit in digits:
        number += digit * (10 ** power)
        power -= 1
    return number


def number_to_digits(number):
    """
    Convert a number to a list of digits
    e.g. 123 -> [1, 2, 3]
    Extracting digits using modulo 10

    :param number: number to convert
    """
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number //= 10
    return digits


def find_prime_in_window(digits, window_size):
    """
    Find the first prime number in a window of digits
    We use a sliding window of size window_size to generate numbers from the digits
    If a prime number is found, return it immediately

    :param digits: list of digits
    :param window_size: size of the window
    """

    n = len(digits)
    for i in range(n - window_size + 1):
        window = digits[i:i + window_size]
        number = digits_to_number(window)

        if is_prime(number):
            return number
    return None


def generate_e_digits(n):
    """
    Using scaled integer arithmetic to avoid floating point precision issues
    Adding extra working precision (n+10) to ensure accuracy
    Returning slightly more digits than requested for safety

    :param n: number of digits to generate
    :return: list of digits
    """

    # We'll use more precision than requested to ensure accuracy
    working_precision = n + 10  # Add extra digits for precision
    precision = 10 ** working_precision

    # Start with 2.0 * precision
    e = 2 * precision

    factorial = 1
    term = precision  # Start with 1.0 * precision
    i = 1

    while term > 0:
        factorial *= i
        term = precision // factorial
        e += term
        i += 1

    digits = number_to_digits(e)[1:]  # Skip the '2'
    return digits[:n + 5]  # Return a few extra digits just in case

def find_first_prime_in_e(num_digits):
    """
    Generating more digits than needed to ensure accuracy
    We generate the digits of e using a series expansion and then search for a prime number

    :param num_digits: number of digits to search for
    """
    extra_digits = 100 # Extra digits to ensure we find a prime
    e_digits = generate_e_digits(num_digits + extra_digits)
    return find_prime_in_window(e_digits, num_digits)


# Run the solution and measure the time taken
n = 10
start = time.time()
result = find_first_prime_in_e(n)
end = time.time()

print(f"First {n}-digit prime in e: {result}")
print(f"Time taken: {end - start} seconds")

#First 10-digit prime in e: 7427466391
#Time taken: 0.0023949146270751953 seconds
