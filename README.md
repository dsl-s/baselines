This repository contains simple baselines and helper scripts for  the [VarDial 2023](https://sites.google.com/view/vardial-2023) shared task on [Discriminating Between Similar Languages - Speech](https://dsl-s.github.io/) (DSL-S).

- `svm-baseline.py` an SVM-based classifier using pre-extracted i-vectors or x-vectors.
- `features/` includes a script for downloading the features
- `data/` includes a script for downloading the audio data

For more information, please visit the shared task [website](https://dsl-s.github.io/).

The basline script (after downloading features, without changing any
default parameters) gives the following output on the development set.

```
              precision    recall  f1-score   support

          da       0.51      0.36      0.42      1986
          et       0.56      0.86      0.68      2638
          fi       0.41      0.09      0.15      1405
         mdf       0.31      0.52      0.39        54
         myv       0.03      0.02      0.02       239
          nn       0.01      0.01      0.01       168
          ru       0.57      0.83      0.68     10153
          sv       0.67      0.60      0.64      5012
          uk       0.61      0.32      0.42      8085

    accuracy                           0.58     29740
   macro avg       0.41      0.40      0.38     29740
weighted avg       0.58      0.58      0.55     29740

```
