import requests
from bs4 import BeautifulSoup
import csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://dte.maharashtra.gov.in/search-of-institute-results-2/?RegionID=6&RegionName=Pune'
response = requests.get(url, verify=False)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

with open('output-from-python.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    for row in table.find_all('tr'):
        csv_writer.writerow([cell.text for cell in row.find_all('td')])
