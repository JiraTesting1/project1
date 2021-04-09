import requests
from bs4 import BeautifulSoup
url = "https://d4954819a40c.ngrok.io/"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
vibration = int(soup.get_text())