print("hello ran")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("----------------------------------")

#print(2 + 19)
print(10 % 4)


print("----------------------------------")

ran_age = 11
amit_age = 8
difference = ran_age - amit_age
print(difference)


ran_name = 'ran'
amit_name = "amit"
print(ran_name, amit_name)

kid_names = 'sahar ran amit'
print(kid_names)

print("----------------------------------")

kid_names = 'sahar\nran\namit'
print(kid_names)

print("----------------------------------")

kid_names = """sahar
ran
amit"""
print(kid_names)

print("----------------------------------")

print(kid_names[0:5])
print(kid_names[6:9])
print(kid_names[-4:])
print(kid_names[::-1])

print("----------------------------------")

kid_names = ['sahar', 'ran' , 'amit']
boys = kid_names[1:]
print(boys)

print("----------------------------------")

girls = ['sahar']
boys = ['ran' , 'amit']
all_kids = girls + boys
print(all_kids)

print("----------------------------------")
all_kids.append('omri')
print(all_kids)
