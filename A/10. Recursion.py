# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into 
# writing a function which never terminates, or one that uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# Here we define a function codon_recursion that calls itself.

def codon_recursion(k):
  if k > 0:
    result = k + codon_recursion(k - 1)
    print (result)
  else:
    result = 0
  return result
  
print ("\n\nRecursion of the codons")

# Call: codon_recursion(6)
# Output: 21 15 10 6 3 1
