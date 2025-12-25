class TableFormatter:
    def headings(self, headers: list[str]):
        """
        Emit the table headings.
        """
        raise NotImplementedError()
    
    def row(self, rowdata: list[list]):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format.
    """
    def headings(self, headers: list[str]) -> None:
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-"*10 + " ")*len(headers))
    
    def row(self, rowdata: list[str]) ->  None:
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Emit a table in CSV format.
    """
    def headings(self, headers: list[str]) -> None:
        print(",".join(headers))
    
    def row(self, rowdata: list[str]) -> None:
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Emit a table in HTML.
    """
    def headings(self, headers: list[str]) -> None:
        print("<tr><th>", end="")
        print("</th><th>".join(headers), end="")
        print("</th></tr>")
    
    def row(self, rowdata: list[str]) -> None:
        print("<tr><td>", end="")
        print("</td><td>".join(rowdata), end="")
        print("</td></tr>")


def create_formatter(fmt: str):
    """
    Creates a formatter object of the specified type.
    """
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format '{fmt}'!")
