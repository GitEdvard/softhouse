import click
from stock_winners.app import start as start_app


@click.command("stock-winners")
@click.option("--port", help="Port which stock-winner will listen to (default: 9999).", type=click.INT, default=9999)
@click.option('--debug', is_flag=True, default=False, help="Enable debug mode.")
def start(port=9999, debug=False):
    start_app(port, debug)

