import os
import csv
from person import Person
import urllib2

class Members:
    members = {}

    def add(self, person):
        self.members[person.name] = person

    def parse_tsv(self, string):
        lines = iter(string.splitlines())
        r = csv.DictReader(lines, delimiter='\t')
        for row in r:
            person = Person(row)
            template = os.environ.get('PHOTO_URL_TEMPLATE')
            if template:
                person.photo_url = str.replace(os.environ.get('PHOTO_URL_TEMPLATE'), '%NAME%', person.photo)
            self.add(person)
        return self

    def load(self, resource):
        if (resource.startswith('http')):
            response = urllib2.urlopen(resource)
            tsv = response.read()
            return self.parse_tsv(tsv)
        else:
            return self.parse_tsv(open(resource).read())
