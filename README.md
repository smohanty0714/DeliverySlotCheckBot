# Delivery Slot Check Python Bot
At COVID-19 pandemic situation online grocessary comes as a saviour,  but, unfortunatly , we do struggle in getting a delivery slot in our trusted online grocery store due to overwhelming orders. Personally, I struggled a lot to get a delivery slot as, delivery slots are limited and also not able to know when the slots are getting open/ available. So, usually I go check over and over on the site whether slots are available or not,  and honstly, its really ridiculous and frustrating activity to do. 

To make my life bit easier I thought, let's employ a Bot to do the same task for me. So, this bot is going to check the delivery slots availability within a configured time interval and will trigger a SMS notification immediately to my given mobile number once it see the available slots. 
## Setup Instructions


### prerequisite
> Python 3 <br>
> Chrome Selenium Driver <br>
> Chrome Application 

### setup steps
1. Install the Python 3 and pip3 - https://realpython.com/installing-python/
2. Download Selenium Firefox Driver based on your OS - https://github.com/mozilla/geckodriver/releases https://chromedriver.chromium.org/getting-started 
3. Install Firefox Application
4. Create a python virtual environment using `python -m venv delivery_slot_venv`
5. Enable the virtual env (for ios - `source /delivery_slot_venv/bin/activate`) 
6. Checkout this code to your system and go the home of this code base, run the requirement.txt file to install all python    dependencies - `pip3 install -r requirements.txt` . else, install the packages listed on the file manually. 
7. Go to the https://www.twilio.com/ and create a free account for the SMS service and update the credentials, your mobile number on `/bot/check/props.py`
8. Post successful installation of packages, navigate to `/bot/check/props.py` and update the credentials required for sms service, login authentication credentials and As well, update the slenium firefox, chrome driver path. 
8. On the `SlotCheckBot.py` update the slot checking time interval in seconds. Currently, its has been set to 5 min(300 seconds) .  <i>Note: don't make it less than 5 mins as destination server can detect it as a Bot and will block your IP/hostname.</i>
9. Go to the https://www.twilio.com/ and create a free account for the SMS service and update the credentials, your mobile number on `WaangooSlotCheck.py` file
10. Now run the Bot - `python3 SlotCheckBot.py` and Bot will check the slot availability and send SMS notification once it sees the available slots.

## If you wish to deploy it into AWS trail EC2, then here is a detail guide that will help :
https://medium.com/@praneeth.jm/running-chromedriver-and-selenium-in-python-on-an-aws-ec2-instance-2fb4ad633bb5
