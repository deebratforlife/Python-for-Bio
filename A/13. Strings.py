# Strings in python

# Like many other popular programming languages, strings in Python are ARRAYS of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = "TTCGTCA"
print(a[2])
#output = C

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "TTCGTCA"
print(x)
# output = T T C G T C A

# To get the length of a string, use the len() function.
a = "TTCGTCA"
print(len(a))
# output = 7

# To check if a certain phrase or character is present in a string, we can use the keyword in.
a = "TTCGTCA"
print("TC" in a)
# output = TRUE

# Use it in an if statement:
a = "TTCGTCA"

if "TC" in a:
    print("yes, this dimer is present in the sequence.")
# output = yes, this dimer is present in the sequence.

# Same as above, to check if a certain phrase or character is NOT present in a string, we can use the keyword not in.