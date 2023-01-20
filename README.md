This repository contains simple baselines and helper scripts for  the [VarDial 2023](https://sites.google.com/view/vardial-2023) shared task on [Discriminating Between Similar Languages - Speech](https://dsl-s.github.io/) (DSL-S).

- `svm-baseline.py` an SVM-based classifier using pre-extracted i-vectors or x-vectors.
- `features/` includes a script for downloading the features
- `data/` includes a script for downloading the audio data

For more information, please visit the shared task [website](https://dsl-s.github.io/).

The basline script (after downloading features, without changing any
default parameters) gives the following output on the development set.

```
              precision    recall  f1-score   support

          da       0.53      0.35      0.42      1986
          et       0.57      0.85      0.68      2638
          fi       0.47      0.09      0.15      1405
          df       0.38      0.43      0.40        54
          hr       0.77      0.90      0.83     12905
          nn       0.01      0.01      0.01       168
          ru       0.58      0.78      0.67     10153
          sv       0.66      0.58      0.62      5012
          uk       0.59      0.28      0.38      8085

    accuracy                           0.65     42406
   macro avg       0.51      0.47      0.46     42406
weighted avg       0.64      0.65      0.63     42406

```
