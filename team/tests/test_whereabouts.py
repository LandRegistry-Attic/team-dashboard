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
    assert places['London'] == ['Theodore Ruoff']
    assert places['Holiday'] == ['Robert Roper']

    places = w.places('2014-07-16')
    assert places['Holiday'] == ['Theodore Ruoff', 'Robert Roper']
