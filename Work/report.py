#!/usr/bin/env python

from collections import Counter
import sys

import fileparse
import portfolio
import stock
import tableformat


def read_portfolio(portfolio_file: str) -> list[stock.Stock]:
    with open(portfolio_file) as f_pf:
        return portfolio.Portfolio(
            [
                stock.Stock(d['name'], d['shares'], d['price'])
                for d in fileparse.parse_csv(
                    f_pf,
                    types=[str, int, float]
                    )
                ]
            )


def read_prices(prices_file: str) -> list:
    with open(prices_file) as f_prices:
        prices = fileparse.parse_csv(
            f_prices,
            has_headers=False,
            types=[str, float]
            )
    return prices


def make_report_data(portfolio: list[stock.Stock], prices: list):
    report_out = []
    for h in portfolio:
        current_price = [tp for tp in prices if tp[0] == h.name][0][1]
        change = current_price - h.price
        report_out.append(
           ( 
                h.name,
                h.shares,
                current_price,
                change
                )
            )
    return report_out


def portfolio_report(file_portfolio: str, file_prices: str, fmt: str ="txt") -> None:
    pf = read_portfolio(file_portfolio)
    prices = read_prices(file_prices)
    report = make_report_data(pf, prices)
    formatter = tableformat.create_formatter(fmt)
    #print_report(report, formatter)
    print_table(pf, ["name", "shares", "price"], formatter)


def print_report(reportdata: list[tuple], formatter: tableformat.TableFormatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def print_table(portfolio: list[stock.Stock], columns: list[str], formatter: tableformat.TableFormatter) -> None:
    """Print a table with requested columns."""
    formatter.headings(columns)
    for r in portfolio:
        rowdata = []
        for c in columns:
            rowdata.append(str(getattr(r, c)))
        formatter.row(rowdata)

def main(fargs: list) -> None:
    if len(sys.argv) not in [3, 4]:
        raise SystemExit(f"Usage: {fargs[0]} file_portfolio, file_prices [format]")
    fmt = "txt"
    if len(sys.argv) == 4:
        fmt = sys.argv[3]
    portfolio_report(sys.argv[1], sys.argv[2], fmt)

if __name__ == "__main__":
    main(sys.argv)