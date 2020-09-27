# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.

# Long version

def sum_multiples(number):
    list_multiples = []
    sum_count = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list_multiples.append(i)
    for i in list_multiples:
        sum_count = sum(list_multiples)
        return sum_count

print(sum_multiples(1000))          

# List comprehension one-liner:

print("This is a one-liner solution using a list comprehension: ") 
print(sum([x for x in range(1000) if ((x % 5 == 0) or (x % 3 == 0))]))

