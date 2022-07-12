def is_prime(num):
    # return boolean value T/F
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False



def primes(count):
    """Return count number of prime numbers, starting at 2.
    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]
    """
    # return a list of prime numbers
    # check if prime number helper function
    # if it is, then add it to result list, then return length of result list to match count
    results = []
    num = 2

    while count > 0:
        if is_prime(num):
            results.append(num)
            count-= 1

        num+= 1

    return results
