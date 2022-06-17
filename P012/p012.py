from time import process_time
from math import floor, sqrt


def main():
    start_time = process_time()

    prime_table = gen_prime_table()

    # Start with a prime
    n = 3
    # Number of divisors for any prime
    dn = 2
    cnt = 0
    while cnt < 500:
        n += 1
        n1 = n
        if n1 % 2 == 0:
            n1 = n1 / 2

        dn1 = 1
        for i in range(len(prime_table)):
            if prime_table[i] * prime_table[i] > n1:
                dn1 = 2 * dn1
                break

            exponent = 1
            while n1 % prime_table[i] == 0:
                exponent += 1
                n1 = n1 / prime_table[i]

            if exponent > 1:
                dn1 = dn1 * exponent

            if n1 == 1:
                break

        cnt = dn * dn1
        dn = dn1

    print(int(n * (n - 1) / 2))

    elapsed_time = process_time() - start_time
    print(f"Execution time: {round(elapsed_time, 2)} seconds")


def gen_prime_table():
    num = 1
    prime_array = []

    # The largest expected triangle number is within a 32-bit integer
    while num < 65500:
        if is_prime(num):
            prime_array.append(num)
        num += 1
    return prime_array


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
        r = floor(sqrt(n))
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
