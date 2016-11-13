import requests
import threading
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient


def send_sms():
    client = TwilioRestClient("ACee782f2e314a70151536680e5484c403", "fc4299125919e8ce0009bc06b8ef242d")
    client.messages.create(to="+19497716120", from_="+12548486298",
                       body="Spring 2017 - The American Serial Killer is NOW AVAILABLE")
    client.messages.create(to="+18572538606", from_="+12548486298",
                       body="Spring 2017 - The American Serial Killer is NOW AVAILABLE")


def get_class():
    t = threading.Timer(10.0, get_class)
    t.start()
    res = requests.get(
        'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1478939644?ModuleName=class_topic/_start.pl&PlannerISN=0000020789&KeySem=20174&ViewSem=Spring%202017&BldgCd=&ClassCd=CASWR150%20O9&TopicCd=633079&LastActivityTime=1478939644')
    soup = BeautifulSoup(res.text)
    # print(soup.find_all(attrs={"valign": "top"}))
    lst = soup.find_all(attrs={"valign": "top"})
    result = []
    for father in lst:
        for child in father:
            try:
                result.append(child.get_text().split())
            except AttributeError:
                continue
    print(result)

    if result[5] != ['0'] or result[6] != ['Class', 'Full']:
        send_sms()
        t.cancel()

    result = []



client = TwilioRestClient("ACee782f2e314a70151536680e5484c403", "fc4299125919e8ce0009bc06b8ef242d")
client.messages.create(to="+19497716120", from_="+12548486298",
                       body="Start tracking <Spring 2017 - The American Serial Killer>")
client.messages.create(to="+18572538606", from_="+12548486298",
                       body="Start tracking <Spring 2017 - The American Serial Killer>")
get_class()
