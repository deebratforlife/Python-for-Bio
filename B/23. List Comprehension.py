# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Let us make a new list by finding items that contain letter r in the original list.                             FOR LOOP WITH IF CONDITIONN
sequence_list = ["DNA", "RNA", "Protein"]
# create an empty list.
new_list = []
# a for loop with conditional statement is used.
for x in sequence_list:
 if "r" in x:
  new_list.append(x)

print(new_list)
# output: ["Protein"]

# With list comprehension you can do all that with only one line of code:                                           LIST COMPREHENSION
sequence_list = ["DNA", "RNA", "Protein"]

newlist = [x for x in sequence_list if "r" in x]
print (newlist)


# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

sequence_list = ["DNA", "RNA", "Protein", "ORF", "UTR"]
sequence_list.sort()

print(sequence_list)
# output: ['DNA', 'ORF', 'Protein', 'RNA', 'UTR']

# To sort descending, use the keyword argument reverse = True:
sequence_list = ["DNA", "RNA", "Protein", "ORF", "UTR"]
sequence_list.sort(reverse = True)

print(sequence_list)
# output: ['UTR', 'RNA', 'Protein', 'ORF', 'DNA']

# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

# Sort the list based on how close the number is to 50:
def my_func(n):
 return abs(n - 50)
 
sequence_list = [10, 40, 50, 86, 24, 65, 65]

sequence_list.sort(key = my_func)
print(sequence_list)
# output: [50, 40, 65, 65, 24, 86, 10]

# You cannot copy a list simply by typing list2 = list1, because: 
# list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().
thislist = ["DNA", "RNA", "Protein"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
thislist = ["DNA", "RNA", "Protein"]
mylist = list(thislist)
print(mylist)

# A way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

for x in list2:
 list1.append(x)
 
print(list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)













