""" Find the largest palindrome made from the product of two 3-digit numbers """


def main():
    largest_pal = 0
    p1 = 999
    while p1 >= 100:
        p2 = 999
        while p2 >= p1:
            if (p1 * p2) <= largest_pal:
                break
            if is_palindrome(p1 * p2):
                largest_pal = (p1 * p2)
                largest_p1 = p1
                largest_p2 = p2                
            p2 -= 1
        if (largest_pal / 999) >= p1:
            break
        p1 -= 1
    print(f"{largest_p1} * {largest_p2} = {largest_pal}")


def is_palindrome(n):
    reverse = int(str(n)[::-1])
    if n == reverse:
        return True


if __name__ == '__main__':
    main()