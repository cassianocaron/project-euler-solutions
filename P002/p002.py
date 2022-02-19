""" By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms """


MAX_TERM_VALUE = 4000000

def main():
    result = 0
    curr_term = 1
    next_term = 2

    while curr_term < MAX_TERM_VALUE:
        if curr_term % 2 == 0:
            result += curr_term
        # print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
    print(result)


if __name__ == '__main__':
    main()