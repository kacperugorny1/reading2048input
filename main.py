from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import os
import subprocess


def main():
    url = "https://play2048.co/"
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(10)
    board = [[0 for _ in range(4)] for _ in range(4)]
    previous_res = ""
    bodyElement = browser.find_element(By.TAG_NAME, "body")
    while True:
        board = [[0 for _ in range(4)] for _ in range(4)]
        soup = BeautifulSoup(browser.page_source)
        res = soup.find('div', {'class': 'tile-container'})
        if previous_res == res:
            continue
        for child in res.children:
            info = child["class"]
            posy = int(info[2][14]) - 1
            posx = int(info[2][16]) - 1
            size = int(info[1][info[1].find('-')+1:])
            if size > board[posy][posx]:
                board[posy][posx] = size
        print(board)
        solverProcess = subprocess.run(["./solver_2048.exe"],
                                       input="".join("".join(str(num) + " " for num in line) + "\n" for line in board),
                                       encoding="utf-8",
                                       capture_output=True
                                       )
        bodyElement.send_keys(solverProcess.stdout)
        time.sleep(0.5)
        previous_res = res


def remove_ads(browser: webdriver):
    all_iframes = browser.find_elements(By.TAG_NAME, "iframe")
    if len(all_iframes) > 0:
        print("Ad Found\n")
        browser.execute_script("""
            var elems = document.getElementsByTagName("iframe");
            for(var i = 0, max = elems.length; i < max; i++)
                 {
                     elems[i].hidden = true;
                 }
                              """)


if __name__ == "__main__":
    main()
