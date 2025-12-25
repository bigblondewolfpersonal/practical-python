#!/usr/bin/env python

import csv
import gzip

def parse_csv(
        lines,
        select=None,
        types=None,
        has_headers=True,
        delimiter=",",
        silence_errors=False):
    """Parse a CSV file into a list of records."""
    if select and not  has_headers:
        raise RuntimeError("select only works with has_headers=True!")
    rows = csv.reader(lines, delimiter=delimiter)
    records = []
    if has_headers:
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
    for row_nr, row in enumerate(rows):
        try:
            if not row:
                continue
            if has_headers:
                if indices:
                    row = [row[idx] for idx in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                record = dict(zip(headers, row))
            else:
                record = row
                if types:
                    record = [func(val) for func, val in zip(types, record)]
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f"Row {row_nr+1}: Couldn't convert {row}")
                print(f"Row {row_nr+1}: Reason: {e}")
    return records

if __name__ == "__main__":
    #print(
    #    parse_csv(
    #        "Data/portfolio.dat",
    #        select=["name", "shares", "price"],
    #        types=[str, int, float],
    #        delimiter=" "
    #        )
    #    )
    #print(
    #    parse_csv(
    #        "Data/prices.csv",
    #        types=[str, float]
    #    )
    #)
    #with open("Data/missing.csv") as fn:
    #    print(
    #        parse_csv(
    #            fn,
    #            types=[str, int, float]
    #        )
    #    )
    with gzip.open("Data/portfolio.csv.gz", "rt") as fn:
        print(
            parse_csv(
                fn,
                types=[str, int, float]
            )
        )
# fileparsi.py
#
# Exercise 3.3