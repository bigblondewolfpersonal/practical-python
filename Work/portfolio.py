#!/usr/bin/env python

import stock

class Portfolio:
    def __init__(self, holdings: list[stock.Stock]):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])
    
    def tabulate_stock(self):
        from collections import Counter
        total_stock = Counter()
        for s in self._holdings:
            total_stock[s.name] += s.stock
        return total_stock