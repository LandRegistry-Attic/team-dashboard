import os
import csv
import re
from collections import defaultdict
import urllib2

re_date = re.compile(r'^\d{4}-\d{2}-\d{2}$')

class DayPlace(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = defaultdict(list)
            return value

class Whereabouts:
    def __init__(self):
        self.reset()

    def reset(self):
        self.day_place = DayPlace()

    def add(self, day, name, place):
        if re_date.match(day) and place:
            self.day_place[day][place].append(name)

    def places(self, day):
        return self.day_place[day]

    def parse_tsv(self, string):
        lines = iter(string.splitlines())
        next(lines)
        r = csv.DictReader(lines, delimiter='\t')
        for row in r:
            for key in row:
                self.add(key.strip(), row['name'], row[key])
        return self

    def load(self, resource):
        if (resource.startswith('http')):
            response = urllib2.urlopen(resource)
            tsv = response.read()
            return self.parse_tsv(tsv)
        else:
            return self.parse_tsv(open(resource).read())
