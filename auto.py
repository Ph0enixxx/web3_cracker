from selenium import webdriver 
 
# Import chromedriver_autoinstaller to install chromedriver automatically 
import chromedriver_autoinstaller 
 
# Installs chromedriver which corresponds to the main Chrome automatically 
chromedriver_autoinstaller.install() 
 
# Define the proxy server 
PROXY = "IpOfTheProxy:PORT" 
 
# Set ChromeOptions() 
chrome_options = webdriver.ChromeOptions() 
 
# Add the proxy as argument 
# chrome_options.add_argument("--proxy-server=%s" % PROXY) 
chrome = webdriver.Chrome(options=chrome_options) 
 
# Send the request 
chrome.get("https://www.baidu.com")
input()