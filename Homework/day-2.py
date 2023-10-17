#Exercise 1:
#Using the given list, print out a filtered version of the list with only the numbers 
#that are less than ten.

alist = [1,11,14,5,8,9]

filtered = [x for x in alist if x < 10]

#print("\n")
#for number in alist:
#    if number < 10:
#        print(number)

#Exercise 2:
#Merge and sort the two lists below
#Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

l_3 = l_1 + l_2
print(l_3)

final_list = sorted(set((l_3)))
print(final_list)

# Exercise 3:
# Square every number from 1 to 15

square_numbers = [x**2 for x in range(1,16)]
print(square_numbers)

# Exercise 4:
# Using List Comprehension and the given list, print out a filtered list with only the names that start 
# with the letter 'a'. The names in the outputted list should be title cased and have no whitespace.

names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
#expected output = ['Amy', 'Alex']
# new_list = []
# for name in names_list:
#     if len(name.strip()) > 0 and name.strip().lower()[0] == "a":
#         new_list.append(name.strip().title())
#     print(new_list)

list_comp = [name.strip().title() for name in names_list if len(name.strip()) > 0 and name.strip().lower()[0] == "a"]
print(list_comp)

# Exercise 5:
# Print all Prime numbers from 1 to 100

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for number in range(1, 101):
    if prime(number):
        print(number)
