#!/usr/bin/env python

from collections import namedtuple

stock_db = {}

Stock = namedtuple('Stock', ['name', 'symbol', 'purchase_date', 'purchase_price', 'num_of_shares'])

google = Stock('Google', 'GOOG', 'Mar-15-2016', '750.00', 3)
amazon = Stock('Amazon', 'AMZN', 'Feb-2-2016', '800.00', 4)
# print(google)

stock_db[google.name] = google
stock_db[amazon.name] = amazon


class Portfolio(object):
    def __init__(self, stock_database):
        self.stock_list = []
        if not stock_database:
            self.stock_db = []
        else:
            assert isinstance(stock_db, list)
            self.stock_db = stock_database

    def add_new_symbol(self, *args, **kwargs):
        stock = Stock(*args, **kwargs)
        print("Adding stock: {}".format(stock.name))
        self.stock_db.append(stock)

    def sell_stock(self, symbol, sell_quantity):
        try:
            current_quantity = self.stock_db[symbol].num_of_shares
            remaining_shares = current_quantity = sell_quantity
            if remaining_shares <= 0:
                raise ValueError("Sell quantity {} is greater than number of shares held: {}".format(sell_quantity, current_quantity))
            elif remaining_shares == 0:
                self.remove_symbol(symbol)
            else:
                self.stock_db[symbol].num_of_shares = remaining_shares
                print(self.stock_db[symbol])
        except AttributeError:
            print("We do not have attribute {}".format(sell_quantity))

    def remove_symbol(self, symbol):
        del self.stock_db[symbol]


    def ytd(self):
        pass

    def annual_ret_perf(self):
        pass

