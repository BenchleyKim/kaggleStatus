import requests
from bs4 import BeautifulSoup
url  = "https://www.kaggle.com/bottlechrome97"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
res = requests.get(url, headers=headers)

print(res.status_code)
res.raise_for_status()

with open("kaggle.html",'w', encoding="utf8") as f :
    f.write(res.text)

soup = BeautifulSoup(res.text,"lxml")

ranks = soup.find_all("script", attrs={"class":"kaggle-component"})
for rank in ranks :
    
    print(rank)


