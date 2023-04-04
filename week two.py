string1 = '''John_said, "let's learn python together".'''
print(string1)

i = 1
test = i == 1  # --> True
print(test)

x = 0.2 + 0.2
print(x)

print(x==0.4)

import math
f = 0.2 + 0.2 + 0.2
print(math.isclose(f, 0.6))

x = 1
print(type(x))

xstr = '1'
print(type(xstr))

test = x == xstr
print(test)
print(type(test))

print(3+2)

print('3'+'2')

a = '3' + '2'
print(type(a))

x = 1
print(x)

x = str('abc')
xup = str.upper(x)
print(xup)

"Hi".center(40)

"Hi".center(40, '@')

a = 'True'
b = 5
print(f"The value of a is {a} and the value of b is {b}")

x = str(5)
print(x)

# create a variable called "str", overwriting the built-in method
str1 = "very bad idea!"

srt2 = "very bad idea!"

x = str(5)
print(x)


Height = 30.5
Width = 33
Length = 56
volume = Height * Width * Length
print(f"the volume of the box is {volume} cubic centimeters.")


lst = {"a", "b", "c", "d", "e", "f"}
print(lst)


lst_a = [1, "string", True, None]
lst_b = ["a", lst_a]
print(lst_b)


lst = [1, "string", True, None, True]
print(f"Original lst is {lst}")

lst.remove(True)
print(f"lst after removing the first True is {lst}")

line = 'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]
print(domain)

# Create a tuple with two elements
tup = (1, 2)
# unpack the tuple into two variables:
(a, b) = tup
# print
print(f'`a` is {a} and `b` is {b}')

