import requests
from bs4 import BeautifulSoup


url = 'https://7daysperformance.co.uk'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.title.text
links = soup.find_all('Sold Out')

print(title)
