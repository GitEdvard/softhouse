import pytest
from stock_winners.repository import StockRepository
from datetime import datetime


@pytest.fixture
def example_data():
    data_contents_list = [
        "Date;Kod;Kurs",
        "2017-01-01 12:00:00;ABB;217",
        "2017-01-01 12:00:01;NCC;122",
        "2017-01-01 12:00:02;ABB;218",
    ]
    return "\n".join(data_contents_list)


def test_repository(example_data):
    repo = StockRepository()

    result = repo.get_stock_exchange_from_contents(example_data)

    stock_values = result.stock_values
    assert stock_values[0].company_abbr == "ABB"
    assert isinstance(stock_values[0].timestamp, datetime)

