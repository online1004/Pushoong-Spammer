from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, os, requests, random

def CheckURL(userid):
        result = requests.get(f"https://pushoong.com/ask/{userid}")
        if result.status_code == 200:
            return True
        else:
            return False

def SpamPushoong(userid, msg, thread):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--incognito')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = f'https://pushoong.com/ask/{userid}'
    driver.get(url)
    time.sleep(0.5)
    driver.find_element(By.ID, "hide-modal-long").click()
    time.sleep(0.5)
    for i in range(thread):
        driver.find_element(By.ID, "ask_textarea").send_keys(msg)
        time.sleep(0.5)
        driver.find_element(By.ID, "ask_send").click()
        time.sleep(0.5)
    driver.quit()
    print("[+] SUCCESSㅣ도배가 성공적으로 완료되었습니다.")

def main():
    os.system("color B")
    print('=====================================')
    ids = input("아이디를 입력하세요 : ")
    thread = int(input("횟수를 입력하세요 : "))
    msg = input("메시지를 입력하세요 : ")
    print('=====================================')

    if CheckURL(ids):
        SpamPushoong(ids, msg, thread)
    else:
        print('존재하지 않는 ID 입니다.')

main()