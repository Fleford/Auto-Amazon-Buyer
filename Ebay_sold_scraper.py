from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# # Uncomment to use google profile
# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\Fleford\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
# driver = webdriver.Chrome(PATH, options=options)

driver.get("https://www.ebay.com/")

link = driver.find_element_by_link_text("Sign in")
link.click()