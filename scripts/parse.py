
import os
import requests
import xml.etree.ElementTree as ET
from ics import Calendar, Event
from datetime import datetime
from urllib.parse import urlparse

import pyparsing as pp

url = 'https://www.boogie-baeren.de/share/events-rss-feed.xml'
scriptDir = os.path.dirname(os.path.abspath(__file__))
icsFileName = urlparse(url).netloc
icsFilePathFull = "{}/../calendars/{}.ics".format(scriptDir, icsFileName)

LOG_NUMBER_WIDTH = 4
VERBOSE = os.getenv('VERBOSE') or False


def loadExitingCalendar(icsFilePathFull):
    if not os.path.exists(icsFilePathFull):
        with open(icsFilePathFull, "x"):
            print(f"Created {icsFilePathFull}")

    with open(icsFilePathFull, 'r', encoding="utf-8") as f:
        try:
            calendarData = Calendar(f.read())
        except:
            calendarData = Calendar()

    print(f"{len(calendarData.events):{LOG_NUMBER_WIDTH}} Events existed previously")

    return calendarData


def getFromUrl(url):
    response = requests.get(url)
    return response.content


def parseXml(url):
    xml = getFromUrl(url)

    rootElement = ET.fromstring(xml)
    events = []

    for item in rootElement.findall('./channel/item'):
        events.append(
            {
                "title": parseTitle(item.find('title').text),
                "description": item.find('description').text,
                "uid": item.find('guid').text,
                "url": item.find('link').text,
            }
        )

    print(f"{len(events):{LOG_NUMBER_WIDTH}} Events to be added")

    return events


def parseTitle(title):
    """
    title = '10.03.2023 Hot Friday #25 | Altmünchner Gesellenhaus'
    """

    colon = pp.Suppress(':')
    dot = pp.Suppress('.')
    dash = pp.oneOf('- –')
    bracket = pp.Suppress(pp.oneOf('( )'))

    date = pp.Word(pp.nums, exact=2) + dot + pp.Word(pp.nums, exact=2) + dot + pp.Word(pp.nums, exact=4)
    startDate = date('startDate')
    dateRange = date('startDate') + dash + date('endDate')

    time = pp.Word(pp.nums, exact=2) + colon + pp.Word(pp.nums, exact=2)
    timeRange = time('startTime') + dash + time('endTime')
    timeAddition = bracket + timeRange + bracket

    text = pp.OneOrMore(pp.Word(pp.identbodychars + pp.printables))

    titleGrammar = (dateRange | startDate)('date') + \
        pp.Opt(timeAddition)('time') + text('summary')

    result = pp.ParseResults(titleGrammar.parse_string(title))

    # print(f"{result}")

    return result


def createIcs(oldCalendarItems, newCalendarItems):
    calendar = oldCalendarItems

    for item in newCalendarItems:
        titleDescription = item['title']
        description = item['description']
        uid = item['uid']#[40:]
        url = item['url']

        if uid in calendar.serialize():
            VERBOSE and print(f"{' ': >{LOG_NUMBER_WIDTH+1}}Item exists: {uid}")
            continue

        event = Event()

        if titleDescription.startTime:
            startTime = f"T{':'.join(titleDescription.startTime)}"
            startDate = '.'.join(titleDescription.startDate)
            event.begin = datetime.strptime(
                startDate + startTime, '%d.%m.%YT%H:%M').astimezone()
        else:
            event.begin = datetime.strptime(
                '.'.join(titleDescription.startDate), '%d.%m.%Y').date()
            event.make_all_day()

        endDate = '.'.join(
            titleDescription.endDate or titleDescription.startDate)
        if titleDescription.endTime:
            endTime = f"T{':'.join(titleDescription.endTime)}"
            event.end = datetime.strptime(
                endDate + endTime, '%d.%m.%YT%H:%M').astimezone()
        else:
            event.end = datetime.strptime(endDate, '%d.%m.%Y').date()

        event.name = ' '.join(titleDescription.summary)

        event.uid = uid
        event.url = url

        calendar.events.add(event)
        VERBOSE and print(f"{' ': >{LOG_NUMBER_WIDTH+1}}Item added:  {uid}")

    print(f"{len(calendar.events):{LOG_NUMBER_WIDTH}} Events in total")

    return calendar


def writeToDisk(calendar, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(calendar.serialize())


def main(url):
    oldCalendarItems = loadExitingCalendar(icsFilePathFull)
    newCalendarItems = parseXml(url)
    calendar = createIcs(oldCalendarItems, newCalendarItems)

    writeToDisk(calendar, icsFilePathFull)


if __name__ == "__main__":
    main(url)
