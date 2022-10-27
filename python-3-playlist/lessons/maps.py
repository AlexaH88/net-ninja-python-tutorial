from random import shuffle


def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


words = ['beetroot', 'carrots', 'potatoes']
anagrams = []


# for loop method
for word in words:
    anagrams.append(jumble(word))
print(anagrams)


# map function method --> map(function, data)
# need to add list function to make it into a list as otherwise it returns an object
print(list(map(jumble, words)))


# comprehension method
print([jumble(word) for word in words])
