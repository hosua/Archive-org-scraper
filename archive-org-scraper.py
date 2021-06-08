from selenium import webdriver
from selenium.webdriver.common.by import By
import os

print("\nArchive-org-scraper v0.1\n")
print(	 "  __  __           _        _             _   _                               \n"
	" |  \\/  | __ _  __| | ___  | |__  _   _  | | | | ___  _____      _____   ___  \n"
	" | |\\/| |/ _` |/ _` |/ _ \\ | '_ \\| | | | | |_| |/ _ \\/ __\\ \\ /\\ / / _ \\ / _ \\ \n"
	" | |  | | (_| | (_| |  __/ | |_) | |_| | |  _  | (_) \\__ \\\\ V  V / (_) | (_) |\n"
	" |_|  |_|\\__,_|\\__,_|\\___| |_.__/ \\__, | |_| |_|\\___/|___/ \\_/\\_/ \\___/ \\___/ \n"
	"                                  |___/                                       \n\n")
user_browser = input("What browser are you using? (Chrome/Firefox/Opera)").lower()
if user_browser == "chrome":
    driver = webdriver.Chrome()
if user_browser == "firefox":  
    driver = webdriver.Firefox()
if user_browser == "opera":
    driver = webdriver.Opera()
user_in = input("Enter a link to scrape:\n")
driver.get(user_in)
links = driver.find_elements_by_xpath("//a[@href]")

outFile = "links.txt"
keepStr = input("\n\nEnter the region you want to grab. (Case sensitive)\n" +
"Note: This will check the URL text, not the actual URL)\n\n")

keepMisc = input("Do you want to grab extras? (betas/demos/prototypes) (y/n)").lower()
getExtras = None
if (keepMisc == "y"):
    getExtras = True
if (keepMisc == "n"):
    getExtras = False


demo = "%28Demo"    # Parenthesis in URL's are denoted with %28 as '(' and %29 as ')'
beta = "%28Beta"
proto = "%28Proto"

f = open(outFile, "w+")

for link in links:
    if not getExtras:  # if not keeping betas/demos/protos
        if keepStr in link.text:    # if we found the substring
            if demo not in link.get_attribute("href"):   # ignore extras
                if beta not in link.get_attribute("href"):
                    if proto not in link.get_attribute("href"):
                        f.write(link.get_attribute("href") + "\n")
                        print(link.get_attribute("href"))
    if getExtras:
        if keepStr in link.text:    # if we found the substring
            f.write(link.get_attribute("href") + "\n")
            print(link.get_attribute("href"))



print("\n\nScraping process finished.\n")
print("Links were saved to " + os.path.join(os.getcwd(), outFile))