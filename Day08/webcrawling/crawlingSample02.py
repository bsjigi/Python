driver.get('https://www.naver.com')


driver.find_element_by_id('query').send_keys('kg아이티뱅크')
driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()
driver.find_element_by_xpath('//*[@id="main_pack"]/div[1]/div[2]/ul/li[1]/div/a[1]').click()

##탭 바꾸기!
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)
time.sleep(3)
driver.find_element_by_xpath().click()