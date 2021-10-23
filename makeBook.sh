#!/bin/sh
#------------------------------------------------------------------------------
#   this is sort of a hack makefile to have one less file and since this has
#   some semi-complicated operations I decided to execute this with a shell
#   script
#   Example exeuction:
#       ./makeBook.sh
#------------------------------------------------------------------------------

tabs=( $(ls tabs/) )

python3 sort_by_artist.py

target=new_testament.tex
# write the .tex file
header=( 
        "\\documentclass{article}" 
        "\\usepackage[a4paper,total={7.5in,10in}]{geometry}" 
        "\\usepackage[linktocpage=true]{hyperref}"
        "\\usepackage{graphicx}"
        "\\usepackage{amsmath}" 
        "\\setlength\\\\parindent{0pt}" 
        "\\makeatletter"
        "\\\renewcommand{\\\\l@section}{\\\\@dottedtocline{1}{1.5em}{2.6em}}"
        " " 
        "\\\title{New-Testament}" 
        " " 
        "\\\begin{document}" 
        "\\maketitle" 
        "\\\vfill"
        "\\\begin{center}"
        "\includegraphics[width = 0.8\\\textwidth]{bear_playing_harp.jpeg}"
        "\\\end{center}"
        "\\\newpage" 
        "\\input{the_good_word.tex}"
        "\\\newpage" 
        "\\\tableofcontents" 
        "\\\newpage" 
        "\\input{sort_by_artist.tex}"
        "\\\newpage" 
        " " 
        )

[ -f $target ] && rm $target

# Write header lines into file
for line in ${header[*]};
do
    echo "$line" >> $target
done


# Write Tabs
for tab in ${tabs[*]};
do
    echo "\\input{tabs/$tab}" >> $target
done

echo "\\end{document}" >> $target

# Compile the document
pdflatex --shell-escape -interaction=nonstopmode $target
