from selenium import webdriver
from time import sleep
num_of_con = int(input("How many connections do you want to add: "))
print("Starting Firefox....")
browser = webdriver.Firefox()
browser.get("https://linkedin.com")
input("Please login with the id you wish to add connections to, then press Enter")
print("Going to Network Page....")
browser.get("https://www.linkedin.com/mynetwork/")
requests_sent = 0
y_scroll = 0
while requests_sent < num_of_con:
    buttons = browser.find_elements_by_tag_name("button")
    connect_buttons = [i for i in buttons if i.text == "Connect"]
    if len(connect_buttons) == 0:
        sleep(1)
        continue
    try:
        for i in range(len(connect_buttons)):
            connect_buttons[i].click()
            requests_sent += 1
            print("\rRequest Sent. Total requests sent: {}".format(requests_sent), end='')
            sleep(1)
            if requests_sent == num_of_con:
                break
    except:
        print("\nCould not find connections in this page, Scrolling....")
        y_scroll += browser.execute_script("return window.scrollY")/2
        browser.execute_script("window.scrollTo(0, {});".format(y_scroll))
        sleep(1)
