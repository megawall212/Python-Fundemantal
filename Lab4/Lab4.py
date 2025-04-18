def fibonacci(n):
    if n == 0:
        return 1  # Custom return for position 0
    if n < 1:
        raise ValueError

    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b

    return a #in case you want to test it

def is_prime(n):
    if n <= 1:
        return False # not a prime if less than or equal to 1 (special case)
    for i in range(2, n): # check the factorials
        if n % i == 0:
            return False
    return True

# Test cases in case you need

#print(is_prime(11))    # True
#print(is_prime(9))     # False
#print(is_prime(-2))    # False


def print_prime_factors(n):
    if n <= 1:
        raise ValueError

    factors = [] #empty list
    out=n
    # Check for 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # n must be odd numbers/factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i) #append means keep adding that factor to the list
            n //= i

    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    # Format the output
    # The expression map(str, factors) is used to convert each element
    # in the factors list from its original type (typically integers) to strings
    factors_string = " * ".join(map(str, factors))
    print(f"{out} = {factors_string}")

