#!/usr/bin/env python3
# def test_print_fibonacci_zero(self):
#         '''prints empty list when length = 0'''

# def test_print_fibonacci_one(self):
#         '''prints 0 when length = 1'''

# def test_print_fibonacci_two(self):
#         '''prints 0\\n1 when length = 2'''

# def test_print_fibonacci_ten(self):
#         '''prints 0\\n1\\n1\\n2\\n3\\n5\\n8\\n13\\n21\\n34 when length = 10'''


def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fibonacci = [0, 1]
        for i in range(2, length):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        print(fibonacci)
