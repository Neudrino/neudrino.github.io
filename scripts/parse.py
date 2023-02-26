
import re
import requests
import xml.etree.ElementTree as ET
from icalendar import Calendar, Event
from datetime import datetime

url = 'https://www.boogie-baeren.de/share/events-rss-feed.xml'


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
    print(f"{0}".format(element[0][0]))
    print(element)

    return element[0]


def createIcs(calendarItems):
    calendar = Calendar()
    calendar.add('prodid', 'BB-Calendar')
    calendar.add('version', '2.0')

    for item in calendarItems:
        event = Event()
        event.add('dtstart', datetime.strptime(item[0], '%d.%m.%Y').date())
        event.add('summary', item[1])

        calendar.add_component(event)
    return calendar


def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()


def writeToDisk(calendar, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(display(calendar))
    print(display(calendar))


def main(url):
    xml = loadRss(url)
    calendarItems = parseXml(xml)
    calendar = createIcs(calendarItems)
    writeToDisk(calendar, '../calendars/boogie-baeren.ics')


if __name__ == "__main__":
    main(url)
