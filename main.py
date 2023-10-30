from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

url = "https://play2048.co/"
browser = webdriver.Chrome()
browser.get(url)
board = [[0 for _ in range(4)] for _ in range(4)]
board_previous = [row[:] for row in board]
previous_res = ""
bodyElement = browser.find_element(By.TAG_NAME, "body")
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
    bodyElement.send_keys('w')
    previous_res = res
