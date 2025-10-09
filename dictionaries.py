# DICTIONARIES{}/Json -- store informations that come as key-> value pair
# None --- represents absence of a value
# Methods
# .get() -- gets key->value that does not exist and returns None(inseatd of error), or could assign default value instead
# Note: .get() can be used instead of []

customer = {
    "name": " John Smith",
    "age": 30,
    "is_verified": True
}

# customer["name"] = "Matthew "
# print(customer["name"])
# print(customer.get("city"))
# print(customer.get("city", "Lafia"))

# for k, v in customer.items():
#     print(k + v)


# # 3rd
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