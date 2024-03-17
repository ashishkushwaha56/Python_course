# slicing = create a substring by extracting elements from another string 
# indexing[] or slice()
# [start:stop:step]

name = "Ashish Kushwaha"

first_name = name[:6]
last_name = name[7:]

print("First name: "+first_name)
print("Last name: "+last_name)

reversed_name = name[::-1]

print(reversed_name)


# using slice() function

website = "https://google.com"

slice1 = slice(8,-4)

print(website[slice1])
