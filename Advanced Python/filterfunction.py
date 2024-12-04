def is_positive(number):
    return number > 0

numbers = [-2,-1,0,1,2,3,4,5]

# FILTER takes two arguments one is function and the second is list
postive_numbers = filter(is_positive,numbers)

def is_even(number):
    return number % 2 == 0 

numbers = [1,2,3,4,5,6]
even_numbers = list(filter(is_even,numbers))
print(even_numbers)

# for odd numbers
badshah = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x:x % 2 !=0, badshah))
print(odd_numbers)
