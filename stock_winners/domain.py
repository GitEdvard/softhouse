from datetime import datetime
from collections import defaultdict


class StockValue:
    def __init__(self, company_abbr, value, timestamp):
        self.company_abbr = company_abbr
        self.value = value
        self.timestamp = timestamp


class StockExchange:
    """
    This is the core functionality, calculating an ordered list of stock change since last day
    """
    def __init__(self, stock_values):
        self.stock_values = stock_values
        stock_histories = list()
        for company_abbr in self.company_list:
            stock_values_for_company = [
                item for item in self.stock_values if item.company_abbr == company_abbr
            ]
            stock_history = StockHistory(stock_values_for_company)
            stock_histories.append(stock_history)
        self.stock_histories = stock_histories

    def raise_exeption(self):
        raise Exception("hej")

    @property
    def company_list(self):
        return list(set(item.company_abbr for item in self.stock_values))

    def get_daily_winners(self):
        stock_motions = \
            [stock_history.get_latest_motion() for stock_history in self.stock_histories]
        stock_motions.sort(key=lambda x: x.change_in_percent, reverse=True)
        self.raise_exeption()

        return stock_motions[:3]


class StockHistory:
    """
    A stock history for a specific company
    """
    def __init__(self, stock_values):
        self.stock_values = stock_values
        # Validate there are stock values for today and yesterday

    def _get_latest_value_for_each_day(self):
        stock_values_by_day = defaultdict(lambda: list())
        for item in self.stock_values:
            stock_values_by_day[datetime.strftime(item.timestamp, "%y%m%d")].append(item)

        latest_value_by_day = dict()
        for day in stock_values_by_day:
            daily_stock_values = stock_values_by_day[day]
            daily_stock_values.sort(key=lambda x: x.timestamp, reverse=True)
            latest_value = daily_stock_values[0]
            latest_value_by_day[day] = latest_value

        return latest_value_by_day

    def get_latest_motion(self):
        latest_value_by_day = self._get_latest_value_for_each_day()
        # Fetch the two latest items in case of more than two days
        daily_value_list = [latest_value_by_day[day] for day in latest_value_by_day]
        daily_value_list.sort(key=lambda x: x.timestamp, reverse=True)
        todays_stock_value = daily_value_list[0]
        yesterdays_stock_value = daily_value_list[1]
        return LatestStockMotion(todays_stock_value, yesterdays_stock_value)


class LatestStockMotion:
    def __init__(self, todays_stock_value, yesterdays_stock_value):
        self.company_abbr = todays_stock_value.company_abbr
        self.change_in_percent = (todays_stock_value.value/yesterdays_stock_value.value - 1) * 100
        self.latest = todays_stock_value.value
