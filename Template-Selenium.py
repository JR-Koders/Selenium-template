
# webdriver is the most basic thing we need for a selenium project
from selenium import webdriver
# to be able to wait some time
from time import sleep

# Create a new instance of the webdriver, you could also use webdrive.chrome()
driver = webdriver.Firefox()

# Navigate to youtube's website (to our channel)
driver.get("https://youtube.com/@JR-Koders")

# wait for a few seconds
sleep(5)


# Close the browser window
driver.quit()



