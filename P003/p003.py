from time import process_time
from math import sqrt


N = 600851475143


def main():
    start_time = process_time()

    largest_factor = get_largest_prime_factor(N)
    print(int(largest_factor))

    print(f"\nTook {round(process_time() - start_time, 2)} seconds to run")


def get_largest_prime_factor(n):
    if n % 2 == 0:
        last_factor = 2
        n /= 2

        while n % 2 == 0:
            n /= 2
    else:
        last_factor = 1

    factor = 3

    max_factor = sqrt(n)

    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n /= factor
            last_factor = factor

            while n % factor == 0:
                n /= factor

            max_factor = sqrt(n)

        factor += 2

    return last_factor if n == 1 else n


if __name__ == '__main__':
    main()
