"""
Basic HRV related utility functions
 - HRV:
    - 'RMSSD' [default] sqrt of the mean of the squares of the successive differences between adjacent IBIs
    - 'SDNN'  the standard deviation of IBIs
    - 'SDSD'  standard deviation of the successive differences between adjacent IBIs
    - 'pNN50' proportion of pairs of successive IBIs that differ by more than 50/20 ms
    - 'pNN20' proportion of pairs of successive IBIs that differ by more than 20 ms
 - IBI
 - convert IBI (in msec) to BPM
"""

import numpy as np
