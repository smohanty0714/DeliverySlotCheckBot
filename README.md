# Delivery Slot Check Python Bot
In current COVID-19 pandemic situation, online grocery comes as a saviour,  but, unfortunately , we do struggle in getting a delivery slot in our trusted online grocery store due to overwhelming orders. Personally, I struggled a lot to get a delivery slot as, delivery slots are limited and also not able to know when the slots are getting open/ available. So, usually I go check over and over on the site whether slots are available or not,  and honestly, its really ridiculous and frustrating activity to do. 

To make my life bit easier I thought, let's employ a Bot to do the same task for me. So, this bot is going to check the delivery slots availability within a configured time interval and will trigger a SMS notification immediately to my given mobile number once it see the available slots. 

This implementation has been done for below two popular online grocery sites based in Singapore and you can extend this code to create a bot of your favourite online shopping site:

> https://redmart.lazada.sg/ <br>
> https://www.waangoo.com/

<i>Note :  Excuse on some coding standards as created with limited time</i>

## Setup Instructions


### prerequisite
> Python 3 <br>
> Firfox Selenium Driver <br>
> Firfox Application 

### setup steps
1. Install the Python 3 and pip3 - https://realpython.com/installing-python/
2. Download Selenium Firefox Driver based on your OS - https://github.com/mozilla/geckodriver/releases 
3. Install Firefox Application
4. Create a python virtual environment using `python -m venv delivery_slot_venv`
5. Enable the virtual env (for ios/linux - `source /delivery_slot_venv/bin/activate` and for windows `\delivery_slot_venv\Scripts\activate.bat`) 
6. Checkout this code to your system and go the home of this code base, run the requirement.txt file to install all python    dependencies - `pip3 install -r requirements.txt` . else, install the packages listed on the file manually. 
7. Go to the https://www.twilio.com/ and create a free account for the SMS service and update the credentials, your mobile number on `/bot/check/props.py`
8. Post successful installation of packages, navigate to `/bot/check/props.py` and update the credentials required for sms service, login authentication credentials (if you are using redmart then its required , your lazada credentials) and As well, update the slenium firefox driver path. 
9.Now run the Bot - `python3 SlotCheckBot.py <site_name - eg. waangoo / redmart> <time_interval - eg. 300>` and Bot will check the slot availability randomly based on given time interval and send SMS notification once it sees the available slots.<i>Note: don't make `time_interval` less than 5 mins as destination server can detect it as a Bot and will block your IP/hostname.</i>

## If you wish to deploy it into AWS trail EC2, then here is a detail guide that will help :
https://medium.com/@praneeth.jm/running-chromedriver-and-selenium-in-python-on-an-aws-ec2-instance-2fb4ad633bb5
