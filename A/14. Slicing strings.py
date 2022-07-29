# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, 
# to return a part of the string.

X = "ATTCGCTG"

# slice from position 3 to position 5 (not included)
print(X[2:5])
# output: TCG


# slice from start to position 5 (not included)
print(X[:5])
#output: ATTCG

# slice from position 5 to the end
print(X[5:])
#output: CTG

# Use negative indexes to start the slice from the end of the string
print(X[-5:-2])
#output: CGC



