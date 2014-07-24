import pytest
from team.person import Person

def test_init_from_args():
    person = Person(name="Theodore Burton Fox Ruoff", github="nobody")
    assert person.name == "Theodore Burton Fox Ruoff"
    assert person.github == "nobody"

def test_init_from_dict():
    d = { "name": "Theodore Burton Fox Ruoff", "github": "nobody" }
    person = Person(d)
    assert person.name == "Theodore Burton Fox Ruoff"
    assert person.github == "nobody"
