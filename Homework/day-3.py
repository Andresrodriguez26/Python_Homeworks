# 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

shopping_cart = {}

while True:
    response = input("What would you like to do? add/delete/view/quit")

    if response.strip().lower() == "add":
        new_item = input("What item would you like to add? ")
        quantity = input("How many? ")
        shopping_cart[new_item] = quantity
    elif response.strip().lower() == "delete":
        deleted = input("What item would you like to delete? ")
        if deleted in shopping_cart:
            del shopping_cart[deleted]
            print(f"{deleted} removed from your shopping cart.")
        else:
            print("That is not in your cart. Please try again")
    elif response == "view":
            print(f"Here is your current shopping cart: {shopping_cart}. ")
    elif response == "quit":
        break
    else:
        print("please enter a valid response")
    
print("These are your final items:")
for item, quantity in shopping_cart.items():
        print(f"{quantity} {item}(s)")

print("Thank you for shopping with us!")


# 2) Set Practice
# Remove all duplicates from the following list

nums_list = [1, 1, 1, 2, 2, 3, 5, 6, 4, 12, 11, 12, 12, 14, 16, 16, 16, 1, 1, 1, 2, 2]
print(set(nums_list))


# Out put the intersection of the following the following sets.

set1 = {20, 24, 26, 27}
set2 = {26, 35, 63, 27}

set3 = set1.intersection(set2)
print(set3)

# Output the difference between the following sets

set3 = {100, 65, 89, 200}
set4 = {65, 103, 54, 200}

set5 = set3.difference(set4)
print(set5)