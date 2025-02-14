import pytest

from utils.buy_sell_stock import max_profit


@pytest.mark.parametrize(
    ('prices, profit'),
    (
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 6, 3, 6, 9, 2, 4, 6, 8, 3], 7),
        ([1, 2], 1),
    ),
)
def test_max_profit(prices, profit) -> None:
    assert max_profit(prices) == profit
