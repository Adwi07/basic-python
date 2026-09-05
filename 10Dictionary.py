#A dictionary is a mutable data type in python and consist of a key-value pair enclosed within {key: value}

laptop = {

"brand": "Dell",

"model": "XPS 15",

"price": 120000,

"ram": "16GB",

"storage": "512GB SSD",

"available": True

}

# Display the product
print("Dictionary is: ",laptop)

#TO print the brand
print("Brand is:", laptop["brand"])

#To print the model
print("Model is:", laptop["model"])

#To print the price
print("Price is:", laptop["price"])


#To change the price
laptop["price"] = 150000

print(laptop["price"]) # To print the new price

#To add processor information
laptop["Processor"] = "Ryzen 7 7th generation"
print(laptop)

#To add gpu information
laptop["Gpu"] = "Nvidia Rtx 3050 ti"
print(laptop)

#To change RAM to 32gb
laptop["ram"] = "32 gb"
print(laptop)

# #To remove the key "available"
laptop.pop("available")
print(laptop)

#To print all keys
print("All keys in our dictionary:\n",laptop.keys())

#To print all values
print("All values in our dictionary:\n", laptop.values())



#To print all items
print("All items in our dictionary:\n",laptop.items())

#product dictionary for a mobile phone

mobile = {
    "Model": "Samsung s24",

    "Brand": "Samsung",

    "Ram": "16gb",

    "Price": 65000,

    "Battery life": "16 Hours"

}

print("Mobile specs: ", mobile)