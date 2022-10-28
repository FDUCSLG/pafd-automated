import json
import datetime

def random_sechedule():
    with open('randomizer-status.json', 'r+') as f:
        status = json.load(f)
        today = datetime.date.today()

        if status['last_date'] == today:
            pass
        else:
            pass

if __name__ == '__main__':
    random_sechedule()