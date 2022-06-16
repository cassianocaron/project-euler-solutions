from time import process_time

LENGTH_SEQ = 4


def main():
    start_time = process_time()

    with open("grid.txt", "r") as f:
        grid = [row.strip().replace(" ", ",").split(",") for row in f]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = int(grid[i][j])

    great_hor = greatest_product_horizontally(grid)
    great_ver = greatest_product_vertically(grid)
    great_diag_right = greatest_product_diag_right(grid)
    great_diag_left = greatest_product_diag_left(grid)

    print(max(great_hor, great_ver, great_diag_right, great_diag_left))
    elapsed_time = process_time() - start_time
    print(f"Execution time: {round(elapsed_time, 2)} seconds")


def greatest_product_horizontally(grid):
    greatest_hor = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            seq = grid[i][j:j+LENGTH_SEQ]
            if len(seq) == LENGTH_SEQ:
                product_hor = 1
                for k in range(LENGTH_SEQ):
                    product_hor *= seq[k]
                if product_hor > greatest_hor:
                    greatest_hor = product_hor
    return greatest_hor


def greatest_product_vertically(grid):
    x = 0
    y = LENGTH_SEQ
    greatest_vert = 0
    for _ in range(len(grid) - 3):
        for i in range(len(grid)):
            product_vert = 1
            for j in range(x, y):
                product_vert *= grid[j][i]
            if product_vert > greatest_vert:
                greatest_vert = product_vert
        x += 1
        y += 1
    return greatest_vert


def greatest_product_diag_right(grid):
    x = 0
    y = LENGTH_SEQ
    greatest_diag_right = 0
    for _ in range(len(grid) - 3):
        n1 = 0
        n2 = 0
        for __ in range(len(grid) - 3):
            n1 = n2
            product_diag_right = 1
            for i in range(x, y):
                product_diag_right *= grid[i][n1]
                n1 += 1
            if product_diag_right > greatest_diag_right:
                greatest_diag_right = product_diag_right
            n2 += 1
        x += 1
        y += 1
    return greatest_diag_right


def greatest_product_diag_left(grid):
    x = 0
    y = LENGTH_SEQ
    greatest_diag_left = 0
    for _ in range(len(grid) - 3):
        n1 = (len(grid) - 1)
        n2 = (len(grid) - 1)
        for __ in range(len(grid) - 3):
            n1 = n2
            product_diag_left = 1
            for i in range(x, y):
                product_diag_left *= grid[i][n1]
                n1 -= 1
            if product_diag_left > greatest_diag_left:
                greatest_diag_left = product_diag_left
                n1 = n2
                gtp = []
                for i in range(x, y):
                    gtp.append(grid[i][n1])
                    n1 -= 1
            n2 -= 1
        x += 1
        y += 1
    print(*gtp, sep=", ")
    return greatest_diag_left


if __name__ == '__main__':
    main()
