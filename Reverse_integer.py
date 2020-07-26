def reverse_integer(n):

    reversed = 0
    remainder = 0
    while n  > 0:
        remainder = n % 10
        n = n // 10
        reversed = reversed * 10 + remainder

    return reversed

n = 1234
print(reverse_integer(n))
