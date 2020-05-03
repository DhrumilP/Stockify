from csv import DictReader
from django.core.management import BaseCommand
from stockApp.models import Stocks
from pytz import UTC


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the stock data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class CopyToDatabase:
    # Show this when the user types help
    help = "Loads data from trial.csv into our stock mode"
    def handle(self, *args, **options):
        for row in DictReader(open('./trial.csv')):
            stocks = Stocks()
            stocks.symbol = row['Symbol:']
            stocks.name = row['Names']
            stocks.price = row['Prices']
            stocks.change = row['Change']
            stocks.percent_change = row['% Change']
            stocks.market_caps = row['Market Cap']
            stocks.avg_volume = row['Avg Volume (3 Months)']
            stocks.volume = row['Volume']
            stocks.save()
