cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

print("Items in cart is: ",cart) #to display all products
print(cart[0]) # to display first product
print(cart[-1]) # to display last product

cart.append("Webcam") # to add a new item in cart

print(cart) # to print the whole cart with new item

cart.insert(2, "USB Hub") # to insert an item at index 2
print(cart) # printing updated cart

cart.remove("Mouse") #to remove "Mouse"
print(cart) # printing updated cart

cart.pop() # to remove the last item
print(cart) # printing updated cart

print(cart.count("Laptop")) # to count occurences of "Laptop"

another_cart = cart.copy() # to make copy of the cart
print("Copy of the cart is: ",another_cart)

cart.reverse() # to reverse the cart
print(cart)

# or 

# reverse_cart = cart[::-1]
# print(reverse_cart) same for reversing the cart

cart.sort() 
print(cart)
# to print the cart alphabetically also known as sorting


#understanding extend() fn


new_items = ["Webcam", "USB Hub", "Charger"]

cart.extend(new_items)

print(cart)

#diffrence bw append and extend
cart.append(["Webcam", "USB Hub"])
print(cart)
# [..., ['Webcam', 'USB Hub']]

cart.extend(["Webcam", "USB Hub"])
print(cart)
#[..., 'Webcam', 'USB Hub']


#clear -> removes everything
cart.clear()

print(cart)