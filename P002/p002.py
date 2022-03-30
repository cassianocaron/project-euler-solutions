from time import process_time


# Four million
MAX_TERM_VALUE = 4E6


def main():
    start_time = process_time()

    even_nums = get_even_fibonacci_nums()
    print(sum(even_nums))

    print(f"\nTook {round(process_time() - start_time, 2)} seconds to run")


def get_even_fibonacci_nums():
    even_nums = []
    curr_term = 1
    next_term = 2

    while curr_term < MAX_TERM_VALUE:
        if curr_term % 2 == 0:
            even_nums.append(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
    return even_nums


if __name__ == '__main__':
    main()
