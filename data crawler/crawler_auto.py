from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import urllib.request
import json

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--headless')


def get_page_source(url):
    driver.get(url)

    time.sleep(6)
    for i in range(0 , 3):
        try:
            element = driver.find_element("xpath", '//*[@class="btn-load__more"]')
            element.click()
            time.sleep(6)
        except:
            print('element not found')

    return driver.page_source

def extract_data(page_source, category_name):
    i = 1 # count variable

    dict_data = {
        "category_name": category_name,
    }

    items = []

    print('data extraction is starting...')
    soup = BeautifulSoup(page_source, 'html.parser')

    links = []
    

    products = soup.find(
        'div', class_='product-listing').find_all('div', class_="itemLoop clearfix")

    for product in products:
        a_tag = product.find('a')
        link = 'https://tinhocngoisao.com'+a_tag.get('href')
        links.append(link)

    # open each of links
    for link in links:
        print(i)
        i = i + 1
        # if i == 68:
        #     break
        page2 = urllib.request.urlopen(link)
        soup2 = BeautifulSoup(page2, 'html.parser')
        # page2.close()
        # name
        product_name = soup2.find('h1', class_="title pdTitle")
        # print(product_name.contents[0])
        # price
        product_price = soup2.find('span', id="pdPriceNumber")
        product_price_str = product_price.contents[0][:-1].replace(',', '')
        # print(product_price.contents[0])
        # images
        img_urls_str = ""
        product_img_urls = soup2.find(
        'div', class_='insgalary').find_all('img')
        for img_url in product_img_urls:
            product_img_url = img_url.get('data-src')
            # print(product_img_url)
            if len(img_urls_str) == 0:
                img_urls_str += product_img_url
            else:
                img_urls_str = img_urls_str + " " + product_img_url
        #  description
        product_description = soup2.find('div', class_="hrvproduct-tabs ch")
        # print(product_description)
        items.append({"product_name": str(product_name.contents[0]), "product_price": str(product_price_str), 
        "product_img_urls": str(img_urls_str), "product_description": str(product_description)})
        print('---------------------------------------')
        
    dict_data["items"] = items

    return dict_data

# products crawl link
page_source = get_page_source('https://tinhocngoisao.com/collections/tan-nhiet-pc')

category_name = "cooler"

dict_data = extract_data(page_source, category_name)



# Writing to data.json
with open("./data/{}.json".format(category_name), "w", encoding='utf8') as outfile:
    # serializing json
    json_data = json.dumps(dict_data, indent=2, ensure_ascii=False)
    try:
        outfile.write(json_data)
    except TypeError:
        print(TypeError)

# remove \n \t from data.json
