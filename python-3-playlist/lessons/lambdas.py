# lambda --> small anonymous function that is ever only used once

nums = [1, 2, 3, 4, 5, 6]


# standard way to do it
def square(n):
    return n*n


print(list(map(square, nums)))


# or using a lambda
# this is a lambda function on its own
lambda n: n*n

# and this is how you can include it directly in the map function
print(list(map(lambda n: n*n, nums)))
