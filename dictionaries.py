# DICTIONARIES{}/Json -- a collection of {key:value} pairs. ordered and changeable. No diplicates
# None --- represents absence of a value

# METHODS
# print(dir(customer))
# print(help(customer))
# .get() -- gets key->value that does not exist and returns None(inseatd of error), or could assign default value instead
    # Note: .get() can be used instead of []
# .update({:})
# .pop("age") -- remove the specified one
# .popitem("age") -- remove the last inserted
# .clear() -- clear the dictionary
# .keys() -- returns all keys
# .values() -- returns all values
# .items() -- returns dictionary objects

customer = {
    "name": " John Smith",
    "age": 30,
    "is_verified": True,
    "city": "Abuja"
}

customer["name"] = "Matthew "
print(customer["name"])
print(customer.get("city")) #get the value of city
print(customer.get("city", "Lafia")) #passing default
customer.update({"age": 40})
print(customer)

for key, values in customer.items():
    print(f"{key}: {values}")


# 3rd
# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# } 
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
#     print(output)

# 4th
# message = input(">: ")
# words = message.split(" ")
# emojis = {
#     ":)": "😊",
#     ":(": "😠"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# DICTIONARIES CALCULATIONS
# zip(shares.values(), shares.keys())
# shares = {"NNPC": 464, "Shell": 300,
#           "BUA": 30, "Dangote": 54,
#           "GLO": 60, "AAPL": 65
#          }

# # This interchanges key-values' position
# min_shares = min(zip(shares.values(), shares.keys()))

# print(min_shares)