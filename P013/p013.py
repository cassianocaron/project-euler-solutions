from time import process_time


def main():
    start_time = process_time()

    with open("numbers.txt", "r") as numbers:
        num_array = [int(row.strip()) for row in numbers]

    print(str(sum(num_array))[:10])

    elapsed_time = process_time() - start_time
    print(f"Execution time: {round(elapsed_time, 2)} seconds")


if __name__ == '__main__':
    main()
