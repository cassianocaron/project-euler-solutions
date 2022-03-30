from time import process_time
import math


def main():
    start_time = process_time()

    num = 20
    prime_powers = []
    multiples = []

    for i in range(2, num+1):
        if not i in multiples:
            prime_powers.append(i ** int(math.log(num, i)))
            multiples.extend([i * m for m in range(2, int(num // i) + 1)])
    answer = math.prod(prime_powers)

    print(answer)

    print(f"\nTook {round(process_time() - start_time, 2)} seconds to run")


if __name__ == '__main__':
    main()
