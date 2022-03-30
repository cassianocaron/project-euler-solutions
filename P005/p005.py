from time import process_time


def main():
    start_time = process_time()

    n = 1

    while True:
        smallest = evenly_divisible(n)

        if smallest == n:
            print(smallest)
            break
        n += 1

    print(f"\nTook {round(process_time() - start_time, 2)} seconds to run")


def evenly_divisible(smallest):
    for n in range(1, 21):
        if smallest % n != 0:
            return
    return smallest


if __name__ == '__main__':
    main()
