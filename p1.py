""" Find the sum of all the multiples of 3 or 5 below 1000 """


def main():
    result = 0

    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            result = result + n

    print(result)


if __name__ == '__main__':
    main()