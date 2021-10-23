#!/usr/local/bin/python3
#------------------------------------------------------------------------------
#   Sort by artist
#       This script reads in all the text files in 'tabs', sorts them by artist
#       and writes a .tex file 
#------------------------------------------------------------------------------
from glob import glob

songs = glob('tabs/*.tex')
tabs = []
for s in songs:
    temp = s.split("_")
    song = temp[0].split("/")[1].replace("-"," ")
    artist = temp[1].split(".tex")[0].replace("-"," ")
    tabs.append((artist,song))

tabs.sort()

with open('sort_by_artist.tex','w') as f:
    f.write("\\section*{Sorted By Artist}\n")
    for s in tabs:
        artist,song = s
        f.write("{} - {} \dotfill \pageref{{{} - {}}} \n".format(artist,song,song,artist))
        f.write("\n")
