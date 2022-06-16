from time import process_time
import math

LIMIT = 2000000


def main():
    start_time = process_time()
    candidate = 1
    # We know 2 is prime
    sum_primes = 2
    while candidate <= LIMIT:
        if is_prime(candidate):
            sum_primes += candidate
        candidate += 2
    print(sum_primes)
    elapsed_time = process_time() - start_time
    print(f"Execution time: {round(elapsed_time, 2)} seconds")


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True


if __name__ == '__main__':
    main()
