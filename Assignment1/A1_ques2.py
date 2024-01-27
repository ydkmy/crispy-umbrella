#Write a program that can compute the factorial of given numbers. The results should be printed in a comma-separated sequence on a single line.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numbers = [5, 7, 10, 3, 6]

factorials = [str(factorial(num)) for num in numbers]

print(",".join(factorials))
