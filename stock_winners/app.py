from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from stock_winners.repository import StockRepository
from stock_winners.serializers import EnvelopeSerializer


class StockWinners(RequestHandler):
    """
    Example:
    https://<base-uri>/api/winners
    """
    def get(self):
        repo = StockRepository()
        stock_exchange = repo.get_stock_exchange()
        diff_list = stock_exchange.get_daily_winners()
        envelope = EnvelopeSerializer(diff_list)
        return self.write(envelope.toJSON())


def make_app(debug=False):
    urls = [
        ("/api/winners", StockWinners),
    ]
    return Application(urls, debug=debug)


def start(port, debug=False):
    app = make_app(debug=debug)
    app.listen(port)
    IOLoop.instance().start()


if __name__ == '__main__':
    start(3000)
