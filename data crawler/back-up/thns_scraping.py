from bs4 import BeautifulSoup
import urllib.request
# from selenium import webdriver

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

url = 'https://tinhocngoisao.com/collections/laptop-asus'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

links = []

products = soup.find(
	'div', class_='product-listing').find_all('div', class_="itemLoop clearfix")

for product in products:
    a_tag = product.find('a')
    link = 'https://tinhocngoisao.com'+a_tag.get('href')
    # img_src = product.find('img')
    # link = feed.get('href')
    # content = feed.contents[0]
    links.append(link)
    # print('link_href: {}'.format(link.get('href')))
# print(links[0])
i = 1
for link in links:
    print(i)
    i = i + 1
    page2 = urllib.request.urlopen(link)
    soup2 = BeautifulSoup(page2, 'html.parser')
    product_imgs = soup2.find(
	'div', class_='insgalary').find_all('img')
    for img in product_imgs:
        product_img_src = img.get('src')
        print(product_img_src)
    print('---------------------------------------')
    # product_img_src = product_img.get('src')
    