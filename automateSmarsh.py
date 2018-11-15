from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def smarsh():
    # opts = Options().__setattr__('headless', True)
    browser = Chrome(options=opts)
    browser.get('https://app.smarsh.com/ContentUsageAdmin/ManageContentUsage?categoryId=1&channelIds=1')
    try:
        userName = EC.presence_of_element_located((By.ID, 'username'))
        WebDriverWait(browser, 20).until(userName)
    except TimeoutException:
        print('Timed Out!!!')
    userName = browser.find_element_by_id('username')
    userName.send_keys('######')
    password = browser.find_element_by_id('password')
    password.send_keys('######')
    browser.find_element_by_id('loginButton').click()
    browser.find_element_by_name('filterByIdentityPerson').send_keys('Varunaditya Jadwal')
    sleep(5)
    try:
        targetName = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="ContentUsageContext"]/div/div[2]/div[2]/table/tbody/tr/td[1]/label/i')
        )
        WebDriverWait(browser, 20).until(targetName)
    except TimeoutException:
        print('Timed Out!!!')
    browser.find_elements_by_xpath('//*[@id="ContentUsageContext"]/div/div[2]/div[2]/table/tbody/tr/td[1]/label/i')[0].click()
    browser.find_element_by_xpath('//*[@id="ContentUsageContext"]/div/div[2]/div[1]/div[1]/button[1]').click()
    try:
        dropDownMenu = EC.presence_of_element_located((By.NAME, 'archivingStatusId'))
        WebDriverWait(browser, 20).until(dropDownMenu)
    except TimeoutException:
        print('Timed Out!!!')
    dropDownMenu = Select(browser.find_element_by_name('archivingStatusId'))
    dropDownMenu.select_by_value('2')  # 2: Not Archiving
    browser.find_element_by_xpath('//*[@id="editIdentifiersForm"]/div[3]/button[2]').click()
    try:
        confirmButton = EC.presence_of_element_located((By.ID, 'alertify-ok'))
        WebDriverWait(browser, 20).until(confirmButton)
    except TimeoutException:
        print('Timed Out!!!')
    sleep(2)
    try:
        browser.find_element_by_id('alertify-ok').click()
    except selenium.common.exceptions.WebDriverException:
        pass
    browser.close()


if __name__ == '__main__':
    smarsh()
