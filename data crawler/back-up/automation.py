from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = 'https://tinhocngoisao.com/collections/laptop-asus'
driver.get(url)
time.sleep(2) #sleep for 2 sec
element = driver.find_element("xpath", '//*[@class="btn-load__more"]')
element.click()
# driver.quit()
# driver.quit()
# def open_browser():
#     PATH = "C:\Program Files (x86)\chromedriver.exe"
#     driver = webdriver.Chrome(PATH)
#     url = 'https://tinhocngoisao.com/collections/laptop-asus'
#     driver.get(url)
    # driver.find_element_by_class('btn-load__more').click()
    # element = driver.find_element_by_xpath("//a[contains(@class, 'btn-load__more')]")
    # element = driver.find_element("xpath", '//*[@class="btn-load__more"]')
    # print('---------------------------------')
    # print(element)
    # element.click()
    # driver.quit()

# open_browser()