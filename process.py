#!/usr/local/bin/python3
#------------------------------------------------------------------------------
#   this script will remove the backslash tabs and replace the first character
#   backslash with a period to hold the indentation
#------------------------------------------------------------------------------
from sys import argv
from os import system

# input file
file = argv[1]
system("cp {} /tmp".format(file))

# read in the tab
with open(file,'r') as f:
    text = f.read().split("\n")

# remove the empty strings from text
text=list(filter(None,text))
nlines = len(text)


# These are used as aruments to 'filter' to determine if a line has no chords
# or lyrics i.e. it only has spaces and backslashes
comparison1 = lambda string: string != " "
comparison2 = lambda string: string != "\\"

with open(file,'w') as f:
    # print the first three lines as they are
    f.write("{}\n".format(text[0]))
    f.write("{}\n".format(text[1]))
    f.write("{}\n".format(text[2]))

    # remove the tabs from the fourth line
    f.write("{}{}\n".format(text[3][0:8],text[3][16:]))

    # Process all the inner lines 
    for i,line in enumerate(text):
        if i >=4:
            phase1 = list(filter(comparison1,line))
            phase2 = list(filter(comparison2,phase1))
            # this condition tests if a line has no lyrics or chords and
            # inserts a blank line
            if phase2 == []:
                f.write("{}\n".format("\\\\"))
            # The last line
            elif line[-2] == "$":
                f.write("{} }}\n".format(line[8:-2]))
            # lines with a left bracket get this condition
            elif "lbrack" in line:
                f.write("{}\n".format(line[8:]))
            # lines with text that is left aligned get this condition
            elif line[8] != "\\":
                f.write("{}\n".format(line[8:]))
            # lines with spacing (non-left aligned get this condition)
            elif line[8] == "\\":
                f.write(".{}\n".format(line[9:]))

