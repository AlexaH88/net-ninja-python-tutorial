from random import randint

ninja_words = [
    'Aiki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haiboku',
    'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]


# create ninjarize function and pass through a word each time
def ninjarize(word):
    # create a random integer and apply it to the list of words in relation to their indexing number
    # -1 at the end because the number of items in the list is one more than the indexing needed
    # get a random integer between the values of 0 and total length of list -1
    random_pos = randint(0, len(ninja_words)-1)
    # return a string with the original word, and the randomly selected new ninja word
    return f'{word} {ninja_words[random_pos]}'


# have the user define how many paragraphs there should be
paragraphs = int(input('How many paragraphs of ninja ipsum:'))


with open('ipsum.txt') as ipsum_original:
    # add the read items to a variable which becomes a string through read() and then split them into individual strings to form a list
    items = ipsum_original.read().split()


    # cycle through the number of paragraphs requested via a for loop
    for n in range(paragraphs):
        ninja_text = list(map(ninjarize, items))
        # use a to amend instead of w to write as we're cycling through and creating new paragraphs we don't want replaced
        with open('ninja_ipsum.txt', 'a') as ipsum_ninja:
            # use join to create a list of words, rather then just one due to ninjarize above
            # and add line breaks in between empty string spaces
            ipsum_ninja.write(' '.join(ninja_text) + '\n\n')
