"""
Downloading datasets for demo
"""

import numpy as np

from nilearn.dataset.utils import _get_dataset_dir, _uncompress_file, _fetch_files


def _fetch_blink(data_dir, verbose=1):
    """
    This function helps in downloading and unzipping blink data from Galvez-Pol et. al 2020
    from Open Science Framework (OSF).
    https://osf.io/ye3rg/


    Reference
    ---------
    Galvez-Pol A, McConnell R, Kilner JM. Active sampling in visual search is coupled to the cardiac cycle. Cognition. 2020 Mar;196:104149. doi: 10.1016/j.cognition.2019.104149.
    """
    dataset_name = "saccade_cardiac"
    index_url = "https://osf.io/h5x84/download"
    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir, verbose=verbose)

    # fetch data and rename

    # uncompress data

    # load .mat file to arrys

    # dump to csv

    return data


def _fetch_saccade_fixation(data_dir, verbose=1):
    """
    This function helps in downloading and unzipping saccade and cardiac cycle data from Galvez-Pol et. al 2020
    from Open Science Framework (OSF).
    https://osf.io/ye3rg/


    Reference
    ---------
    Galvez-Pol A, McConnell R, Kilner JM. Active sampling in visual search is coupled to the cardiac cycle. Cognition. 2020 Mar;196:104149. doi: 10.1016/j.cognition.2019.104149.
    """
    dataset_name = "saccade_cardiac"
    index_url = "https://osf.io/rbt7w/download"
    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir, verbose=verbose)
    # fetch data and rename

    # uncompress data

    # load .mat file to arrys

    # dump to csv
    return data


def fetch_saccade_cardiac(data_dir, verbose=1):
        """
    This function helps in downloading and unzipping data used in Galvez-Pol et. al 2020
    from Open Science Framework (OSF).
    https://osf.io/ye3rg/


    Reference
    ---------
    Galvez-Pol A, McConnell R, Kilner JM. Active sampling in visual search is coupled to the cardiac cycle. Cognition. 2020 Mar;196:104149. doi: 10.1016/j.cognition.2019.104149.
    """

    return data
