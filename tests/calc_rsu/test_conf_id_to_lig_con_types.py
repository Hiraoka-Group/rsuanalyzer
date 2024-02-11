import pytest

from rsuanalyzer.calc_rsu.conf_id_to_lig_and_types import (
    conf_id_to_con_types, conf_id_to_lig_types)


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFFLL", ["RR", "LL"]),  # chain
        ("RRFFLLBB", ["RR", "LL"]),  # ring
        ("RRFFLLBBRLFB", ["RR", "LL", "RL"])  # ring
    ]
)
def test_conf_id_to_lig_types(conf_id, expected):
    assert conf_id_to_lig_types(conf_id) == expected


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFFLL", ["FF"]),  # chain
        ("RRFFLLBB", ["FF", "BB"]),  # ring
        ("RRFFLLBBRLFB", ["FF", "BB", "FB"])  # ring
    ]
)
def test_conf_id_to_con_types(conf_id, expected):
    assert conf_id_to_con_types(conf_id) == expected