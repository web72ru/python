from selenium import webdriver
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)

driver.get('https://www.tyumen-city.ru/sobitii/society/110338/')

driver.save_screenshot("screenshot.png")
driver.quit()