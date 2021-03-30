from selenium import webdriver
import random
import pandas as pd
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)


def run_script(name):
    # Page 1 getting Variable
    driver.get("https://forms.gle/gjXfSvdkudWcqVG2A")
    driver.implicitly_wait(5)

    radio_btn = driver.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")


    driver.implicitly_wait(4)
    name_area = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    name_area.send_keys(name)

    val = random.randint(0, 4)
    # Select Random Age Group.
    radio_btn[val].click()


    # Select Gender
    radio_btn[5].click()

    driver.implicitly_wait(3)

    next_btn = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    next_btn.click()

    driver.implicitly_wait(5)
    radio_btn_1 = driver.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    val = random.randint(0, 1)
    radio_btn_1[val].click()

    val = random.randint(2, 4)
    radio_btn_1[val].click()


    val = random.randint(5, 7)
    radio_btn_1[val].click()

    val = random.randint(8, 12)
    radio_btn_1[val].click()

    val = random.randint(13, 15)
    radio_btn_1[val].click()

    val = random.randint(16, 18)
    radio_btn_1[val].click()

    val = random.randint(19, 21)
    radio_btn_1[val].click()

    val = random.randint(22, 24)
    radio_btn_1[val].click()

    driver.implicitly_wait(4)
    final_submit_btn = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    final_submit_btn.click()

    driver.implicitly_wait(4)
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






