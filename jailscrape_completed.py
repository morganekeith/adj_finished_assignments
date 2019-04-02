import urllib2, csv
from bs4 import BeautifulSoup
/* This line of code shows that we are urllib2 (which allows us to visit websites using Python), Pythons csv module and the most recent version of BeautifulSoup to parse the websites HTML and extract data. */

outfile = open('jaildata.csv', 'w')
/* The outfile creates a path to the file we are creating with our scraper. */
writer = csv.writer(outfile)
/* The writer tool will dump out the lists that we collect from the site into the outfile. */

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
/* This is the website that we are scraping our data from. */
html = urllib2.urlopen(url).read()
/*This line of code has Python open the websites HTML, where the data we are scraping is located, and read it.*/

soup = BeautifulSoup(html, "html.parser")
/* This specifies the parser library that you want to use. */

tbody = soup.find('tbody', {'class': 'stripe'})
/* This line of code instructs BeautifulSoup how to locate the specific data that we are trying to scrape. */

rows = tbody.find_all('tr')
/* Here we dig down into the table and return a list of rows using the <tr> tag inside of the table. */

for row in rows:
    /* The for command sets up guidelines for navigating the different row of data. */

    cells = row.find_all('td')
    /* This allows each cell within the row to be looped through, identifying them by using HTMLs <td> tag that creates cells. */

    data = []
    /* The list for data appears empty. Either this is intentional or the list will be filled after the rows and cells are looped through. */
    for cell in cells:
        data.append(cell.text.encode('utf-8'))
        /* The data scraped from the cells is added onto a larger list and is encoded using the standard utf-8, which will allow the final product (xml or html) to function properly. This differs from the BeautifulSoup standard of Unicode. */

    writer.writerow(data)
    /* This final command dumps out our list of lists, so our rows of cells. */
