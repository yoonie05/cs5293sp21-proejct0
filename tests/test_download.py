# Download data
import urllib.request
from PyPDF2 import PdfFileReader
import io #input/output
import pandas as pd

# Download test
def test_download():
    # Set up the URL
    url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

    # Set up the headers
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
    # Read the data from the url
    p0_data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    assert True

if __name__ == '__main__':
    test_download()

