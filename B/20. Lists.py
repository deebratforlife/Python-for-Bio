# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

sequence_list = ["DNA", "RNA", "Protein"]
X = ("the central dogma is {}")

print(X.format(sequence_list))
# output: the central dogma is ['DNA', 'RNA', 'Protein']

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# To determine how many items a list has, use the len() function:
sequence_list = ["DNA", "RNA", "Protein"]
print(len(sequence_list))
#output: 3

# To check data type of list
print(type(sequence_list))
# output: <class 'list'>
# From Python's perspective, lists are defined as objects with the data type 'list':

# It is also possible to use the list() constructor when creating a new list.
sequence_list = list(("DNA", "RNA", "Protein"))
print(sequence_list)
# output: ['DNA', 'RNA', 'Protein']
# Note the double round brackets and the word list before the brackets.
# If you skip the word list, it will create a tuple instead of a list.

# REMEMBER
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# When choosing a collection type, it is useful to understand the properties of that type. 
# Choosing the right type for a particular data set could mean retention of meaning, and, 
# it could mean an increase in efficiency or security.











