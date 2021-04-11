
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

#PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\91940\\AppData\\Local\\Google\\Chrome\\User Data\\Default") # change to profile path
chrome_options.add_argument('--profile-directory=Profile 2')
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe", chrome_options=chrome_options)

username = "user"
password = "pass"

#driver.get("https://us.i.mi.com/")

driver.get("https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Fus.i.mi.com%2Fsts%3Fsign%3DQUjUnrCggg9No240fiSu7mm%252BaPw%253D%26followup%3Dhttps%253A%252F%252Fus.i.mi.com%252F%26sid%3Di.mi.com&sid=i.mi.com&_locale=en_US&_snsNone=true")

time.sleep(20)


username_text = driver.find_element_by_name("account")
username_text.send_keys(username)
password_text = driver.find_element_by_name("password")
password_text.send_keys(password)

login_button = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/form/div/button")
login_button.submit()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[3]/a[4]/div[1]/img'))).click()


curr_url = driver.current_url
intend_url = "us.i.mi.com/note"

if intend_url in curr_url:
    intent=True
else:
    intent=False

if intent==False:
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="verify-mod-send_ticket_tip"]/div[2]/button'))).click()
    otp = input("Enter OTP:" )
    otp_text = driver.find_element_by_name("ticket")
    otp_text.send_keys(otp)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="verify-mod-SMS"]/div[3]/a'))).click()
else:
    pass

time.sleep(20)


list_of_notes = []
listdiv = driver.find_elements_by_class_name('note-preview-3vEE2')

for element in listdiv:
    list_of_notes.append(element)

print(list_of_notes)
