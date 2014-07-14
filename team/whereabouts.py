#!/usr/bin/env python

import os
import csv
import re
from collections import defaultdict

re_date = re.compile(r'^\d{4}-\d{2}-\d{2}$')

class DayPlace(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = defaultdict(list)
            return value

class Whereabouts:
    day_place = DayPlace()

    def add(self, day, name, place):
        if re_date.match(day) and place:
            self.day_place[day][place].append(name)

    def places(self, day):
        return self.day_place[day]

    def load(self, filename):
        self.by_day = {}
        with open(filename) as f:
            next(f)
            r = csv.DictReader(f, delimiter='\t')
            for row in r:
                for key in row:
                    self.add(key.strip(), row['name'], row[key])
        return self

if __name__ == '__main__':
    filename = "data/whereabouts.tsv"
    whereabouts = Whereabouts().load(filename)
    days = whereabouts.day_place
    for day in sorted(days):
        print day, whereabouts.places(day)
