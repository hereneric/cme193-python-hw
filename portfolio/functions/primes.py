def is_prime(n):
    """
    return true if n is prime number
    """
    if n == 2 or n == 3:
        return True
    elif (n - 1) % 6 != 0 and (n + 1) % 6 != 0:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def return_primes(n):
    """
    return a list of primes up to n
    """
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result

def return_n_primes(n):
    """
    return n primes from 2
    """
    result = []
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            result.append(num)
            count += 1
        num += 1
    return result

print is_prime(17)
print return_primes(100)
print return_n_primes(20)
