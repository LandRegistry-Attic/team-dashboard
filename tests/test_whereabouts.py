import pytest
import mock
from requests import Response
from team.whereabouts import Whereabouts

data = """	Monday	Tuesday	Wednesday
name	2014-07-14	2014-07-15	2014-07-16
Theodore Ruoff	London	Glasgow	Holiday
Robert Roper	Holiday	Holiday	Holiday
"""

data_response = Response
data_response.status = 200
data_response.text = data

def test_init_from_args():
    w = Whereabouts()
    w.parse_tsv(data)

    places = w.places('2014-07-14')
    assert places['london'] == ['Theodore Ruoff']
    assert places['holiday'] == ['Robert Roper']

    places = w.places('2014-07-16')
    assert places['holiday'] == ['Theodore Ruoff', 'Robert Roper']

def test_trim():
    w = Whereabouts()
    w.parse_tsv("""
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
    w.parse_tsv("""
name	2014-07-14
A	England
B	Working from home
C	Zoo
D	Conference
""")

    assert sorted(w.places('2014-07-14').keys()) == ['conference', 'england', 'working from home', 'zoo']

@mock.patch('requests.get', return_value=data_response)
def test_init_from_url(mock_get):
    url = 'http://example.com/file.tsv'
    w = Whereabouts(url)
    assert w.url == url

    mock_get.assert_called_with(url)

    places = w.places('2014-07-14')
    assert places['london'] == ['Theodore Ruoff']
