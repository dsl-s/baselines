The files here are not needed for the baseline. The download scripts
are provided to help participants download the audio data.  

**You should be ready to download 14G archives.**
(16G when uncompressed).

The shell script `get-cv-data.sh` downloads all audio data from the
[Common Voice](https://commonvoice.mozilla.org/en/datasets) used
in the shared task. The downloaded archive files include all recorded
scripts, including those that are not part of train/dev/test sets.
The script `cleanup.sh` removes the audio files that are not part of
training, development or test sets, opening up about 8G of space.

