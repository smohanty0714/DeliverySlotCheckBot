from selenium import webdriver
from time import sleep
from twilio.rest import Client
from .props import account_sid, auth_token, to_n, from_n, firefox_driver_path
from random import randint
from selenium.webdriver.firefox.options import Options


class WaangooSlotCheck:
    def __init__(self):

        # initiate your selenium webdriver as a headless browser
        # initiate your selenium webdriver as a headless browser
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=firefox_driver_path)

        # Your Account SID from twilio.com/console
        self.account_sid = account_sid
        # Your Auth Token from twilio.com/console
        self.auth_token = auth_token

    # This method will help to check the available delivery slots
    def check(self, sleep_interval):
        try:
            site_address = 'https://www.waangoo.com/'
            self.driver.get(site_address)

            # Giving sleep(secs) after each step of operation makes the destination server consider it as a user
            # operation rather a bot, and it will allow your dom to be loaded properly before you access it.
            sleep(2)
            try:
                self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/button').click()
            except:
                try:
                    self.driver.find_element_by_class_name('ui-dialog-titlebar-close').click()
                except:
                    print('No notification !!')
            sleep(1)
            while True:
                self.slot_check(sleep_interval)

            self.driver.quit()
        except Exception as e:
            print('Error, something went wrong on the checking the slot availability !!')
            self.driver.quit()
            print(e)

    def slot_check(self, sleep_interval):
        slot_check_ele = self.driver.find_element_by_xpath('//*[@id="btnAddNewProduct"]')
        if slot_check_ele:
            slot_check_ele.click()
        sleep(2)
        table = self.driver.find_element_by_id('tbl')
        slotavailable = False
        slottime = ''
        for row in table.find_elements_by_xpath(".//tr"):
            if slotavailable:
                break
            for td in row.find_elements_by_xpath(".//td"):
                if td.get_attribute('class') != 'disable' or td.get_attribute('style') != '':
                    slotavailable = True
                    slottime = td.text
                    break
        # close delivery slot popup
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/button').click()
        if slotavailable:
            msg = 'Delivery slot is available in www.waangoo.com at : %s ' % slottime
            print(msg)
            self.send(msg)
        else:
            print('No, delivery slot is available on www.waangoo.com.')

        # generating random check interval to avoid being detected as bot
        interval = sleep_interval
        if sleep_interval > 60:
            interval = randint(60, sleep_interval)
        print('Sleep interval : %d ' % interval)
        sleep(interval)

    # Send Text Message to the given 'to' number . You can get the credentials by signup in  https://www.twilio.com/ .
    # This site gives 250+ message free on trail account
    def send(self, text):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            to=to_n,
            from_=from_n,
            body=text)

        print('SMS Sent to : %s ' % message.to)
