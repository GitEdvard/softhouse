from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class StockWinners(RequestHandler):
    """
    Example:
    https://<base-uri>/api/winners
    """
    def get(self):
        print("hello")


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

