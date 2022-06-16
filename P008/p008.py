"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""

from time import process_time


def main():
    start_time = process_time()

    with open("number.txt", "r") as f:
        number = "".join(row.strip() for row in f)

    biggest = 0
    for i in range(len(number)):
        seq = number[i:i+13]
        if len(seq) == 13:
            n = 1
            for j in range(len(seq)):
                n *= int(seq[j])
            if n > biggest:
                biggest = n
    print(biggest)

    elapsed_time = process_time() - start_time
    print(f"Execution time: {round(elapsed_time, 2)} seconds")


if __name__ == '__main__':
    main()
