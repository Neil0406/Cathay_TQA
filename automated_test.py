# 自動化測試

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs

'''
1. 使用Chrome App到國泰世華銀行官網(https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。
'''
def screenshot(png_name: str = "網頁選單.png"):
    opt = Options()
    opt.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, chrome_options=opt)
    driver.set_window_size(430, 932)
    try:
        driver.get("https://www.cathaybk.com.tw/cathaybk/")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        driver.save_screenshot(png_name)
        print("create_png: ",png_name)  
    except Exception as e:
        print(e)
    finally:
        driver.quit()

'''
2. 點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖。
'''
def element_click(png_name: str= "信用卡列表選單.png"):
    opt = Options()
    opt.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opt)
    driver.set_window_size(430, 932)
    result = []
    try:
        driver.get("https://www.cathaybk.com.tw/cathaybk/")
        burger_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="cubre-a-burger"]'))
        )
        burger_button.click()
        
        product_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="cubre-a-menuSortBtn -l1" and text()="產品介紹"]'))
        )
        product_button.click()
        
        credit_card_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="cubre-a-menuSortBtn" and text()="信用卡"]'))
        )
        credit_card_button.click()

        links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@class="cubre-a-menuLink"]'))
        )
        driver.implicitly_wait(10)
        driver.save_screenshot(png_name)
        for link in links:
            if link.text:
                result.append(link.text)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
    print("element: ",result, 'create_png: ', png_name)
    return result

'''
3. 個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖
'''
def card_count():
    opt = Options()
    opt.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opt)
    result = []
    try:
        driver.get("https://www.cathaybk.com.tw/cathaybk/personal/product/credit-card/cards/")
        driver.implicitly_wait(10)
        html = driver.page_source
        soup = bs(html,'html.parser')
        q = soup.select('section:nth-child(7) > div > div.cubre-o-block__component > div > div.swiper-wrapper > div.cubre-o-slide__item > div > div.cubre-m-compareCard__title')
        for i in q:
            result.append(i.text)

    except Exception as e:
        print(e)
    finally:
        driver.quit()
    return len(result)

if __name__ == '__main__':
    screenshot() # 1
    element_click() # 2
    card_count() # 3