from bs4 import BeautifulSoup
import requests

# requested url
url = "https://www.yallakora.com/match-center/"
request = requests.get(url)
content = request.text

# parse the content
soup = BeautifulSoup(content, 'html.parser')

# find links
soup.find('main', class_='cd-main-content')
date = soup.find('div', class_='dayName').find('span').text
numofmatches = soup.find('div', class_='toursMatchesNum').find('p').find('span', class_='matchesCount').text
print(numofmatches)

