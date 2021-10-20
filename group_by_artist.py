#!/usr/local/bin/python3
from glob import glob

songs = glob('tabs/*.tex')
tabs = []
for s in songs:
    temp = s.split("_")
    song = temp[0].split("/")[1].replace("-"," ")
    artist = temp[1].split(".tex")[0].replace("-"," ")
    tabs.append((artist,song))
tabs.sort()


with open('group_by_artist.tex','w') as f:
    f.write("\\section*{Sorted By Artist}\n")
    for s in tabs:
        artist = s[0] 
        song = s[1] 
        f.write("{} - {} \dotfill \pageref{{{} - {}}} \n".format(artist,song,song,artist))
        f.write("\n")
