'''operator precedence means order of operation
1 - Parenthesis (){}[]
2 - exponentiation 2 ** 3
3 - multiplication or division
4 - addition/subtraction'''
x = 10 + 3 * 2
print(x) #16
y = 10 + 3 * 2 ** 2
print(y) #22
z = (10 + 3) * 2 ** 2
print(z) #52

