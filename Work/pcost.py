#!/usr/bin/env python
# pcost.py

import csv
import sys

import fileparse
import portfolio
import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    pf = report.read_portfolio(filename)
    return pf.total_cost


def main(fargs: list) -> None:
    if len(fargs) < 2:
        raise SystemExit(f"Usage: {fargs[0]} file_portfolio, file_prices")
    cost = portfolio_cost(fargs[1])
    print('Total cost:', cost)


if __name__ == "__main__":
    main(sys.argv)