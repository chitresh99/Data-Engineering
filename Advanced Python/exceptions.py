def kelvintofarhenit(temperature):
    # if this is true and if false stop here
    assert(temperature >= 0),"colder than absoulte zero"
    # return this
    return ((temperature-273)*1.8)+32

print(kelvintofarhenit(273))
print(kelvintofarhenit(0))
print(int(kelvintofarhenit(505.78)))
print(kelvintofarhenit(-5))