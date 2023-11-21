# LISTS
numbers = list(range(20))
print(numbers)

print(list("hellow world"))
print(len(list("hellow world")))
# you can also assign the list function to a variable and then print

# ACCESSING ITEMS IN LIST
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-1])  # accessing items in a list

letters[2] = "C"  # modifying items in list
print(letters)

print([letters[0:3]])  # slicing a list
print(letters[::2])  # skipping every second element

numbers = list(range(20))
print(numbers)
print(numbers[::2])
print(numbers[::3])
print(numbers[::-1])
print(numbers[::-2])

# LIST UNPACKING
collection = [1, 2, 3, 4, 5, 6, 7, 8, 9]
one, *others, last = collection   # *This step unpacks the collection list
# This step also packs the numbers from 2 to 8 into *others.
print(one)
print(last)
print(others)

# LOOP OVER LISTS
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for letter in letters:
    print(letter)
# LOOP OVER LISTS ALONG WITH GETTING THEIR INDEX
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for letter in enumerate(letters):
    print(letter)  # at each interation of the result, we get a tuple

for index, letter in enumerate(letters):
    # used for unpacking the resulting tuples
    print(index, letter)
