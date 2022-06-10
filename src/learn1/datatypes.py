value = (2 / 2 + 5) * 3 - 1
print(value)
value = 3 ** 4
print(value)
value = 17 % 3
print(value)

width = 20
height = 48
space = width * height
print(space)

price = 258
tip = 12/100
total = price + tip*price
print(total)

print('hello there....\nhello to you too....')
print("the time is 12 o'clock")
print("the kid \"said\" that it is 12 o'clock")
print('----------------------')
print('''first line
second line
third line
and another
long long line
whatever....
the end''')

print('----------------------')
print(2+5)
print('ran ' + 'amit')
print('ran ' * 10)
book = ('ran' 'amit' 'sahar')
print(book)
print('----------------------')

name = 'ran'
print(name[0])
print(name[2])
print(name[-1])
# print(name[20])
fullname = name + ' the clown'
print(fullname)  # ran the clown
name = 'amit'
print(name)  # amit
print(fullname)  # ran the clown
fullname = name + ' the clown'
print(fullname)  # amit the clown
print(fullname[5:8])
print(fullname[5:])
print(fullname[:4])

print('----------------------')
fullname = 'amit the clown'
name = 'ran'
fullname = name + fullname[4:]
print(fullname)  # ran the clown
isnot = 'is not a '
fullname = fullname[:4] + isnot + fullname[8:]  # ran is not a clown
print(fullname)

print('----------------------')
sizes = [43000000, 44, 36, 35]
print(sizes)
print(sizes[0])
more_sizes = [1, 2, 3]
all_sizes = sizes + more_sizes
print(all_sizes)
all_sizes[0] = 'ran hello'
print(all_sizes)
all_sizes.append('the end')
print(all_sizes)
lenght_of_list = len(all_sizes)
print(lenght_of_list)
