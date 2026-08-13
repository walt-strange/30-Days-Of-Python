fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# print(len(it_companies))
it_companies.add('Twitter')

it_companies.update(['Netflix', 'Snowflake'])
# print(it_companies)

it_companies.remove('Snowflake')
# print(it_companies)

# remove raises an error if its arugment is not in the set while discard does not raise an error.

C = A.union(B)
print(C)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))

del A
del B
del it_companies

print(len(set(age)))
print(len(age))

# string is a single item contained in quotations, list is a mutable collection of items, tuple is an inmutable collection of items, and a set is a collection of items without repeating values.

words_list = 'I am a teacher and I love to inspire and teach people'.split()
print(len(set(words_list)))