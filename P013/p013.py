"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

from time import process_time


def main():
    start_time = process_time()

    with open("numbers.txt", "r") as numbers:
        num_array = []
        for number in numbers:
            num_array.append(int(number.strip("\n")))

    print(str(sum(num_array))[:10])

    print(f"\nTook {round(process_time() - start_time, 2)} seconds to run")


if __name__ == '__main__':
    main()
