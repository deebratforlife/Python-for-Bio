# boolean with an if else

a = "TTCGCGATAAT"
b = "TTTTACTGCTACTGAATCG"

c = len(a)
d = len(b)

if c > d:
 print("sequence 'b' is longer than 'a'.")
 
else:
 print("It seems 'a' might be the longer sequence.")


# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones. 

# The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool("GUU"))
# output: TRUE

print(bool())
# output: FALSE

# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One can however create a function that returns FALSE. The function output can then be used for actions.

def my_function():
    return False
    
if my_function():
    print("Yes!")
    
else:
    print("No")
    
# output: No


# Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:

x = 100
print (isinstance(x,int))
#output: True

