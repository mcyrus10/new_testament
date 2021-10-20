#!/usr/local/bin/python3
from sys import argv

def transpose(chord,step):
    # {{{
    discrete = chord.split('-')
    for j,val in enumerate(discrete):
        if val not in ["|","x"]:
            discrete[j]=str(int(discrete[j])+step)
    return("-".join(discrete))
    # }}}

chordDict = {
            # major chords
            'C':r"|-0-3-2-0-1-0-|",
            'A':r"|-x-0-2-2-2-0-|",
            'G':r"|-3-2-0-0-3-3-|",
            'E':r"|-0-2-2-1-0-0-|",
            'D':r"|-x-x-0-2-3-2-|",
            'F#':r"|-2-4-4-3-2-2-|",
            'G#':r"|-4-6-6-5-4-4-|",
            # minor chords
            'Am':r"|-x-0-2-2-1-0-|",
            'Cm':r"|-x-3-5-5-4-3-|",
            'C#m':r"|-x-4-6-6-5-4-|",
            'Em':r"|-0-2-2-0-0-0-|",
            'Fm':r"|-1-3-3-1-1-1-|",
            'F#m':r"|-2-4-4-2-2-2-|",
            'Gm':r"|-3-5-5-3-3-3-|",
            'G#m':r"|-4-6-6-4-4-4-|",
            # 7
            'A7':r"|-x-0-2-0-2-0-|",
            'C7':r"|-x-3-2-3-1-0-|",
            'D7':r"|-x-x-0-2-1-2-|",
            'E7':r"|-0-2-0-1-0-0-|",
            'G7':r"|-3-5-3-4-3-3-|",
            # major 7 chords
            'Amaj7':r"|-x-0-2-1-2-0-|",
            'Cmaj7':r"|-3-3-2-0-0-0-|",
            'Dmaj7':r"|-x-x-0-2-2-2-|",
            'Fmaj7':r"|-1-3-3-2-1-0-|",
            'Gmaj7':r"|-3-2-0-0-0-2-|",
            # minor 7 chords
            'Em7':r"|-0-2-0-0-0-0-|",
            # suspended 2 chords
            'Asus2':r"|-x-0-2-2-0-0-|",
            'Dsus2':r"|-x-x-0-2-3-0-|",
            }

# major chords transpose
chordDict['Bb']=transpose(chordDict['A'],1)
chordDict['B']=transpose(chordDict['A'] ,2)
chordDict['Db']=transpose(chordDict['A'],4)
chordDict['F']=transpose(chordDict['E'] ,1)

# major chords transpose
chordDict['Bm']=transpose(chordDict['Am'],2)

chordDict['Bmaj7']=transpose(chordDict['Amaj7'],2)
chordDict['B7']=transpose(chordDict['A7'],2)

chordDict['Fm7']=transpose(chordDict['Em7'],1)
chordDict['F#m7']=transpose(chordDict['Em7'],2)
chordDict['Gm7']=transpose(chordDict['Em7'],3)

makeChord = lambda dictionary,val: print(r"{}\ {}\\".format(dictionary[val],val))

def diagrams(chords):
    print(r"|-E-A-D-G-B-e-|\\")
    print(r"---------------\\")
    for chord in chords:
        makeChord(chordDict,chord)

if __name__=="__main__":
    progression = []
    for chord in argv[1:]:
        progression.append(chord)
    diagrams(progression)
