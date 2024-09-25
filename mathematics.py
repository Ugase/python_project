"""
Mathematics Module
==================
by Ugase (github)

In almost every function there is a `print_statement` parameter. Heres what it means:
Whether it should print details and return the answer or just return the answer

When using a fraction returning function
it returns a list. The first item in the list
represents the numerator and the second one represents
the denomenator.

When a fraction returning function takes 
n and d or n, d, n2, d2

n and d mean numerator and denomenator
while
n, d, n2, d2 mean 2 fractions
n and d is the first fraction n2 and d2 is the second fraction
"""

import math
from decimal import Decimal as D
from functools import reduce
from math import sqrt, gcd

typing_speed_average = 0.13
e = 2.718281828459045
pi = 3.141592653589793
tau = 6.28210184121061


class FactorialError(Exception):
    """For `factorial` function"""


class FactorsError(Exception):
    """For the `factors` function"""


class FactorizationError(Exception):
    """For the `factorization` function"""


class MixedFractionError(Exception):
    """For the `improper_fraction` function"""

def rb(it: list):
    return str(it).replace("[", "").replace("]", "")

def simplify(n: int, d: int, print_statement=True):
    """
    Simplify's Fractions
    @param n - is numerator
    @param d - is denomenator
    """
    if d == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    greatest_common_divisor = gcd(n, d)
    k = [n // greatest_common_divisor, d // greatest_common_divisor]
    if print_statement:
        print(f"{k[0]}\n-\n{k[1]}")
    return k


def plus_fractions(n: int, d: int, n2: int, d2: int, print_statement=True):
    """Finds the sum of two fractions"""
    c = (n * d2) + (n2 * d)
    g = d * d2
    if print_statement:
        print(f"Result: {c/g} or {c}/{g}")
    return [c, g]


def multiply_fractions(n: int, d: int, n2: int, d2: int, print_statement=True):
    """Finds the product of two fractions"""
    a = n * n2
    b = d * d2
    if print_statement:
        print(f"Result: {a}/{b}")
    return [a, b]


def divide_fractions(n: int, d: int, n2: int, d2: int, print_statement=True):
    """Divdes two fractions"""
    print(
        "Change it to mutiply but in the second fraction numerator is now in denominator and vice-versa"  # noqa: E501
    )
    multiply_fractions(n, d, d2, n2, print_statement)


def mixed_fraction(
    big_boy: int,
    small_boy_one_or_numerator: int,
    small_boy_two_or_denomenator: int,
    print_statement=True,
):
    """Changes mixed fraction to improper fraction
    @param big_boy - Whole number
    @param small_boy_one_or_numerator - Mixed fraction numerator
    @param small_boy_two_or_denomenator - Mixed fraction denomenator
    """
    a = big_boy * small_boy_two_or_denomenator + small_boy_one_or_numerator
    b = [a, small_boy_two_or_denomenator]
    if print_statement:
        p = rb(b)
        print(f"Improper fraction: {p}")
    return b


def average(x: list[int], detail=False, print_statement=True):
    """
    Finds the average of `x`
    """
    if not len(x):
        return 0
    le = rb(x)
    c = sum(x)
    average_num = c / len(x)
    if print_statement:
        if detail:
            print(
                f"""Average of {le} is {average_num} 
                The length of list provided is {len(x)} 
                And the sum of all intergers in a list is {c}"""
            )
        else:
            print(f"Average of {le} is {average_num}")
    return average_num


def factors(x: int, print_statement=True):
    """
    Finds the factors of `x` and
    returns it


    >>> factors(8)
    The Factors of 8 are 1, 2, 4, 8
    [1, 2, 4, 8]

    >>> x = factors(100, False)
    >>> x[5]
    20

    >>> factors(60)
    The Factors of 60 are 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60
    [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]

    >>> factors(0)
    File "~\Dev\mathematics.py", line 156, in factors
        raise FactorsError("Factors of {x} is unknown")
    FactorsError: Factors of 0 is unknown
    """  # noqa: E501

    if x <= 0:
        raise FactorsError(f"Factors of {x} is unknown")
    result = [i for i in range(1, x) if x % i == 0]
    result.append(x)
    if print_statement:
        p = rb(result)
        print(f"The Factors of {x} are {p}")

    return result


def check_prime(a, print_statement=True):
    """Checks if `a` is a prime"""
    if len(factors(a, False)) == 2:
        if print_statement:
            print("The Number is a prime!")
        return True
    else:
        if print_statement:
            print("The Number is not a prime :(")
        return False


def list_of_prime(n, print_statement=True):
    """Finds a list of primes up to `n`"""
    n += 1
    primes = [i for i in range(1, n) if check_prime(i, False)]
    if print_statement:
        p = rb(primes)
        print(f"The list of prime numbers up to {n} is {p}")
    return primes

# Basiclly math.gcd
def hcf(a: int, b: int, print_statment=True):
    """Finds the HCF of a, b"""
    c, d = factors(a, False), factors(b, False)
    g = 0
    if a == b:
        if print_statment:
            print(f"The Hcf of {a} and {b} is {c[-1]}")
        return max(c)
    if check_prime(a, False) or check_prime(b, False):
        if print_statment:
            print(f"The Hcf of {a} and {b} is 1")
        return 1
    for i in c:
        for x in d:
            if i == x:
                g = i
    if print_statment:
        print(f"The Hcf of {a} and {b} is {g}")
    return g


def multiply_mixed_fractions_with_numbers(
    x: int, n: int, d: int, a: int, print_statement=True
):
    """
    @param x - is the whole number
    @param n - is numerator of mixed fraction
    @param d - is denomenator of mixed fraction
    @param a - the number to multiply with the mixed fraction
    """

    b = mixed_fraction(x, n, d, False)
    y = (a / hcf(b[1], a, False)) * b[0]
    if print_statement:
        print(f"The answer is {y}")
    return y


def hamming_codes(array, print_statment=True):
    """Error correction

    @param array - An array of Bits
    """
    error = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(array) if bit]) - 1
    if print_statment:
        print(error)
        print(bin(error).replace("0b", ""))
    return error


def multiples(integer: int, limit: int, print_statement=True):
    """Finds the list of mutiples of `integer` with a limit of how many multiples of `limit`

    @param integer - The integer to find multiples of
    @param limit - Limit to how many multiples
    """  # noqa: E501
    multi = [integer * i for i in range(1, limit + 1)]
    if print_statement:
        p = rb(multi)
        print(f"The list of multiples of {integer} with the limit of {limit} is {p}")
    return multi


def is_even(x, print_statement=True):
    """Checks if `x` is even"""
    if x % 2 == 0:
        if print_statement:
            print("Is Even!")
        return True
    else:
        if print_statement:
            print("Is Odd!")
        return False


def fibonacci(limit, print_statement=True):
    """Lists fibonacci numbers with a limit of `limit`"""
    a, b = 0, 1
    c = []
    while a < limit:
        c.append(a)
        if print_statement:
            print(a)
        a, b = b, a + b
    return c


def lcm(a, b, print_statement=True):
    """Finds the lcm of `a, b`"""
    d_top = a * b
    d_bottom = hcf(a, b, False)
    answer = d_top // d_bottom
    if print_statement:
        print(f"The Lcm of {a}, {b} is {answer}")
    return answer


def add_all_values(n, print_statement=True):
    """Finds the sum of all values leading up to `n`
    using the formula:
    n x (n + 1) / 2
    """
    ans = n * (n + 1) / 2
    if print_statement:
        print(f"The sum of all values leading up to {n} is {ans}")
    return ans


def percentage(n, d, detail=False, print_statement=True):
    """Finds percentage of a fraction"""
    hun = 100 / d
    top = float(n * hun)
    if print_statement:
        print(f"The answer is {top} over 100, or {top}%")
        if detail:
            print(
                f"""The answer is {round(top)} over 100, or {round(top)}%
                Details:
                Number used for multiplication: {hun}
                Better approximation percentage: {top}"""
            )
    return top


def factorial(n: int, print_statement=True):
    """
    Finds the factorial of `n`.

    Negetive numbers are not allowed
    """
    if n == 0:
        if print_statement:
            print("The factorial of 0 is 1")
        return 1
    if n < 0:
        raise FactorialError("Factorial doesn't support negetive numbers")
    if n + 1 == n:
        raise OverflowError("n to large")
    if type(n) != int:
        raise FactorialError("Must be a integer")
    output = 1
    for o in range(1, n+1):
        output *= o
    if print_statement:
        print(f"The Factorial of {n} is {output}")
    return output


def product(*args, print_statement=False):
    """
    Returns the product of all the items in an iterable.
    If the input is not a list or a tuple only intergers or floats!!
    Python will convert it into a tuple.
    """
    for i in args:
        if i != int or i != float:
            raise TypeError("Only ints or floats")
    pro = 1
    for i in args:
        if isinstance(i, (list, tuple)):
            for o in i:
                pro *= o
        if type(i) == int and i != 0:
            pro *= i
    if print_statement:
        prod = str(args).replace("(", "").replace(")", "")
        print(f"The product of {prod} is {pro}")
    return pro


def improper_fraction(n, d, print_statement=True):
    """Changes improper fraction to mixed fraction

    The return value is [whole_number, mixed_fraction_numerator, d]
    """

    if n > d:
        whole_number = n // d
        mixed_fraction_numerator = n % d
        if print_statement:
            print(
                f"Whole number: {whole_number}, Mixed fraction numerator: {mixed_fraction_numerator}, Mixed fraction denomerator: {d}"  # noqa: E501
            )
        return [whole_number, mixed_fraction_numerator, d]
    elif n == d:
        print(f"{n} over {d} is 1")
    else:
        raise MixedFractionError("It's a proper fraction")


def factorization(x:int, print_statement=True):
    """Finds the prime factors of `x`"""
    prime_factors = []
    n = x
    o = list_of_prime(x, False)
    if x <= 0:
        raise FactorizationError("The input must be a positive integer")
    while n != 1:
        for i in o:
            if n % i == 0:
                n //= i
                prime_factors.append(i)
                break
    if print_statement:
        p = rb(prime_factors)
        d = p.replace(",", " x")
        print(f"The prime factors of {x} are {p} or {d}")
    return prime_factors


def square(x, print_statement=True):
    """Find the square of `x`"""
    square_x = x * x
    if print_statement:
        print(f"The square of {x} is {square_x}")
    return square_x


def list_of_squares(limit, print_statement=True):
    """Finds a list of squares with a limit of `limit`"""
    list_of_square = [square(i, False) for i in range(1, limit + 1)]
    if print_statement:
        p = rb(list_of_square)
        print(f"The list of square up to {limit} is {p}")
    return list_of_square


def list_of_even(x, print_statement=True):
    """Generate a list of even numbers up to `x`"""
    even_num_list = [i for i in range(1, x + 1) if is_even(i, False)]
    if print_statement:
        p = rb(even_num_list)
        print(f"The list of even number up to {x} is {p}")
    return even_num_list


def list_of_odd(x, print_statement=True):
    """Generate a list of odd numbers up to `x`"""
    odd_num_list = [i for i in range(1, x + 1) if not is_even(i)]
    if print_statement:
        p = rb(odd_num_list)
        print(f"The list of odd number up to {x} is {p}")
    return odd_num_list


def square_root(n, print_statement=True):
    """Finds the square root of `n`"""
    return nth_root(n, 2, print_statement)


def perfect_square(x, print_statement=True):
    """Checks if x is a perfect square"""
    ps = True
    if type(square_root(x, False)) == float:
        ps = not ps
    if print_statement:
        if ps:
            print(f"{x} is a perfect square")
        else:
            print(f"{x} is not a perfect square")


def nth_root(x, n, print_statement=True):
    """Finds the nth root of `x`"""
    root = x**0.5 if n == 2 else x ** (1.0 / n)
    if root == int(root):
        root = int(root)
    if print_statement:
        print(f"The {n}th root of {x} is {root}")
    return root


def cube_root(x, print_statement=True):
    """Find the cube root of x"""
    return nth_root(x, 3, print_statement)


def perfect_cube(x, print_statement=True):
    """Checks if `x` is a perfect cube"""
    ps = True
    if type(cube_root(x, False)) == float:
        ps = not ps
    if print_statement:
        if ps:
            print(f"{x} is a perfect cube")
        if not ps:
            print(f"{x} is not a perfect cube")


def cube(x, print_statement=True):
    """Finds the cube of x"""
    cube_x = x * x * x
    if print_statement:
        print(f"The cube of x is {cube_x}")
    return cube_x


def list_of_cubes(limit, print_statement=True):
    """Finds a list of cubes with a limit of `limit`"""
    list_of_cube = [cube(i) for i in range(1, limit + 1)]
    if print_statement:
        p = rb(list_of_cube)
        print(f"The list of cube up to {limit} is {p}")
    return list_of_cube


def find_between_values(x: int, y: int, print_statement=True):
    """Finds values between `x` and `y`"""
    try:
        assert type(x) == int and type(y) == int
    except AssertionError:
        print("The values must be an integer")
        return False
    if x > y:
        raise ValueError("Min can't be bigger than max")

    if x == y and print_statement:
        print(f"The values between {x} and {y} is {y}")
        return y
    values = list(range(x, y))
    del values[0]
    if print_statement:
        p = rb(values)
        print(f"The values between {x} and {y} is {p}")


def list_of_factorial(x, print_statement=True):
    """Get a list of factorial up to `x`"""
    list_factorial = [factorial(i, False) for i in range(x + 1)]
    if print_statement:
        p = rb(list_factorial)
        print(f"The List of factorial up to {x} is {p}")
    return list_factorial


def shift_bits_left(x: int, n: int, print_statement=True):
    """Shift the bits of `x`, `n` to the left"""
    if n < 0:
        raise ValueError("negative shift count")
    shifted_bits = x * 2**n
    if print_statement:
        print(f"The number is now {shifted_bits}")
    return shifted_bits


def shift_bits_right(x: int, n: int, print_statement=True):
    """Shift the bits of `x`, `n` to the right"""
    if n < 0:
        raise ValueError("negative shift count")
    shifted_bits = x // 2**n
    if print_statement:
        print(f"The number is now {shifted_bits}.")
    return shifted_bits


def cm_cubed_to_liters(cm_3: int, print_statement=True):
    """Converts centimeter cubed to liter"""
    liters = D(cm_3) / D(1000)
    if print_statement:
        print(f"In liters: {liters}")
    return liters


def liters_to_cm_cubed(liters: int, print_statement=True):
    """Converts liters centimeter cubed"""
    if print_statement:
        cm_3 = liters * 1000
        print(f"In centimeters cubed: {cm_3}")
    return liters


def multiples_limit(number: int, limit: int, print_statement=True, num_end=False):
    """Finds all the multiples of `number` below `limit`"""
    multi = []
    for i in range(1, limit + 1):
        if number * i >= limit:
            if number * i == limit:
                multi.append(number * i)
            break
        multi.append(number * i)
    if print_statement:
        p = rb(multi)
        print(f"The list of multiples of {number} with the limit of {limit} is {p}")
    return multi


def find_perimeter(length: int, b: int, print_statement=True):
    """Finds the perimeter of squares and rectangles"""
    perimeter = 2 * (length + b)
    if print_statement:
        if length == b:
            print(f"The perimeter of the square is {perimeter}")
        else:
            print(f"The perimeter of the rectangle is {perimeter}")
    return perimeter


def median(list_of_num: list, print_statement=True):
    """Finds the median of a list"""
    from statistics import median

    median_num = median(list_of_num)
    if print_statement:
        print(f"The median is {median_num}")
    return median_num


def mode(list_of_num: list, print_statement=True):
    """Find the mode of a list"""
    from statistics import mode

    mode_num = mode(list_of_num)
    if print_statement:
        print(f"The mode is {mode_num}")
    return mode_num


def num_of_combinations(n: int, r: int, print_statement=True):
    """
    Finds the number of combinations of r items from a set of n items.
    Args:
    n: The number of items in the set.
    r: The number of items to choose.
    print_statement: Whether or not to print the result.
    Returns:
    The number of combinations.
    """
    if r > n:
        return 0
    combinations = factorial(n, False) // (
        factorial(r, False) * factorial(n - r, False)
    )
    if print_statement:
        print(
            f"The number of combinations of {r} items from a set of {n} items is {combinations} combinations."
        )  # noqa: E501

    return combinations


def collatz_sequence(num: int, print_statement=True):
    """Returns the collatz sequence made from the parameter `num`"""
    sequence = [
        num,
    ]
    while num != 1:
        if num % 2 == 1:
            num = 3 * num + 1
            sequence.append(num)

        if num % 2 == 0:
            num //= 2
            sequence.append(num)
    if print_statement:
        seq = rb(sequence)
        print(seq)
    return sequence


def find_circumfrence(diameter: int, print_statement=True):
    """Find's the circumfrence of the circle"""
    ans = diameter * (884279719003555 / 281474976710656)
    if print_statement:
        print(f"The circumfrence of the circle is {ans}")
    return ans


def pyth_ther(a, b, print_statement=True, sr=False):
    if print_statement:
        print(f"Result: {a**2+b**2}")
        if sr:
            print(f"Result (Square rooted): {sqrt(a**2+b**2)}")
            return [a**2 + b**2, sqrt(a**2 + b**2)]
    if sr:
        return [a**2 + b**2, sqrt(a**2 + b**2)]
    return a**2 + b**2


def percentage_difference(original_number:int, new_number:int, steps=False, print_statement=True):
    if steps:
        l = len(f"{new_number} - {original_number}")
        l2 = len(f"{original_number}")
        first = f"""
({new_number} - {original_number})
--{"-" * l}--  x 100
{" " * ((l//2)-l2)}{original_number}
        """
        second = f"""
{new_number - original_number}
--{"-" * l}--  x 100
{" " * ((l//2)-l2)}{original_number}
        """
        third = f"{((new_number) - original_number) / original_number} x 100"
        forth = eval(third.replace("x", "*"))
        result = f"The steps are as follows:\n\n{first}\n\n{second}\n\n{third}\n\n{forth}%"
        if print_statement:
            print(result)
        return result
    res = (((new_number) - original_number) / original_number) * 100
    if print_statement:
        print(f"The answer is: {res}%")
    return res
