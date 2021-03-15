# cs5293sp21-project0
# Yoon Hi Sung

# Project description
This project is to: 
1) download an incident pdf file from the Norman, Oklahoma police department reports, 
2) extract data fields (Date/Time, Incident number, Location, Nature, Incident ORI), 
3) create a SQLite database,
4) insert the data into the database,
5) print each nature (alphabetically) and its frequency

# 1) Download a pdf file 
__ A recent incident file (March 1) was selected from the police department website.
__ Based on the example code that Dr. Grant gave, downloaded it with the name of "p0_data"
__ An error occured: 'module urllib' has no attribute 'request.' SJ recommended using "import urllib.request" not "import urllib," which solved the error.
__ The data was read by using "PdfFileReader." 
__ An error occured: Data couldn't be read since "p0_data" consists of bytes. "io" module was used to resolve the issue. JournalDev site was used as a reference to understand the module (Refer to COLLABORATORS).
__ To check if the download successfully, a test file was created: "test_download.py" in the tests directory, which passed the test.

# 2) Extract data 
__ All pages were read by using reader.getPage() function and for loop function. 
__ Using regular expressions for extracting data was not understandable to me, instead list functions were used since data involved in each column were repeated every five elements.
__ A total of five lists were created for Date/Time, Incident Number, Location, Nature, Incident ORI.
__ If an element index is divided by 5, leading to the remainder 0, the element should be the first column for Date/Time. If the remainder is 1, the element should be for Incident Number. Similarly, the remainder 2 means Location, the remainder 3 means Nature, and the remainder 4 means Incident ORI. 
__ Using the for loop function, lst0, lst1, lst2, lst3, list4 were created, generating one total list, "lst"
__ Using pandas package, a dataframe was made from the lst. 
__ A bug was found: in the middle of the data, some ORI data were in the Data/Time function. Looking back into the dataset, when the location information consists of two rows in the pdf file (page 11 in the file downloaded), the location data is read into two data elements. So, using list merge code (i.e., lstp17:19] =[''. join(lst[17:19])]), the bug was resolved.
__ Given only the first page has the column titles, using .loc function, the titles were set as column names of the dataframe.
__ Because of this setting, the index was started from 1, not 0. By using .reset_index fucntion, the issue was resolved.
__ To make titles shorter(for coding convenience), .rename function used: the column titles are now "time" "number" "location" "nature" and "ori."
__ The dataframe was stored as a csv file with the name of "output.csv" with the separator of "|"
__ To test the code so far, test_extract.py was created, which passed the test.    

# 3) Create a SQLite database
__ Accessed to sqlite (by installing sqlite3)
__ A table (project0) was created by importing the output.csv file: ".import output.csv project0"

# 4) Insert the data into the dababase
__ The table was saved as database with the name of normanpd: ".save normanpd.db"
__ By using "import sqlite3," accessed sqlite data memroy and brought the normanpd.db.

# 5) Print each nature (alphabetically) and its frequency
__ To execute sorting by nature and showing its frequency, a sqlite code was directly input by using .connection and .execute.
__ An error occured: since the command "pipenv run python project0/main.py" is executed in the "cs5293sp21-project0," the main.py file cannot be read. So, sqlite3.connect("normanpd.db") was corrected to sqlite3.connect("project0/normanpd.db"), which resolved the error._ 
__ An issue occured: When "print(row)" to print out the results, results included () and "". To make it solved, the data was parsed, made into string. In addition, separator "|" was added.  
__ To test the code specifically focusing on reading database, test_readdb.py was created, which passed the test.


