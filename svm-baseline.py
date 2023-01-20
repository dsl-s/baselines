#!/usr/bin/env python3
""" Simple linear SVM baseline for the DSL-S 2023 task.
"""

import argparse
import logging
logging.basicConfig(format='%(asctime)s: %(message)s',
                    level=logging.INFO)
import glob
import os
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.metrics import classification_report

def read_vectors(datadir='features/',
                 vectype='xvectors', split='train',
                 subsample=None):
    pattern = os.path.join(datadir, f"*-{vectype}-{split}.tsv.gz")
    vecsize = 512
    if vectype == 'ivectors':
        vecsize = 400
    header = ['cvpath', 'text', 'age', 'sex']\
           + [f"v{i:03d}" for i in range(vecsize)]
    data = None
    if subsample:
        logging.info(f"Subsampling to {subsample} instances per class.")
    for fname in glob.glob(pattern):
        lang = os.path.basename(fname).split('-')[0]
        langdata = pd.read_csv(fname,
                        names=header,
                        compression='gzip',
                        low_memory=False,
                        delimiter="\t")
        logging.info(f"{fname}: {langdata.shape}")
        langdata['language'] = lang
        if subsample and len(langdata) > subsample:
            langdata = langdata.sample(n=subsample)
        if data is None:
            data = langdata
        else:
            data = pd.concat((data, langdata))
    return data

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
#    ap.add_argument('input')
    ap.add_argument('--subsample', '-s', type=int, default=0)
    ap.add_argument('--subsample-devset', '-S', type=int, default=0)
    ap.add_argument('--vectype', '-v', default='xvectors')
    ap.add_argument('--C', '-C', type=float, default=0.005)
    ap.add_argument('--kernel', '-k', default="linear")
    args = ap.parse_args()

logging.info("Reading training data.")
traindf = read_vectors(vectype=args.vectype, subsample=args.subsample)
logging.info("Reading validation data.")
devdf = read_vectors(split='dev', subsample=args.subsample_devset)

logging.info("Training the classifier.")
if args.kernel == 'linear':
    clf = LinearSVC(C=args.C, class_weight='balanced', max_iter=5000)
else:
    clf = SVC(C=args.C, kernel=args.kernel, class_weight='balanced')
train_x = traindf[[col for col in traindf.columns if col.startswith('v')]]
train_y = traindf['language']
clf.fit(train_x, train_y)

logging.info("Predicting.")
dev_x = devdf[[col for col in devdf.columns if col.startswith('v')]]
dev_y = devdf['language']
pred = clf.predict(dev_x)
print(classification_report(dev_y, pred))
