# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def my_function(RNA  Type = "mRNA")
  print("This RNA type is " + RNA Type)
  
# Call: my_function("tRNA")
# output: This RNA type is tRNA

# Call: my_function()
# output: This RNA type is mRNA 