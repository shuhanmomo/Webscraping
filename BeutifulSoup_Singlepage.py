from bs4 import BeautifulSoup
import requests
# paste the website link below
website = "https://en.wikipedia.org/wiki/New_York_City_Housing_Authority"
result = requests.get(website)
content = result.text   # to get the content of the website by using .text method
soup = BeautifulSoup(content, 'lxml')  # create a soup and using lxml parser to parse the HTML code
html_code = soup.prettify() # make the code look nicer
# start locating the data to be scraped down
box = soup.find('table',class_ = 'wikitable')  # first locate the box where the data belongs to and narrow down
scraped = box.find('tbody').get_text(strip=True, separator='\n ')  # get text to get the strings, strip and seperator setting can be adjusted
print(scraped)
# save the file into a txt
with open('test.txt','w') as file:
     file.write(scraped)


