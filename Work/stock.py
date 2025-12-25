#!/usr/bin/env python

import json
import sys
import fileparse

class Stock:
    __slots__ = ["name", "_shares", "price"]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amt):
        self.shares = self.shares - amt
        return self.shares
    
    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', {self.shares}, {self.price})"
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Shares number expected an integer (got '{type(value)}')")
        self._shares = value

def main():
    with open(sys.argv[1]) as f_pf:
        portdicts = fileparse.parse_csv(f_pf, types=[str, int, float])
    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    for i in portfolio:
        print(f"{i.name}: {i.shares} {i.price} ({i.cost:.2f})")
    g = [s for s in portfolio if s.name == "AA"][0]
    print(g)
    for x in ["name", "shares"]:
        print(getattr(g, x))
    g = Stock("GOOG", 100, 120.1)
    print(g.__dict__)


if __name__ == "__main__":
    main()