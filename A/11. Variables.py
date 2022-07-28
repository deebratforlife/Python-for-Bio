# A note on casting variables
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3) #x will be '3'
y = int(3) #x will be 3
z = float(3) #z will be 3.0
# Get the data type:
# print(type(x))


# Python allows you to assign values to multiple variables in one line:
x, y, z = "3'UTR", "ORF", "5'UTR"
# print(y) to see.


# or you can give one value to multiple variables:
x = y = z = "RNA"


# Python allows you to assign values to multiple variables in one line:
RNA = ["5'utr", "orf", "3'utr"]
x = y = z = RNA
