import os
import csv
from person import Person

class Members:
    members = {}

    def add(self, person):
        self.members[person.name] = person

    def parse_tsv(self, string):
        lines = iter(string.splitlines())
        r = csv.DictReader(lines, delimiter='\t')
        for row in r:
            person = Person(row)
            self.add(person)
        return self

    def load(self, filename):
        return self.parse_tsv(open(filename).read())
