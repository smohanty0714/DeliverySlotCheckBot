from selenium import webdriver
from time import sleep
from twilio.rest import Client
from .props import account_sid, auth_token, to_n, from_n, firefox_driver_path
from .props import email, secrets
from random import randint
from selenium.webdriver.firefox.options import Options


class RedMartSlotCheck:
    def __init__(self):
        # initiate your selenium webdriver as a headless browser
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=firefox_driver_path)

        # Your Account SID from twilio.com/console
        self.account_sid = account_sid
        # Your Auth Token from twilio.com/console
        self.auth_token = auth_token

    # This method will help to check the available delivery slots
    def check(self, check_interval):
        try:
            site_address = 'https://redmart.lazada.sg/'
            self.driver.get(site_address)

            # Giving sleep(secs) after each step of operation makes the destination server consider it as a user
            # operation rather a bot, and it will allow your dom to be loaded properly before you access it.
            sleep(2)

            login_btn = self.driver.find_element_by_xpath('//*[@id="anonLogin"]/a')
            if login_btn:
                login_btn.click()

            sleep(2)

            for s in email:
                self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/form/div/div[1]/div[1]/input') \
                    .send_keys(s)
            sleep(1)

            for s in secrets:
                self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/form/div/div[1]/div[2]/input') \
                    .send_keys(s)
            sleep(1)

            self.driver.find_element_by_class_name('next-btn').click()
            sleep(5)

            cart_value = self.driver.find_element_by_id('topActionCartNumber').text

            if cart_value is None or cart_value == '' or int(cart_value) <= 0:
                self.driver.find_element_by_class_name('AtcButtonWithoutQtyWithStock').click()
                sleep(1)

            self.driver.find_element_by_class_name('lzd-nav-cart').click()

            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="shop-title-wrap"]/div[1]/div/label/input').click()
            sleep(1)
            self.driver.find_element_by_class_name('checkout-order-total-button').click()
            sleep(1)
            try:
                self.driver.find_element_by_xpath('//*[@id="dialog-body-1"]/button').click()
            except:
                print('no popup info')
            sleep(1)

            while True:
                self.slot_check(check_interval)

            self.driver.quit()
        except Exception as e:
            print('Error, something went wrong on the checking the slot availability in redmart !!')
            self.driver.quit()
            print(e)

    def slot_check(self, check_interval):
        slot_btn_div = self.driver.find_element_by_class_name('deliveryTimeRight')
        slot_btn_div.find_element_by_css_selector('button').click()
        sleep(3)
        slot_divs = self.driver.find_elements_by_class_name('slot-item-container')
        msg = 'No, Slot available in https://redmart.lazada.sg/'
        for slot in slot_divs:
            class_name = slot.get_attribute('class')
            if class_name == 'slot-item-container':
                slot_time = slot.text
                msg = 'Delivery slot is available in https://redmart.lazada.sg/ at : %s ' % slot_time
                self.send(msg)
                break
        print(msg)
        sleep(1)
        popup = self.driver.find_element_by_class_name('rm-slots-page-modal-header-close')
        popup.find_elements_by_tag_name('img')[0].click()
        sleep(1)
        # generating random check interval to avoid being detected as bot
        interval = randint(60, check_interval) if check_interval > 60 else check_interval
        print('time interval: %d' % interval)
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
