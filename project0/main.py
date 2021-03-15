
# Download and extract data
import urllib.request
from PyPDF2 import PdfFileReader
import io #input/output
import pandas as pd

# Set up the URL
url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

# Set up the headers
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
# Read the data from the url
p0_data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
# Change the byte type dataset.
f = io.BytesIO(p0_data) # byte data ==> english
# Send to PdfFileReader
reader = PdfFileReader(f)

# Get the number of pages in the document
numPage = reader.getNumPages()

# Empty DataFrame
output = pd.DataFrame()
# For loop for page loading
for i in range(0, numPage, 1):
    # Get the list of the data points using the split by "\n"
    lst = reader.getPage(i).extractText().split("\n")
    # on page 11: combine 'CHAUTAUQUA' 'AVE' to 'CHAUTAUQUA AVE'
    if i == 10:
        lst[17:19]=[''.join(lst[17:19])]

    # Get the number of data points within the page
    numberofdata = (len(lst)//5)*5
    # Creat the lists for column 0, column 1, column 2, column 3 , column 4 for pattern saving and columns.
    lst0 = []
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []
    # Recognize the pattern and run the loop.
    for j in range(0, numberofdata, 1):
        if j % 5 == 0:
            lst0.append(lst[j])
        elif j % 5 == 1:
            lst1.append(lst[j])
        elif j % 5 == 2:
            lst2.append(lst[j])
        elif j % 5 == 3:
            lst3.append(lst[j])
        elif j % 5 == 4:
            lst4.append(lst[j])
    # Create the list in list
    lst = [lst0, lst1, lst2, lst3, lst4]
    df = pd.DataFrame(lst).T
    # If it is the first page, then get the header from the first row of the dataframe
    if i == 0:
        df.columns = df.loc[0, :]
        df.columns.name = ""
        df = df.loc[1:].reset_index(drop = True)
    # If not, then get it from output dataframe.
    else:
        df.columns = output.columns
        df = df.reset_index(drop = True)
    # Stack the outcomes
    output = pd.concat([output, df])

# Reset the index
output = output.reset_index(drop = True)
output = output.rename({'Date / Time': 'time', 'Incident Number':'number', 'Location': 'location', 'nature': 'nature', 'Incident ORI': 'ori'}, axis='columns')
# Save the outcome
output.to_csv("output.csv", index = False, sep="|")

import sqlite3

def readdb():
    connection = sqlite3.connect(":memory:")
    connection = sqlite3.connect("project0/normanpd.db")

    cursor = connection.cursor()

    rows = cursor.execute("select nature, count(*) from project0 group by nature").fetchall()

    for row in rows:
        print(str(row[0]) + "|" + str(row[1]))

    cursor.close()
    connection.close()
    
    return None

if __name__ == '__main__':
    readdb()


