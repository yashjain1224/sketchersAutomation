from selenium import webdriver
import time, os ,configparser

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.skechers.in/")
driver.maximize_window()
time.sleep(2)

def read_config():
    config = configparser.RawConfigParser()
    # config.read(os.path.abspath('config.ini'))
    config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.ini'))
    
    return config

def intro():

    try:
        print("-->>>",driver.title)
        startMsg = driver.find_element_by_xpath("//*[@id='consent-tracking']/div/div/div[3]/div/button[1]")
        startMsg.click()
        time.sleep(2)
        checkLogin = driver.find_element_by_xpath("//span[normalize-space()='Login / Signup']").text
        if checkLogin == "Login / Signup":
            clickLogin = driver.find_element_by_xpath("//span[normalize-space()='Login / Signup']").click()
            time.sleep(2)
        else:
            driver.quit()
    except Exception as error :
        print("here is the error -->>>>", error)
        driver.quit()

def login():
    try:
        # config = read_config()
        # print("-->>", config["Login"])
        textLogin = driver.find_element_by_xpath("//*[@id='maincontent']/div[2]/div/div[1]/div/div[1]/h5").text
        if textLogin == "LOG IN YOUR SKECHERS ACCOUNT" :
            writeEmail = driver.find_element_by_xpath("//*[@id='login-form-email']").send_keys("9549173178")
            writePassword = driver.find_element_by_xpath("//*[@id='login-form-password']").send_keys("8562SonU@")
            clickLogin = driver.find_element_by_xpath("//*[@id='login']/form/div[5]/button").click()
            time.sleep(2)

    except Exception as error :
        print("here is the error -->>>>", error)
        driver.quit()


# MAIN FUNCTION
def main():
    try:
        intro()
        login()
    except Exception as error :
        print("here is the error -->>>>", error)
        driver.quit()


# CALLING

main()

driver.quit()
