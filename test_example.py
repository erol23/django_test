from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://github.com/erol23')

assert browser.page_source.find('erol')