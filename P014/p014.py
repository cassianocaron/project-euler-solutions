from time import process_time

STARTING_NUM = 10**6


def main():
    start_time = process_time()

    chain_counter = {}

    for n in range(1, STARTING_NUM + 1):
        m, a = n, 1

        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            if n in chain_counter:
                a = a + chain_counter[n]
                break
            else:
                a = a + 1
        chain_counter[m] = a

    print(max(chain_counter.items(), key=lambda x: x[1]))

    elapsed_time = process_time() - start_time
    print(f"Execution time: {round(elapsed_time, 2)} seconds")


if __name__ == '__main__':
    main()
