def sum_of_digits(n):
    total = 0
    n_str = str(n)

    for digit in n_str:
        total += int(digit)

    return total
num = 123456789
result = sum_of_digits(num)
print("The sum of digits in", num, "is", result)