from selenium import webdriver
import random
import pandas as pd
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)


def run_script(name):
    driver.get("https://forms.gle/gjXfSvdkudWcqVG2A")
    # Page 1 getting Variable
    driver.implicitly_wait(5)
    radio_btn = driver.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    name_area = driver.find_element_by_class_name("quantumWizTextinputPaperinputInput")
    next_btn = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

    val = random.randint(0, 4)
    driver.implicitly_wait(2)
    name_area.send_keys(name)

    # Select Random Age Group.
    radio_btn[val].click()


    # Select Gender
    radio_btn[5].click()


    driver.implicitly_wait(3)
    next_btn.click()
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

    final_submit_btn = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    final_submit_btn.click()

    driver.implicitly_wait(3)
    reGen_Link = driver.find_element_by_partial_link_text("Submit")
    reGen_Link.click()

    driver.implicitly_wait(5)


df = pd.read_csv('Indian-Male-Names.csv')
name_list = df['name'].to_list()
count = 0
for name in name_list:
    if count > 100:
        break
    run_script(str(name))
    count = count+1






