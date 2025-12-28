#!/usr/bin/env python

import fileparse
import stock

class Portfolio:
    def __init__(self, holdings: list[stock.Stock]):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])
    
    def tabulate_stock(self):
        from collections import Counter
        total_stock = Counter()
        for s in self._holdings:
            total_stock[s.name] += s.stock
        return total_stock


def read_portfolio(portfolio_file: str) -> list[stock.Stock]:
    with open(portfolio_file) as f_pf:
        return Portfolio(
            [
                stock.Stock(d['name'], d['shares'], d['price'])
                for d in fileparse.parse_csv(
                    f_pf,
                    types=[str, int, float]
                    )
                ]
            )