import pytest
from ..datasets import fetch_saccade_cardiac


def test_fetch_saccade_cardiac(tmp_path):
    data = fetch_saccade_cardiac(data_dir=tmp_path)
    assert len(data.data) == 32
    assert data.headers == ["idx", "ibi", "saccade_onsets", "fixation_onsets"]
