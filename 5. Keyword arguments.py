# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(RNA3, RNA2, RNA1):
  print("The most downstream feature in RNA is" + RNA3)
  
# Call: my_function(RNA3 = "3'UTR", RNA2 = "5'UTR", RNA1 = "ORF")
# Output: The most downstream feature in RNA is 3'UTR

# Keyword arguments are also called kwargs in py.