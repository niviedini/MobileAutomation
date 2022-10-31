import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())


if __name__ == '__main__':
    driver.get("https://www.redfin.com/WA/Seattle/9255-Greenwood-Ave-N-98103/unit-38/home/26357")
    time.sleep(3)
    photos = driver.find_element(by=By.XPATH, value='//*[@id="photoPreviewButton"]/div')
    photos.click()
    time.sleep(10)
    driver.quit()
