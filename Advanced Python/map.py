# Basically we can use map and apply any function to every 
# item in a list or tuple bascially anything that is iterable
# like here we had a function of converting string to int
# and map applied that function to every object in a list

s = ['1','2','3','4']
res = map(int,s)
print(list(res))

# one thing i noticed here is that we have to pass the list explicilty
a = [1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))

d = (1,2)
e = map(lambda x: x*2,d)
print(tuple(e))
