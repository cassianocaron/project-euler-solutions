from time import process_time


STARTING_NUM = 999999


def main():
    start_time = process_time()

    testing_num = STARTING_NUM
    counter = []

    while testing_num > 1:
        n = testing_num
        count = 1

        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            count += 1

        testing_num -= 1
        counter.append(count)

    max_value = max(counter)
    number_index = counter.index(max_value)
    number = STARTING_NUM - number_index
    print(number)

    print(f"\nTook {round(process_time() - start_time, 2)} seconds to run")


if __name__ == '__main__':
    main()
