
# Download and extract data
import urllib.request
from PyPDF2 import PdfFileReader
import io #input/output
import pandas as pd
import sqlite3

def test_readdb():
    connection = sqlite3.connect(":memory:")
    connection = sqlite3.connect("project0/normanpd.db")

    cursor = connection.cursor()

    rows = cursor.execute("select nature, count(*) from project0 group by nature").fetchall()

    for row in rows:
        print(str(row[0]) + "|" + str(row[1]))

    cursor.close()
    connection.close()

    return None
    assert True

if __name__ == '__main__':
    test_readdb()


