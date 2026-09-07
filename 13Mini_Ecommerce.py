products = [

{

"name": "Laptop",

"price": 70000,

"brand": "Dell"

},

{

"name": "Phone",

"price": 40000,

"brand": "Samsung"

},

{

"name": "Tablet",

"price": 30000,

"brand": "Apple"

}

]

# Print all products
print("All products:", products)

# Print first product

print("First product:", products[0])

# To print second product's price

print("Second product's price", products[1]["price"])


# Print third product's brand

print("Third product brand:", products[2]["brand"])



# Change first product's price

products[0]["price"] = 80000
print("After price changed", products[0]["price"])

#To add rating to second product

products[1]["rating"] = 4.0
print("Seconf product details after adding rating:", products[1])


# To add a product manually

products.append({
    "name": "Headphones",
    "price": 5000,
    "brand": "Sony"
})

# Print the final dataset

print("Final dataset:", products)

#The above was a combination of dictionary induced in a list 

# The combination
# List → stores multiple products
# Dictionary → stores information about each product
# Indexing → selects a product, e.g. products[0]
# Keys → identify information, e.g. "price"
# Values → actual data, e.g. 70000