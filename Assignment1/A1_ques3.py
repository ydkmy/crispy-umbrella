#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
def generate_square_dict(n):
    square_dict = {}
    for i in range(1, n + 1):
        square_dict[i] = i * i
    return square_dict

# Given integral number n
n = 10

result_dict = generate_square_dict(n)

print(result_dict)
