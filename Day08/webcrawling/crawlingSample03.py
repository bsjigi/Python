import time

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../driver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://www.naver.com')
driver.find_element_by_id('query').send_keys('오늘날씨')
driver.find_element_by_xpath('//*[@id="search_btn"]').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('p')

for line in data:
    print(line)

print(soup.find('p', class_='cast_txt').txt)

weather = soup.find_all('dd', class_='weather_item _dotWrapper')

for line in weather:
    print(line)
#
# for select in range(1,5):
#     driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[2]/ul/li[{}]/a/span'.format(select)).click()
#     time.sleep(5)

