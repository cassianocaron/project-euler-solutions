from time import process_time

LIMIT = 100


def main():
    start_time = process_time()

    sum_n = LIMIT * (LIMIT + 1) / 2
    sum_sq = (2 * LIMIT + 1) * (LIMIT + 1) * (LIMIT / 6)
    print(int(sum_n**2 - sum_sq))

    elapsed_time = process_time() - start_time
    print(f"Execution time: {round(elapsed_time, 2)} seconds")


if __name__ == '__main__':
    main()
