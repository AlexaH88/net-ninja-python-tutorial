# # option 1, necessitation close command at the end

# ipsum_file = open('files/ipsum.txt')

# # read the file with a for loop, accessing each line
# for line in ipsum_file:
#     print(line)
#     # strip line between each paragraph
#     print(line.rstrip())


# # reset cursor to beginning of file to be able to read it again
# # using 0 character ie start of file
# ipsum_file.seek(0)


# # readlines method
# lines = ipsum_file.readlines()
# print(lines)


# # read from 50th character
# ipsum_file.seek(50)
# # read 100 characters from that point
# file_text = ipsum_file.read(100)
# print(file_text)


# # close file once done as performance will suffer otherwise
# ipsum_file.close()


# option 2
# filter out > SEQUENCE line
def sequence_filter(line):
    # checking for True or False and keeping whichever is True ie does not include <
    return '>' not in line


# dna_file is the variable you're storing it in
# with acts like while ie while the file is open
# don't need to close the file as you're only acting on the open file within the code block
with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    # apply above filter to variable
    # pass in the function first, then the variable you're filtering as created above
    # apply filter method to be able to return a list and not an object and print
    print(list(filter(sequence_filter, lines)))
