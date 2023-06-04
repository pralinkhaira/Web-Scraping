import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.example.com"
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Extract specific elements from the HTML
title = soup.title.text
paragraphs = soup.find_all('p')

# Print the extracted data
print("Title:", title)
print("Paragraphs:")
for p in paragraphs:
    print(p.text)
