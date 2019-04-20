
# set.intersection(another_set) TODO

set()
ex_set = {3, 4, 2}
ex2_set = {3, 4, 2, 5}

# Aadding element - O(1)
ex_set.add(8) 

# Check in set - O(1)
print(2 in ex_set)

# Set interseption
print(ex2_set.intersection(ex_set))