import math
from time import process_time


LIMIT = 10001


def main():
    start_time = process_time()
    count = 1
    candidate = 1
    while True:
        if is_prime(candidate):
            count += 1
        if count == LIMIT:
            print(candidate)
            break
        candidate += 2
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
