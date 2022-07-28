# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, 
# and can access the items accordingly:

def my_function(*RNA)
  print("The most downstream feature of RNA is" + RNA[2])
  
# Call: my_function("5'UTR", "ORF", "3'UTR")
# Output: The most downstream feature of RNA is 3'UTR