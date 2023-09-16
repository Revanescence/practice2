from functools import reduce


def generate_ap(a1, d, n):
    ap = [a1 + i * d for i in range(n)]
    return ap


T = int(input())

if 1 <= T <= 25:
    for _ in range(T):

        input_str = input()
        a1, d, n = map(int, input_str.split())

        if 1 <= a1 <= 100 and 1 <= d <= 100 and 1 <= n <= 100:
           
            ap = generate_ap(a1, d, n)

            print(*ap)
            squares = list(map(lambda x: x**2, ap))
            squares_as_strings = list(map(lambda x: str(x**2), ap))

            # Print the squares of terms as a space-separated string
            print( " ".join(squares_as_strings))

           
            sum_of_squares = reduce(lambda x, y: x + y, squares)

            print(sum_of_squares)
        else:
            print("Constraints:  1 <= a1 <= 100 and 1 <= d <= 100 and 1 <= n <= 100")
else:
    print("The number of test cases must be between 1 and 25.")
