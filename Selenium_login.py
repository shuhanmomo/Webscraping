from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import wget
import getpass

website = 'https://beta.flim.ai/?mt=MOVIES'
path = 'D:\Computational design\chromedriver_win32_new\chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)
sleep(3)

# store log-in information
my_user = 'moumou014725@gmail.com'
my_pwd = ''# put password here
dest_loc = 'D:\Computational design\web_scraped_img'
# fill in login name
login_button = driver.find_element(By.XPATH,'//a[@data-cy="login-modal"]')
login_button.click()
user_name = driver.find_element(By.XPATH,'//input[@name="email"]')
user_name.send_keys(my_user)
user_name.send_keys(Keys.ENTER)
# fill in login password
user_pwd = driver.find_element(By.XPATH,'//input[@name="password"]')
user_pwd.send_keys(my_pwd)
user_pwd.send_keys(Keys.ENTER)
sleep(3)
# remove banner
accept_button = driver.find_element_by_xpath('//button[@data-tid="banner-accept"]')
accept_button.click()
# input search box
search_box = driver.find_element_by_xpath('//input[@id="input-search"]')
search_cont = ['romantic','sadness','calm']
search_box.send_keys("happy and excited moment")
search_box.send_keys(Keys.ENTER)
sleep(3)
# scroll down to the botton
times = 5
for _ in range(times):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)

# find image

try:
    images = driver.find_elements_by_xpath('//img[@alt="preview image"]')
    image_names = driver.find_elements_by_xpath('//a[contains(@class,"movieTitle")]')
    my_images = {}
    for i in range(len(images)):
        source = images[i].get_attribute('src')
        image_name = f"{image_names[i].text}.jpg"
        my_images[image_name] = source

    for name, link in my_images.items():
        try:
            wget.download(link, out=name)
        except:
            pass

except:
    pass



