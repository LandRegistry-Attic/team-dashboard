#!/usr/bin/env python

import os
import csv
from person import Person

class Members:
    members = {}

    def add(self, person):
        self.members[person.name] = person

    def load(self, filename):
        with open(filename) as f:
            r = csv.DictReader(f, delimiter='\t')
            for row in r:
                member = Person(row)
                self.add(member)
        return self

if __name__ == '__main__':
    members = Members().load("data/team.tsv")
    print members.members
