from string import ascii_uppercase

numbers = [16, 9, 3, 15, 3, 20, 6,
           '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

flag = ''
for number in numbers:
    flag += ascii_uppercase[number - 1] if type(number) is int else number

print(flag)
