"""
Downloading datasets for demo
"""
import os, shutil
from pathlib import Path
import scipy.io as sio
from nilearn import datasets as nd
from sklearn.utils import Bunch


def fetch_saccade_cardiac(data_dir, verbose=1):
    """
    This function helps in downloading and unzipping data used in
    Galvez-Pol et. al 2020from Open Science Framework (OSF).
    https://osf.io/ye3rg/

    Parameters
    ----------
    data_dir : string, optional
        Path of the data directory. Used to force data storage in a specified
        location. Default: None

    verbose : int, optional
        Verbosity level (0 means no message). Default=1.

    Returns
    -------
    data : sklearn.datasets.base.Bunch
        Dictionary-like object, the interest attributes are :
        - 'data': numpy array list. Array size: timeseires by 4 per subject.
        - 'header': string list. Name of each column of the data array.

    Reference
    ---------
    .. [1] `Galvez-Pol A, McConnell R, Kilner JM. Active sampling in visual
       search is coupled to the cardiac cycle. Cognition. 2020 Mar;196:104149.
       doi: 10.1016/j.cognition.2019.104149.`

    Notes
    -----
    The raw data did not contain headers. Hence authors of this toolbox retain
    information neccssary for the demo.

    """
    if data_dir is None:
        data_dir = "./"  # use current dir

    dataset_name = "saccade_cardiac"
    data_dir = nd.utils._get_dataset_dir(
        dataset_name, data_dir=data_dir, verbose=verbose
    )

    files = [
        (
            "sourcedata.zip",
            "https://osf.io/rbt7w/download",
            {"move": "sourcedata.zip"},
        )
    ]
    # fetch data and rename
    path_to_files = nd.utils._fetch_files(data_dir, files, verbose=verbose)

    # uncompress data
    for f in path_to_files:
        tmp_path = f.split(".zip")[0]
        filename = f.split(os.sep)[-1]
        os.mkdir(f.split(".zip")[0])
        shutil.move(f, tmp_path)
        nd.utils._uncompress_file(os.path.join(tmp_path, filename))

        # the data has no labels so I will only use the ones maxine figured out
        keep_col = [0, 3, 1, 8]
        col_labels = ["idx", "ibi", "saccade_onsets", "fixation_onsets"]

        data_array = {}
        for s in Path(tmp_path).glob("*.mat"):
            s_id = s.name.split("_")[0]
            # save_to = s.parents[2] / f"{s_id}.tsv"
            # load .mat file to arrys
            content = sio.loadmat(s)["Saccades_Mx3"]
            data_array[s_id] = content[:, keep_col]

    return Bunch(data=data_array, headers=col_labels)
