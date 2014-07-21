import pytest
from team.whereabouts import Whereabouts

def test_init_from_args():
    w = Whereabouts()
    w.parse_tsv(
"""	Monday	Tuesday	Wednesday
name	2014-07-14	2014-07-15	2014-07-16
Theodore Ruoff	London	Glasgow	Holiday
Robert Roper	Holiday	Holiday	Holiday
""")

    places = w.places('2014-07-14')
    assert places['london'] == ['Theodore Ruoff']
    assert places['holiday'] == ['Robert Roper']

    places = w.places('2014-07-16')
    assert places['holiday'] == ['Theodore Ruoff', 'Robert Roper']

def test_trim():
    w = Whereabouts()
    w.parse_tsv(
"""	Monday	Tuesday	Wednesday
name	2014-07-14	2014-07-15
Theodore Ruoff	 London	Glasgow
Robert Roper	                     London	      London   
Rouxville Mark Lowe	                           London	      London   
""")

    places = w.places('2014-07-14')
    assert places.keys() == ['london']

    places = w.places('2014-07-15')
    assert sorted(places.keys()) == ['glasgow', 'london']

def test_order():
    w = Whereabouts()
    w.parse_tsv(
"""	Monday	Tuesday	Wednesday
name	2014-07-14
A	England
B	Working from home
C	Zoo
D	Conference
""")

    assert sorted(w.places('2014-07-14').keys()) == ['conference', 'england', 'working from home', 'zoo']
