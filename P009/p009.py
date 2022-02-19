""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a² + b² = c².

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. """


import time
import numpy as np

def main():
    start_time = time.process_time()
    pyth_trips = list(gen_all_pyth_trips(1000))    
    for i in range(len(pyth_trips)):
        if sum(pyth_trips[i]) == 1000:
            print(f"a = {pyth_trips[i][0]}, b = {pyth_trips[i][1]}, c = {pyth_trips[i][2]}")
            print(f"a*b*c = {pyth_trips[i][0] * pyth_trips[i][1] * pyth_trips[i][2]}")
            break    
    print(f"\nThe program took {round(time.process_time() - start_time, 5)} seconds to run")

    
def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)


def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

    
if __name__ == '__main__':
    main()