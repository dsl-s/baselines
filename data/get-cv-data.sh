#!/usr/bin/env bash
# This script downloads all the raw data used in the shared task
# from the Common Voice project.
# 
# The downloaded files take 14G of space (and bandwidth).

LANGUAGE_CODES=${LANGUAGE_CODES:-da et fi mdf myv nn-NO ru sv-SE uk}
baseurl="https://mozilla-common-voice-datasets.s3.dualstack.us-west-2.amazonaws.com/cv-corpus-12.0-2022-12-07/"

for lcode in $LANGUAGE_CODES;do
    wget ${baseurl}cv-corpus-12.0-2022-12-07-${lcode}.tar.gz
done
