#!/usr/bin/env bash
# 

LANGUAGE_CODES=${LANGUAGE_CODES:-da et fi mdf mhr nn-NO ru sv-SE uk}


for lcode in $LANGUAGE_CODES;do
    grep -v -f <(cut -f2 cv-corpus-12.0-2022-12-07/$lcode/test.tsv cv-corpus-12.0-2022-12-07/$lcode/dev.tsv cv-corpus-12.0-2022-12-07/$lcode/train.tsv) <(find cv-corpus-12.0-2022-12-07/$lcode/clips -name '*.mp3')|xargs -xn 50 rm -f
done
