from time import process_time


def main():
    start_time = process_time()

    largest_pal = 0
    n1 = 999

    while n1 >= 100:
        n2 = 999

        while n2 >= n1:
            if (n1 * n2) <= largest_pal:
                break

            if is_palindrome(n1 * n2):
                largest_pal = (n1 * n2)
                largest_n1 = n1
                largest_n2 = n2
            n2 -= 1

        if (largest_pal / 999) >= n1:
            break
        n1 -= 1

    print(f"{largest_n1} * {largest_n2} = {largest_pal}")

    print(f"\nTook {round(process_time() - start_time, 2)} seconds to run")


def is_palindrome(n):
    reverse = int(str(n)[::-1])
    if n == reverse:
        return True


if __name__ == '__main__':
    main()
