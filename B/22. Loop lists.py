# You can loop through the list items by using a for loop:                                                                        FOR LOOP
sequence_list = ["DNA", "RNA", "Protein"]
for x in sequence_list:
  print(x)
# output: DNA RNA Protein
# NOTE: for loop has no indentation, but print needs some (standard preferred is 4).

# You can also loop through the list items by referring to their index number.                                                    FOR LOOP WITH INDEX AND LEN
# Use the range() and len() functions to create a suitable iterable.
sequence_list = ["DNA", "RNA", "Protein"]
for i in range(len(sequence_list)):
 print(sequence_list[i])
# output: DNA RNA Protein

# You can also select a subset of list:
sequence_list = ["DNA", "RNA", "Protein"]
for i in range(len(sequence_list)-1):
 print(sequence_list[i])
# output: DNA RNA

# You can loop through the list items by using a while loop.                                                                         WHILE LOOP
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
# Remember to increase the index by 1 after each iteration.
sequence_list = ["DNA", "RNA", "Protein"]
i = 0
while i < len(sequence_list):
 print(sequence_list[i])
 i = i+1
# output: DNA RNA Protein
# NOTE: Keep an eye on the indentation of i = i + 1.
# If no indentation is provided, that means the first while loop will iterate forever and print several DNA before crashing.
# Indentation means i is increased after every loop.

# List Comprehension offers the shortest syntax for looping through lists:                                                           LIST COMPREHENSION
sequence_list = ["DNA", "RNA", "Protein"]
[print x for x in sequence_list]
# Kinda similar to the for loop.
