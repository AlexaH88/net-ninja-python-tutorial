def belt_count(dictionary):
    # get the values from the belts dictionary ie the colours
    belts = list(dictionary.values())
    # get each individual item in the list
    # for belt in belts:
    # avoid repetition of duplicates on output by using set on belts to only allow one of each colour
    for belt in set(belts):
        # create variable num and count how many of each item are in the list
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'I am {key} and I am a {val} belt')


ninja_belts = {}


while True:
    ninja_name = input('Enter a ninja name: ')
    ninja_belt = input('Enter a belt colour: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('Add another? (y/n)')
    if another == 'y':
        continue
    else:
        break


# ninja_intro(ninja_belts)
belt_count(ninja_belts)
