""" Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 """


def main():
    n = 1
    while True:
        smallest = evenly_divisible(n)
        if smallest == n:
            print(smallest)
            break
        n += 1


def evenly_divisible(smallest):
    for n in range(1, 21):
        if smallest % n != 0:
            return
    return smallest


if __name__ == '__main__':
    main()