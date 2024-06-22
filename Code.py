# you would need a webdriver installed into a separate folder and selenium package to your  editor
import time
import keyboard
from selenium import webdriver



def impartus_attender():
    # impartus auto login programme

    username = "  "
    password = "  "

    driver = webdriver.Chrome(executable_path=r"C:\Users\Asus\Downloads\chromedriver_win32 (1)\chromedriver.exe") # install and keep in downloads then copy path here
    driver.maximize_window()
    driver.get("https://a.impartus.com/login/#/") # feeding the link

    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_xpath("/html/body/ui-view/div/div/ui-view/div/div[1]/form/div[2]/div").click()

    print('SUCESSFULLY LOGGED IN !')


    time.sleep(5)  # increase or decrease this depending on your internet speed 
    # the subject join button . find and click
    join_button = driver.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[3]/dashboard-interests/div/live-streaming-lectures/md-card/md-list/div[1]/div[1]/div[2]/button')

    if join_button.is_enabled() is True:
        join_button.click()

        print('FOUND AND ENTERED A LIVE CLASSROOM !')

        time.sleep(3)
        keyboard.press_and_release('ctrl+TAB')
        driver.close()

        driver.find_element_by_class_name('md-button md-primary md-raised md-button md-ink-ripple').click()

        print('Sucessfully attending a live class now !')

    else:
        print("NO ONLINE CLASSES FOUND !"
              "no classes for this hour !")
        driver.quit()


if 1 == 1:
    print(impartus_attender())
