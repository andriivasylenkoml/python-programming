# practice_work_1
import math


"""Variant 4"""


def calculate_p(x: float) -> float:
    numerator = math.exp(-3 * x) + math.tan(3 * x - 3)
    denominator = abs(math.sin(x))**4 + \
        math.sqrt(math.cos(x) + math.cos(2 * x))
    return numerator/denominator


# Example usage:
x_value = 1.0  #You cna change this.
p = calculate_p(x_value)
print(f"p({x_value}) = {p}")


"""Variant 19"""


def calculate_u(x: float) -> float:
    if x > 0 and x != 1 and math.log(x) > 0 and math.sqrt(math.log(x)) != 1:
        # First term: ln|1 - x|.
        term1 = math.log(abs(1 - x))

        # Second term: (tan(x) - sin^2(x)) / (1 - sqrt(ln(x)))
        term2 = (math.tan(x) - math.sin(x)**2) / (1 - math.sqrt(math.log(x)))

        return term1 + term2
    return 0.0

# Example usage:
x_value = 2.0 # Change tis to test other values.
u = calculate_u(x_value)
print(f"u({x_value}) = {u}")