#!/usr/bin/env python
# pcost.py

import csv
import sys

import fileparse
from stock import Stock

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, 'rt') as f_pf:
        pf = [
            Stock(d['name'], d['shares'], d['price'])
            for d in fileparse.parse_csv(
                f_pf,
                types=[str, int, float]
                )
        ]
        for h in pf:
            total_cost += h.cost()
    return sum([x.cost() for x in pf])


def main(fargs: list) -> None:
    if not len(fargs) == 2:
        raise SystemExit(f"Usage: {fargs[0]} file_portfolio, file_prices")
    cost = portfolio_cost(fargs[1])
    print('Total cost:', cost)


if __name__ == "__main__":
    main(sys.argv)