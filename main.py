from selenium import webdriver
import random
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSedad9CBnZh5NBK1REEFee_sGa-4H7l-_v9qMU4nn2uLisInA/viewform")

wait = WebDriverWait(driver,10)

def run_script(name):
    # Page 1 getting Variable
    driver.implicitly_wait(10)

    radio_btn_1 = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"docssharedWizToggleLabeledLabelWrapper")))

    name_area = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')))
    name_area.send_keys(name)

    email_area = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    email = str(name+'@gmail.com')
    email_area.send_keys(email)

    # Select Gender
    radio_btn_1[0].click()

    driver.implicitly_wait(5)

    val = random.randint(2, 5)
    radio_btn_1[val].click()

    driver.implicitly_wait(5)
    val = random.randint(6, 8)
    radio_btn_1[val].click()

    driver.implicitly_wait(5)
    val = random.randint(9, 11)
    radio_btn_1[val].click()

    driver.implicitly_wait(5)
    val = random.randint(12, 14)
    radio_btn_1[val].click()

    driver.implicitly_wait(5)
    val = random.randint(15, 16)
    radio_btn_1[16].click()

    driver.implicitly_wait(5)
    val = random.randint(17, 18)
    radio_btn_1[val].click()

    driver.implicitly_wait(5)
    val = random.randint(19, 21)
    radio_btn_1[val].click()

    driver.implicitly_wait(5)
    val = random.randint(22, 25)
    radio_btn_1[val].click()

    driver.implicitly_wait(5)
    val = random.randint(26, 27)
    radio_btn_1[val].click()

    driver.implicitly_wait(5)
    val = random.randint(28, 30)
    radio_btn_1[val].click()

    driver.implicitly_wait(4)
    final_submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div > span > span')))
    final_submit_btn.click()

    driver.implicitly_wait(10)
    reGen_Link = driver.find_element_by_partial_link_text("Submit")
    reGen_Link.click()

    driver.implicitly_wait(5)


df = pd.read_csv('Indian-Male-Names.csv')
name_list = df['name'].to_list()
count = 0
for name in name_list:
    if count > 100:
        break
    run_script(name)
    count = count+1






