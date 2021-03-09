# CaTT
Cardiac Interoception Toolbox

Authors: Maxine Sherman, Hao-Ting Wang


## Data
Currently support ECG data
A txt file of two compulsory columns of data of same leghth `n`:
 - ecg: n x 1 array containing continuous ECG data for each time point.
 - onset: an n x 1 vector containing integer indicating the the onset of stimuli/response for each time point

Other optional columns depending on your data:
 - time: n x 1  array containing continuous timestamps in mscs for each time point; can be constructed by a given sampling rate
 - response: n x 1 vector containing participant response for each time point (nan or response code in int)
