#!/usr/bin/env python

import csv
import sys

import follow
import portfolio
import tableformat
import report

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield(dict(zip(headers, row)))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    #rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows

def filter_symbols(rows, names):
    for row in rows:
        if row["name"] in names:
            yield row

def ticker(file_pf: str, file_stocklog: str, fmt: tableformat.TableFormatter, cols: list[str]=["name", "price", "change"]):
    pf = portfolio.read_portfolio(file_pf)
    stocklog = follow.follow(file_stocklog)
    formatter = tableformat.create_formatter(fmt)
    rows = parse_stock_data(stocklog)
    rows = filter_symbols(rows, pf)
    formatter.headings(cols)
    for row in rows:
        formatter.row(row.values())


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} PORTFOLIO STOCKLOG [FMT]")
        sys.exit(1)
    fmt = "txt"
    file_pf = sys.argv[1]
    file_stocklog = sys.argv[2]
    if len(sys.argv) == 4:
        fmt = sys.argv[3]
    ticker(file_pf, file_stocklog, fmt=fmt)


if __name__ == "__main__":
    main()