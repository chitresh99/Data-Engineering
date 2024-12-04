#lamba is like a function but it's anonymous 
# but the lambda function is much shorter and only one liner

# This is a function 
def add10_func(x):
    return x+10

# but this is way shorter
add10 = lambda x: x+10
print(add10(5))

# we can pass multiple arguments
multiple = lambda x, y : x * y
print(multiple(5,6))

# so a here is it by default sorted by x co-ordinate in a tuple but we can change it
# by passing 1 in x
points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D,key= lambda x:x[1])
print(points2D_sorted)