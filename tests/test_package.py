"""Offline smoke tests (no network/fork required)."""

import pytest

import aave
from aave.v3 import InterestRateMode, get_all_markets


def test_public_api():
    assert "Aave" in aave.__all__
    assert aave.Aave is not None


@pytest.mark.parametrize(
    "mode,value",
    [(InterestRateMode.STABLE, 1), (InterestRateMode.VARIABLE, 2)],
)
def test_interest_rate_mode(mode, value):
    assert mode == value
    assert InterestRateMode(value) is mode


@pytest.mark.parametrize("chain_id,count", [(1, 4), (11155111, 1), (42161, 1)])
def test_known_markets(chain_id, count):
    markets = list(get_all_markets(chain_id))
    assert len(markets) == count


def test_unknown_chain_raises():
    with pytest.raises(ValueError):
        list(get_all_markets(0))
