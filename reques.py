import requests 
from bs4 import BeautifulSoup


req = requests.get('https://www.kaggle.com/bottlechrome97')
html = req.text

soup = BeautifulSoup(html, 'html.parser')
mytitles = soup.find_all('//*[@id="profile-container"]/div[3]/div/div[2]/div/div[1]/div[2]/div/div/a/div/div[1]/p[2]')

print(mytitles)
for title in mytitles :
    print(title)
