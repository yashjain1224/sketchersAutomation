from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import configparser


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.skechers.in/")
action = ActionChains(driver);
driver.maximize_window()
time.sleep(2)


def read_config():
    config = configparser.RawConfigParser()
    # config.read(os.path.abspath('config.ini'))
    config.read(os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'config.ini'))

    return config


def intro():
    try:
        print("-->>>", driver.title)
        startMsg = driver.find_element_by_xpath(
            "//*[@id='consent-tracking']/div/div/div[3]/div/button[1]")
        startMsg.click()
        time.sleep(2)
        checkLogin = driver.find_element_by_xpath(
            "//span[normalize-space()='Login / Signup']").text
        if checkLogin == "Login / Signup":
            clickLogin = driver.find_element_by_xpath(
                "//span[normalize-space()='Login / Signup']").click()
            time.sleep(2)
        else:
            driver.quit()
    except Exception as error:
        print("here is the error -->>>>", error)
        driver.quit()


def login():

    try:

        textLogin = driver.find_element_by_xpath(
            "//*[@id='maincontent']/div[2]/div/div[1]/div/div[1]/h5").text
        if textLogin == "LOG IN YOUR SKECHERS ACCOUNT":
            writeEmail = driver.find_element_by_xpath(
                "//*[@id='login-form-email']").send_keys("9549173178")
            writePassword = driver.find_element_by_xpath(
                "//*[@id='login-form-password']").send_keys("8562SonU@")
            clickLogin = driver.find_element_by_xpath(
                "//*[@id='login']/form/div[5]/button").click()
#             time.sleep(2)

    except Exception as error:
        print("here is the error -->>>>", error)
        driver.quit()


def addToCart():
    try:
        hoverDropDownMen = driver.find_element_by_xpath("//*[@id='Men']")
        # clickMen.click()
        action.move_to_element(hoverDropDownMen).perform()
        time.sleep(1)
        clickMen = driver.find_element_by_xpath("//*[@id='MensRunningShoes']")
        clickMen.click()
        checkTextMen = driver.find_element_by_xpath("//*[@id='product-search-results']/div[1]/div[1]/span[1]").text
       
        if checkTextMen == "Running Shoes":
           
            for i in range(1,5):
                if i==1 or i==2:
                    print("")
                else:
                    i+=1

                time.sleep(1)
                clickShoes = driver.find_element_by_xpath(f"(//div[@class='main-image-slider-item pt-3 pt-md-2']){[i]}")
                print(f" {i} time")
                clickShoes.click()
                for j in range(1,7):
                   
                    clickShoeSize = driver.find_element_by_xpath(f'//*[@id="size-1.0"]/button{[j]}')
                    clickShoeSize.click()
                    time.sleep(2)
                    cart = driver.find_element_by_xpath("//*[@id='maincontent']/div[2]/div[3]/div[2]/div[5]/div[11]/div/div/div/div[1]/div/button").text
                  
                    if cart == "ADD TO CART":
                        addInCart = driver.find_element_by_xpath("//*[@id='maincontent']/div[2]/div[3]/div[2]/div[5]/div[11]/div/div/div/div[1]/div/button")
                        addInCart.click()
                        time.sleep(1)
                        clickMenShoes = driver.find_element_by_xpath("//*[@id='maincontent']/div[2]/div[1]/div/div/div/ol/li[3]/a")
                        clickMenShoes.click()
                        break
        
    except Exception as error :
        print("here is the error -->>>>", error)
        driver.quit()

# MAIN FUNCTION
def main():
    try:

        intro()
        login()
#         addToCart()
    except Exception as error :
        print("here is the error -->>>>", error)
        driver.quit()


# CALLING
main()

driver.quit()
