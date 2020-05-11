from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')

path = '/Users/michaeldargenio/projects/my-apps/py-scraper/chromedriver'
driver = webdriver.Chrome(executable_path = path, chrome_options=options)
print('----------\nAll definitions sourced from "https://www.lexico.com"\n----------\n')

def define(word):
    url = 'https://www.lexico.com/en/definition/' + word
    driver.get(url)
    definition = driver.find_element_by_class_name('ind')
    return definition.text

cont = 'y'
while cont == 'y':
    word = input('----------\nWhat word do you want me to define?: ')
    print(word + ': \n\t' + define(word))
    cont = input('\n\nWould you like to define another word? [y/n]: ')
    if cont == 'n':
        break

driver.quit()