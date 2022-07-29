# We cannot combine strings and numbers by a + operand
# But, we can combine them using the format() method.

# The format() method takes the passed arguments, 
# formats them, and places them in the string where the placeholders {} are:

X = "The sequence motif preference is {} and {}"

Y = "GUUU"
Z = "GUAC"

print(X,format(Y,Z))
#output: The sequence motif preference is GUUU and GUAC
# The format() method takes unlimited number of arguments, 
# and are placed into the respective placeholders.

# You can use index numbers {0} to be sure the arguments 
# are placed in the correct placeholders:

X = "The RNA is {1} with sequence enrichment of {2} and {0}"

A = "GUUU"
B = "long"
C = "GUAC"

print(X.format(C,B,A))
#output: The RNA is long with sequence enrichment of GUUU and GUAC