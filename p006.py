""" Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum """


LIMIT = 100

def main():
    sum_n = LIMIT * (LIMIT + 1) / 2
    sum_sq = (2 * LIMIT + 1) * (LIMIT + 1) * (LIMIT / 6)
    print(int(sum_n**2 - sum_sq))

    
if __name__ == '__main__':
    main()