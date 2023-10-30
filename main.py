from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://play2048.co/"
browser = webdriver.Chrome()
browser.get(url)
board = [[0 for _ in range(4)] for _ in range(4)]
board_previous = [row[:] for row in board]
previous_res = ""
while True:
    soup = BeautifulSoup(browser.page_source, features="lxml")
    res = soup.find('div', {'class': 'tile-container'})
    if previous_res == res:
        continue
    for child in res.children:
        info = child["class"]
        posy = info[2][14]
        posx = info[2][16]
        tile = {"size": info[1][info[1].find('-')+1:], "posy": posy, "posx": posx}
        print(tile)
    previous_res = res
