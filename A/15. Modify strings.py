# Python has a set of built-in methods that you can use on strings.

X = "ATTCGCTGCTC"

# uppercase
print(X.upper())
# output: ATTCGCTGCTC

#lowercase
print(X.lower())
# output: attcgctgctc

# Remover whitespace. Whitespace is the space before 
# and/or after the actual text, and very often you want to remove this space.
Y = "  ATTCGCTGCTC  "
print (Y.strip())
#output: ATTCGCTGCTC (whitespace removed)

# The replace() method replaces a string with another string:
X = "ATTCGCTGCTC"
print(X.replace("T", "U"))
#output: AUUCGCUGCUC (The corresponding RNA sequence!)

# The split() method returns a list where 
# the text between the specified separator becomes the list items.
Z = "ATTTCG CGTCGTA"
print(Z.split(" "))
# output: ['ATTTCG', 'CGTCGTA']

