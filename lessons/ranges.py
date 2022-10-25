#  for loop on a range, numbers 0, 1, 2, 3, 4
# for n in range(5):
#     print(n)

#  range from 3 to 9 (not including 10)
# for n in range(3, 10):
#     print(n)

#  range from 0 to 19, in increments of 4 
# for n in range(0, 20, 4):
#     print(n)


burgers = ['beef', 'chicken', 'veggie', 'supreme', 'double']

# #  cycles through the whole lenght of burgers. If you don't know and can't specify the length for example
# for n in range(len(burgers)):
#     #  print the index number n and the burger name
#     print(n, burgers[n])

# start going through the list from the end
for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])
