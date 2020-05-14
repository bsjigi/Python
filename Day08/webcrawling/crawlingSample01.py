from selenium import webdriver

driver = webdriver.Chrome('../driver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://www.naver.com')
# driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[6]/a').click()
# driver.find_element_by_xpath('//*[@id="scrollbar"]/div[1]/div/div/ul/li[2]/a').click()
# driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[3]/ul/li[1]/dl/dt/a').click()

# driver.find_element_by_id('query').send_keys('파이썬')
# driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()

driver.find_element_by_id('query').send_keys('kgitbank')
driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()
driver.find_element_by_xpath('//*[@id="power_link_body"]/ul/li[1]/div/a').click()