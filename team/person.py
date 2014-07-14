#!/usr/bin/env python

import os
import csv

# what started as a dictionary, has become a dictionary :(
class Person(object):
    name = ""
    photo = ""
    slack = ""
    twitter = ""
    github = ""

    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
        return ', '.join(sb)

    def __repr__(self):
        return self.__str__()

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
