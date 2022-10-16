from stock_winners.domain import StockValue
from stock_winners.domain import StockExchange
from importlib.resources import files
from datetime import datetime


class StockRepository:
    def get_stock_exchange(self):
        return self.get_stock_exchange_from_contents(self.file_contents)

    def get_stock_exchange_from_contents(self, contents):
        rows = [r for r in contents.split("\n") if len(r) > 0]
        rows = rows[1:]
        stock_values = list()
        for row in rows:
            validatated_row = ValidatedRow(row)
            stock_value = StockValue(
                    validatated_row.company_abbr,
                    validatated_row.value,
                    validatated_row.timestamp
                )
            stock_values.append(stock_value)

        return StockExchange(stock_values)

    @property
    def file_contents(self):
        # I do this split so that I can test it more easily
        return files('stock_winners').joinpath('data.csv').read_text()


class ValidatedRow:
    def __init__(self, row):
        row_split = row.split(";")
        if not len(row_split) == 3:
            raise ValueError(f"This row don't seem to have the right format: {row}")
        timestamp_raw = row_split[0]
        try:
            timestamp = datetime.strptime(timestamp_raw, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            raise ValueError(f"This row has a faulty date format: ({row}), message: ''{str(e)}'' ")
        # etcetera ...
        self.timestamp = timestamp
        self.company_abbr = row_split[1]
        self.value = int(row_split[2])
