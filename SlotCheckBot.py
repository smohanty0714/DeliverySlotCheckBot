import sys
from bot.check.WaangooSlotCheck import WaangooSlotCheck
from bot.check.RedMartSlotCheck import RedMartSlotCheck


def main(argv):
    bot_iterate_interval = int(argv[1]) if int(argv[1]) else 300

    if argv[0] == 'waangoo':
        WaangooSlotCheck().check(bot_iterate_interval)
    elif argv[0] == 'redmart':
        RedMartSlotCheck().check(bot_iterate_interval)
    else:
        print('Wrong Usages, Please refer this format'
              ' : python3 SlotCheckBot.py <site_name - waangoo / redmart> <time_interval>')
        sys.exit(2)


""" 
Pass the site name and time interval in seconds (300 secs/ 5 minutes) at which you are checking the slot availability,

python3 SlotCheckBot.py <site_name - eg. waangoo / redmart> <time_interval - eg. 300>

Note:Giving less time interval will lead your ip or host to get blocked by the destination server as it can detect
its a Bot operation. 
"""
if __name__ == '__main__':
    main(sys.argv[1:])
