# Define 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello,{}, From My Function!, I wish you {}".format(username, greeting))

def sum_two_numbers(a, b):
    return a + b

my_function()
my_function_with_args("Elvis Presley", "left the building!")
x = sum_two_numbers(5, 15)
print(x)
