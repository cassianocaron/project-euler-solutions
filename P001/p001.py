from time import process_time


def main():
    start_time = process_time()

    result = 0
    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            result += n

    print(result)
    
    print(f"\nTook {round(process_time() - start_time, 2)} seconds to run")


if __name__ == '__main__':
    main()
