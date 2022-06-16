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
