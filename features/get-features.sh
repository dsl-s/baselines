#!/usr/bin/env bash

LANGUAGE_CODES=${LANGUAGE_CODES:-da et fi mdf mhr nn-NO ru sv-SE uk}
FILE_TYPES=${FILE_TYPES:-ivectors xvectors mfcc metadata}

for lcode in $LANGUAGE_CODES;do
    for typ in $FILE_TYPES;do 
        ext="tsv.gz"
        if [[ $typ == "mfcc" ]];then
            ext="txt.gz"
        fi
        for split in train dev;do
            wget -c -O $lcode-$typ-$split.$ext "https://zenodo.org/record/7555151/files/$lcode-$typ-$split.$ext?download=1"
        done 
    done
done
