
import os
import re
import requests
import xml.etree.ElementTree as ET
from icalendar import Calendar, Event
from datetime import datetime
from urllib.parse import urlparse

url = 'https://www.boogie-baeren.de/share/events-rss-feed.xml'
scriptDir = os.path.dirname(os.path.abspath(__file__))
icsFileName = urlparse(url).netloc
icsFilePathFull = "{}/../calendars/{}.ics".format(scriptDir, icsFileName)

def loadRss(url):
    response = requests.get(url)
    return response.content


def parseXml(xml):
    rootElement = ET.fromstring(xml)
    events = []
    for item in rootElement.findall('./channel/item'):
        events.append(
            parseTitle(item.find('title').text)
        )

        print(events[-1])
        # print(description)
        # print("------------------------------")
    return events


def parseTitle(title):
    # element = re.findall(r"^(\d{2}[.]\d{2}[.]\d{4}) (.*) [|-] (.*)", title)
    element = re.findall(r"^(\d{2}[.]\d{2}[.]\d{4})(.*)", title)
    # print("{}".format(element[0][0]))
    # print(element)

    return element[0]


def createIcs(calendarItems):
    calendar = Calendar()
    calendar.add('prodid', 'BB-Calendar')
    calendar.add('version', '2.0')

    for item in calendarItems:
        event = Event()
        event.add('dtstart', datetime.strptime(item[0], '%d.%m.%Y').date())
        event.add('sumcreateIcsmary', item[1])

        calendar.add_component(event)
    return calendar


def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()


def writeToDisk(calendar, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(display(calendar))
    # print(display(calendar))


def main(url):
    xml = loadRss(url)
    calendarItems = parseXml(xml)
    calendar = createIcs(calendarItems)
    # print(calendar)
    writeToDisk(calendar, icsFilePathFull)


if __name__ == "__main__":
    main(url)
