import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_driver(url):
    # Initialize the webdriver (e.g., Chrome, Firefox, etc.)
    driver = webdriver.Chrome()
    # Navigate to the desired webpage
    driver.get(url)
    # Ensure the page is loaded before proceeding 
    time.sleep(1)
    return driver
    #close with driver.quit() after performing tasks

def type_text(target_input, driver):
    active_input_box = driver.switch_to.active_element
    active_input_box.send_keys(target_input)

def select_input_box(target_xpath, driver):
    input_box = driver.find_element("xpath", target_xpath)
    input_box.click()

def press_key(target_key, driver):
    key_mapping = {
        "enter": Keys.ENTER,
        "arrowleft": Keys.ARROW_LEFT,
        "arrowright": Keys.ARROW_RIGHT,
        "arrowup": Keys.ARROW_UP,
        "arrowdown": Keys.ARROW_DOWN,
        "backspace": Keys.BACK_SPACE
    }

    if target_key.lower() in key_mapping:
        active_input_box = driver.switch_to.active_element
        active_input_box.send_keys(key_mapping[target_key.lower()])
    else:
        print("Invalid key:", target_key)

def click_element(target_xpath, driver):
    element = driver.find_element("xpath", target_xpath)
    element.click()

def click_option(target_xpath, driver):
    option_element = driver.find_element("xpath", target_xpath)
    option_element.click()

def move_mouse(target_xpath, driver):
    element = driver.find_element("xpath", target_xpath)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

def select_input_box(target_xpath, driver):
    input_box = driver.find_element("xpath", target_xpath)
    input_box.click()

def navigate_to_url(url, driver):
    driver.get(url)

def scroll_to_element(target_xpath, driver):
    element = driver.find_element("xpath", target_xpath)
    driver.execute_script("arguments[0].scrollIntoView();", element)

def scroll_page(direction, driver):
    scroll_mapping = {
        "up": "-250",
        "down": "250"
    }
    if direction.lower() in scroll_mapping:
        driver.execute_script(f"window.scrollBy(0, {scroll_mapping[direction.lower()]})")
    else:
        print("Invalid scroll direction:", direction)

def switch_to_frame(frame_xpath, driver):
    frame_element = driver.find_element("xpath", frame_xpath)
    driver.switch_to.frame(frame_element)

def switch_to_default_content(driver):
    driver.switch_to.default_content()

def execute_instruction(instruction, driver):
    type_regex = "^type\s.{1,}$"
    press_regex = "^press\s(enter|arrowleft|arrowright|arrowup|arrowdown|backspace)$"
    clickxpath_regex = "^clickxpath\s.{1,}$"
    clickoption_regex = "^clickoption\s.{1,}$"
    movemouse_regex = "^movemouse\s.{1,}$"
    selectinput_regex = "^selectinput\s.{1,}$"
    navigate_regex = "^navigate\s.{1,}$"
    scroll_regex = "^scroll\s(up|down)$"
    scroll_to_element_regex = "^scrolltoelement\s.{1,}$"
    switch_to_frame_regex = "^switchtoframe\s.{1,}$"
    switch_to_default_content_regex = "^switchtodefaultcontent$"

    if re.match(type_regex, instruction):
        target_input = instruction.split(" ")[1]
        type_text(target_input, driver)
    elif re.match(press_regex, instruction):
        target_key = instruction.split(" ")[1]
        press_key(target_key, driver)
    elif re.match(clickxpath_regex, instruction):
        target_xpath = instruction.split(" ", 1)[1]
        click_element(target_xpath, driver)
    elif re.match(clickoption_regex, instruction):
        target_xpath = instruction.split(" ", 1)[1]
        click_option(target_xpath, driver)
    elif re.match(movemouse_regex, instruction):
        target_xpath = instruction.split(" ", 1)[1]
        move_mouse(target_xpath, driver)
    elif re.match(selectinput_regex, instruction):
        target_xpath = instruction.split(" ", 1)[1]
        select_input_box(target_xpath, driver)
    elif re.match(navigate_regex, instruction):
        url = instruction.split(" ", 1)[1]
        navigate_to_url(url, driver)
    elif re.match(scroll_regex, instruction):
        direction = instruction.split(" ")[1]
        scroll_page(direction, driver)
    elif re.match(scroll_to_element_regex, instruction):
        target_xpath = instruction.split(" ", 1)[1]
        scroll_to_element(target_xpath, driver)
    elif re.match(switch_to_frame_regex, instruction):
        frame_xpath = instruction.split(" ", 1)[1]
        switch_to_frame(frame_xpath, driver)
    elif re.match(switch_to_default_content_regex, instruction):
        switch_to_default_content(driver)
    else:
        print("Invalid instruction:", instruction)

# Initialize the driver
driver = initialize_driver("https://www.google.com")

# Wait for the search input box to be visible and clickable
wait = WebDriverWait(driver, 10)
search_input_xpath = "//input[@name='q']"
search_input_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_input_xpath)))

# Select the search input box
select_input_box(search_input_xpath, driver)

# Type the phrase "Al pastor burrito near me"
search_phrase = "Al pastor burrito near me"
type_text(search_phrase, driver)

# Press the "enter" key to submit the search query
press_key("enter", driver)

# Wait for the search results page to load (you can use an explicit wait if necessary)

# Close the webdriver after the test is completed
driver.quit()