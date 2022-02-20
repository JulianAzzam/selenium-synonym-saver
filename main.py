import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


word = input()
browser = webdriver.Chrome()
browser.get("https://www.thesaurus.com/")
def input_to_element(xpath, input):
    element = browser.find_element(By.XPATH, xpath)
    element.send_keys(input)
    element.send_keys(Keys.RETURN)
def click_element(xpath):
    element = browser.find_element(By.XPATH, xpath)
    element.click()
input_to_element(xpath="//input[@id='searchbar_input']", input=word)
meanings = browser.find_element(By.XPATH, "//div[@id='meanings']")
words = meanings.find_elements(By.TAG_NAME, "li")
mylist = []
for element in words:
    mylist.append(element.text)
browser.execute_script("window.open('');")
time.sleep(3)
click_element("//a[normalize-space()='English']")
time.sleep(3)
input_to_element("//input[@title='Search']", "English to Arabic")
time.sleep(3)
for word in mylist:
    input_to_element("//textarea[@id='tw-source-text-ta']", word)
