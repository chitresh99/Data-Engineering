# python list can hold elements , and elements here can be number
# string character etc

fruits = ["apple","bannana","cherry"]

print(fruits)

# multiline list -> for readabiltiy
numbers = [
    1,
    2,
    3,
    4,
    5
]

print(numbers)

#label on the jar is what we call index

rappers = ["kanye west","raftaar","krsna"]
rapper_first = rappers[0]
print(rapper_first)
#appending
rappers.append("divine")
print(rappers)

#inserting can be done at a specific index
rappers.insert(1,"eminem")
rappers.remove("raftaar")
print(rappers)