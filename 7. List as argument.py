# You can send any data types of argument to a function (string, number, list, dictionary etc.), 
# and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_fucntion(RNA Features):
  for x in RNA Features:
    print(x)
    
# Defining a list:    
RNA = ["5'UTR", "ORF", "3'UTR"]

# Call: my_function(RNA)
# Output: 5'UTR ORF 3'UTR