# FOR LOOPS

# ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

# # for ninja in ninjas:
# #     print(ninja)

# # slice method
# # for ninja in ninjas[1:3]:
# #     print(ninja)

# #  add a statement when the cycle arrives at yoshi
# # for ninja in ninjas:
# #     if ninja == 'yoshi':
# #         print(f'{ninja} - black belt')
# #     else:
# #         print(ninja)


# WHILE LOOPS

age = 25
num = 0

# adds 1 to num on each loop, eventually reaching 26 and ending the loop
# while num < age:
#     print(num)
#     num += 1

#  print only even numbers
# while num < age:
#     if num % 2 == 0:
#         print(num)
#     num += 1

#  break the loop if num is greater than 10
# while num < age:
#     if num % 2 == 0:
#         print(num)
#     if num > 10:
#         break
#     num += 1

# don't output 0
while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1
