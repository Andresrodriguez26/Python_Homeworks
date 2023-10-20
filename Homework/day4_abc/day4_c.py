# 2) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list


shopping_cart = {}

def add_item():
    new_item = input("What item would you like to add? ")
    quantity = int(input("How many? "))
    
    if new_item in shopping_cart:
        shopping_cart[new_item] += quantity
    else: 
        shopping_cart[new_item] = quantity
    
def delete_item():
    deleted = input("What item would you like to delete? ")
    if deleted in shopping_cart:
        dele_quant = int(input(f"How many {deleted}(s) would you like to delete? "))
        if dele_quant >= shopping_cart[deleted]:
            del shopping_cart[deleted]
            print(f"{deleted} removed from your shopping cart.")
        else:
            shopping_cart[deleted] -= dele_quant
    else:
        print("That is not in your cart. Please try again")

def view_store():
    print("Here is your current shopping cart:")
    for item, quantity in shopping_cart.items():
        print(f"{quantity} {item} (s)")
    
while True:
    response = input("What would you like to do? add, delete, view ")
    
    if response.lower() == "add":
        add_item()
    elif response.lower() == "delete":
        delete_item()
        
    elif response.lower() == "view":
        view_store()
        
    elif response.lower() == "quit":
        break
    else: 
        print("Please enter a valid response")
        
if shopping_cart:
    print("These are your final items:")
    for item, quantity in shopping_cart.items():
        print(f"{quantity} {item}(s)")
else:
    print("Your shopping cart is empty.")

print("Thank you for shopping with us!")