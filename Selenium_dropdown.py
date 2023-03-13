from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from time import sleep
Website = 'https://www.adamchoi.co.uk/overs/detailed'
Path = 'D:\Computational design\chromedriver_win32_new\chromedriver'
Driver = webdriver.Chrome(Path)
Driver.get(Website)
all_matches_button = Driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()
# drop down
dropdown = Select(Driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')
sleep(3)

# scrape table
matches = Driver.find_elements_by_tag_name('tr')
date = []
home_team = []
score = []
away_team = []
for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)  # 1-based array
    home_team.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)

# store data into data frame by a dictionary
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score,'away_team': away_team})
df.to_csv('football_data.csv',index= False)
print(df)
#Driver.quit()