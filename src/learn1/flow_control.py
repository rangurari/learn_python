
# user_input = input('Please enter an integer: ')
user_input = '17'
x = int(user_input)

if x < 0:
    print('Negative number detected')
elif x == 0: # else if
    print('Zero')
elif x == 1:
    print('One')
else:
    print('a lot....')

if x < 0 and (x > -8 or x == -8):
    print('whatever....')

# x < 0 and (x > -8 or x == -8)
# x -> -7
# x < 0 -> true
# true and (x > -8 or x == -8)
# true and (true or x == -8)
# true and (true or false)
# true and true
# true

# true -> true
# false -> false
# true and true -> true
# true and false -> false
# true or false -> true
# false and false -> false
# false or false -> false
# true and (false and true) and (true or false) and true -> true and false and true and true -> false

print('--------------------------------------')
words = ['cat', 'window', 'run']
for word in words:
    print('And the next word is......')
    print(word)

def print_even_number(num):
    print('found even number: '+str(num))

# print_even_number(18)

numbers = [5, 17, 8, 19, 20, 21, 11, 120]
for num in numbers:
    if num % 2 == 0:
        print_even_number(num)
