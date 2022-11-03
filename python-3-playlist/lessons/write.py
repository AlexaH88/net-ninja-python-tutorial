# include second argument ('w' which stands for write) in the open function to allow for writing to file
with open('files/write.txt', 'w') as write_file:
    write_file.write('Hey there ninjas, python is awesome')
    write_file.write('\nI love it so much, I dream in python')

# run the file in the console, and the text will be written into the txt file

# if you need to add anything more to the text file after having coded other items, use 'a' for amend, otherwise it will overwrite the previous contents
with open('files/write.txt', 'a') as write_file:
    write_file.write('\nThe dreams involve snakes...')


quotes = [
    '\nI can resist everything, except temptation'
    '\nWe are all in the gutter, but some of us are looking at the stars'
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt', 'a') as write_file:
    # writelines method expects a list so it can cycle through each element
    write_file.writelines(quotes)
