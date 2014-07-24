import os
import csv
import re
from collections import defaultdict
import requests

re_date = re.compile(r'^\d{4}-\d{2}-\d{2}$')
re_holiday = re.compile(r'^(not working|leave|annual leave|away|hoilday)$')

class DayPlace(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = defaultdict(list)
            return value

class Whereabouts:
    day_place = {}

    def __init__(self, url=''):
        self.reset()
        if (url):
            self.url = url
            self.load(url)

    def reset(self):
        self.day_place = DayPlace()

    def add(self, day, name, place):
        if not place:
            return

        if re_holiday.match(place):
            place = "not working"

        if re_date.match(day):
            self.day_place[day][place.lower()].append(name)

    def places(self, day):
        return self.day_place[day]

    def parse_tsv(self, string):
        lines = iter(string.splitlines())
        next(lines)
        r = csv.DictReader(lines, delimiter='\t')
        for row in r:
            for key in row:
                self.add(key.strip(), row['name'], row[key].strip())
        return self

    def load(self, resource=''):
        if not resource:
            resource = self.url

        if (resource.startswith('http')):
            tsv = requests.get(resource)
            return self.parse_tsv(tsv)
        else:
            return self.parse_tsv(open(resource).read())
