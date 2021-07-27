list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = ["a", "b", "c", "d"]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# Updating List
list1[3] = 2001
print(list1)

# Delete list elements
del list1[3]
print(list1)

# Length
print(len([1, 2, 3, 4]))

# Concatenation
print([1, 2, 3, 4] + [5, 6, 7, 8])

# Repetition
print(['Hi!'] * 4)

# Membership
print(3 in [1, 2, 3])

# Iteration
for x in [1, 2, 3]:
    print(x, end='')


