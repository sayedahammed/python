dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name]: ", dict['Name'])
print("dict['Age]: ", dict['Age'])

# Update Existing Entry
dict['Age'] = 8

# Add new entry
dict['School'] = "DPS School"
print(dict)

# delete an entry
del dict['School']
print(dict)

# Get key
print(dict.get('Age', "NA"))

# Values
print(dict.values())

# Keys
print(dict.keys())

# Items
print(dict.items())

# Has Key
if "Age" in dict:
    print("Age Key Found")
else:
    print("Age key does not exists")
