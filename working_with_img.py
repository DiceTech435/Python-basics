from pillow import Image

# Working with images
jay = Image.open("jay.jpg")
print(jay.size)
print(jay.format)
jay.show()


# Crop Image
area = (100, 100, 300, 375)
new = Image.crop(area)
new.show()


# Pasting image on another
jay = Image.open("jay.jpg")
kay = Image.open("kay.jpg")
jay.paste(kay)
jay.show()

# Breaking and seperating image channels
jay = Image.open("jay.jpg")
print(jay.mode) #RGB
r, g, b = jay.split()

r.show()
g.show()
b.show()


