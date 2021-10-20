#!/bin/bash
#==============================================================================
#   this script is for scraping tabs off of UG
#   it takes a url as an argument, then it formats it and outputs it with the
#   second argument as a file name
#       e.g.:
#            < REPLACE SPACES WITH HYPEN >
#           ./uG-rip.sh <url> <song name> <artist name>
#==============================================================================

url=$1
read -p "song name (spaces separated with hyphen) = " song
read -p "artist (spaces separated with hyphen) = " artist
j=0
curl $url > temp.txt
f=temp.txt

# Flag the start of the tab
sed -ie 's/{&quot;content&quot;:&quot;/\
    \
    <START OF TAB?>\
    \
    /g' $f 

# Flag the end of the tab
sed -ie 's/;,&quot;revision_id&quot;/\
    \
    <END OF TAB?>\
    \
    /g' $f 

#------------------------------------------------------------------------------
#   REMOVE all unwanted characters in the body of the tab
#------------------------------------------------------------------------------
expr=(  '\[tab\]' '\\r' '&quot' '&mdash\;' '\[\/tab\]' '\[ch\]' '\[\/ch\]'
        '&ndash' '&lsquo')
for e in ${expr[*]}; do
    grep -q "$e" $f && sed -ie "s/$e//g" $f
done

#------------------------------------------------------------------------------
#   REPLACE all unwanted characters in the body of the tab
#------------------------------------------------------------------------------
expr2=( '\[' ']' '$' '&rsquo;' '&eacute;' '&amp' '&hellip;' '&ldquo;' '&rdquo;' )
replace=( '\\lbrack ' '\\rbrack' '\\$' "'" 'e' '\\&' '...' '``' '"')
j=0
for e in ${expr2[*]}; do
    grep -q "$e" $f && sed -ie "s/$e/${replace[j]}/g" $f
    j=$(( j+1 ))
done

#      Replace sharps in latex
#          |      make all of the \n into new lines in the raw text file
#          |           |
#          v           v
sed -ie 's/#/\\#/g ; s/\\n/\\\\\
    /g' $f


# find the start and end line of the formatted tab
start=$(grep -n '<START OF TAB?>' $f | sed 's/[^[0-9]//g')
end=$(grep -n '<END OF TAB?>' $f | sed 's/[^[0-9]//g')

echo "Start of tab is on line $start"
echo "End of tab is on line $end"

# create file and extract the bounded portion of the tab
file=tabs/${song}_${artist}.tex
label_string="$(echo $song | sed 's/-/ /g') - $(echo $artist | sed 's/-/ /g')"
echo "\\newpage" > $file
echo "\\section{$label_string}" >> $file
echo "\\label{$label_string}" >> $file
#                                                                       This replaces all of the 
#                                                                       spaces " " with "\ "
#                                                                       and removes underscores 
#                                                                                  |
#                                                                         _________v________
echo "\\texttt{$(awk "NR > $(( start+1 )) && NR < $(( end-1 ))" $f | sed 's/ /\\ /g ; s/_//g' )}" >> $file


#sed -ie "s/\\end{document}/\\input{tabs\/${song}_${artist}.tex} \
#\\
#\\\\end{document}/g" musicBook.tex >> musicBook.tex

./process.py $file
