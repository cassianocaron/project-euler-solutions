""" Find the largest prime factor of the number 600851475143 """


N = 600851475143

def main():
    largest = prime_factors(N)
    print(largest)


def prime_factors(n):
    d = 2
    while n > 1:
        if n % d == 0:
            n /= d            
        else:
            d += 1
    return d


if __name__ == '__main__':
    main()