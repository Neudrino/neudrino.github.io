
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

LOG_NUMBER_WIDTH = 4


def getCalendarLength(calendar):
    return len(calendar.subcomponents)


def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()


def loadExitingCalendar(icsFilePathFull):
    with open(icsFilePathFull, encoding="utf-8") as f:
        calendarData = Calendar.from_ical(f.read())

    print(f"{getCalendarLength(calendarData):{LOG_NUMBER_WIDTH}} Events existed previously")

    return calendarData


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
    print(f"{len(events):{LOG_NUMBER_WIDTH}} Events to be added")

    return events


def parseTitle(title):
    # element = re.findall(r"^(\d{2}[.]\d{2}[.]\d{4}) (.*) [|-] (.*)", title)
    element = re.findall(r"^(\d{2}[.]\d{2}[.]\d{4})(.*)", title)
    # print("{}".format(element[0][0]))
    print(element)

    return element[0]


def createIcs(oldCalendarItems, newCalendarItems):
    calendar = oldCalendarItems

    for item in newCalendarItems:
        event = Event()
        event.add('dtstart', datetime.strptime(item[0], '%d.%m.%Y').date())
        event.add('summary', item[1])

        calendar.add_component(event)

    print(f"{getCalendarLength(calendar):{LOG_NUMBER_WIDTH}} Events in total")

    return calendar


def writeToDisk(calendar, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(display(calendar))
    # print(display(calendar))


def main(url):
    oldCalendarItems = loadExitingCalendar(icsFilePathFull)
    # print(display(oldCalendarItems))

    xml = loadRss(url)
    newCalendarItems = parseXml(xml)
    calendar = createIcs(oldCalendarItems, newCalendarItems)

    # writeToDisk(calendar, icsFilePathFull)


if __name__ == "__main__":
    main(url)
