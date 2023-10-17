#Exercise 1:
#Accept two user ages as inputs and give us the difference between them. 
#(The Answer should always be a positive output)

first_age = int(input("What is your age? "))
second_age = int(input("What is your age? "))
difference = (abs(first_age - second_age))

print(f"The age difference between you both is {difference} years. ")

#("\n")
#Exercise 2: 
#Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.

noun = input("Type a noun ")
verb = input("Type a verb ")
adjective = input("Type an adjective ")

result = "This is your noun, verb and adjective {noun}, {verb}, and {adjective}. ".format(noun,verb,adjective)
print(result)


#Exercise 3:
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors.

age = input("Please enter your age ")
if age < 18:
    print("You are a Kid ")
elif 18 <= age <= 65:
    print("You are an Adult")
else:
    print("You are a Senior")


#Exercise 4:
#Take in a number from a user input, output the number squared.

numberx = input("Please type a number")
total = numberx ** 2 

print(f"This is your number {total} squared, you are welcome! ")


#Exercise 5:
#Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False

word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

print(f"Word  {word1} {len(word1) > 5}")
print(f"Word  {word2} {len(word2) > 5}")
print(f"Word  {word3} {len(word3) > 5}")
print(f"Word  {word4} {len(word4) > 5}")
print(f"Word  {word5} {len(word5) > 5}")

