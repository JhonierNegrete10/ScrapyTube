"""
based in https://github.com/michaelkitas/Python-Selenium-Tutorial/tree/master
Example to get cookies 
"""
import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from scraping_utils import read_env_variables 

def iniciar_sesion():
    email, password = read_env_variables()


    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    browser = uc.Chrome(
        options=options,
    )
    
    # url = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    url = "https://accounts.google.com/v3/signin/identifier?dsh=S1896654986%3A1689754282967154&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Des-419%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253FthemeRefresh%253D1&ec=65620&hl=es-419&ifkv=AeDOFXiHFs-RVVcRs_XpItjNOvzJSbv6u1tJxrD5J_rcPZQg7eKW-oVFhDzGLA5rzAdpCQGU5IiT-w&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    browser.get(url)

    browser.find_element(By.ID, 'identifierId').send_keys(email)

    browser.find_element(
        By.CSS_SELECTOR, '#identifierNext > div > button > span').click()

    password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))

    browser.find_element(
        By.CSS_SELECTOR, password_selector).send_keys(password)

    browser.find_element(
        By.CSS_SELECTOR, '#passwordNext > div > button > span').click()

    time.sleep(10)
    return browser

if __name__ == '__main__':
    browser = iniciar_sesion()

    cookies = browser.get_cookies()

    pickle.dump(cookies, open("cookies.pkl", "wb"))
    
 