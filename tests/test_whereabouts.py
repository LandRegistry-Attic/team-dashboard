import pytest
import mock
from requests import Response
from team.whereabouts import Whereabouts

data = """	Monday	Tuesday	Wednesday
name	2014-07-14	2014-07-15	2014-07-16
Theodore Ruoff	London	Glasgow	Croydon
Robert Roper	Croydon	Croydon	Croydon
"""

data_response = Response
data_response.status = 200
data_response.text = data

def test_init_from_args():
    w = Whereabouts()
    w.parse_tsv(data)

    places = w.places('2014-07-14')
    assert places['London'] == ['Theodore Ruoff']
    assert places['Croydon'] == ['Robert Roper']

    places = w.places('2014-07-16')
    assert places['Croydon'] == ['Theodore Ruoff', 'Robert Roper']

def test_trim():
    w = Whereabouts()
    w.parse_tsv("""
name	2014-07-14	2014-07-15
Theodore Ruoff	 London	Glasgow
Robert Roper	                     London	      London   
Rouxville Mark Lowe	                           London	      London   
""")

    places = w.places('2014-07-14')
    assert places.keys() == ['London']

    places = w.places('2014-07-15')
    assert sorted(places.keys()) == ['Glasgow', 'London']

def test_order():
    w = Whereabouts()
    w.parse_tsv("""
name	2014-07-14
A	England
B	Working from home
C	Zoo
D	Conference
""")

    assert sorted(w.places('2014-07-14').keys()) == ['Conference', 'England', 'Working from home', 'Zoo']

@mock.patch('requests.get', return_value=data_response)
def test_init_from_url(mock_get):
    url = 'http://example.com/file.tsv'
    w = Whereabouts(url)
    assert w.url == url

    mock_get.assert_called_with(url)

    places = w.places('2014-07-14')
    assert places['London'] == ['Theodore Ruoff']

def test_not_working():
    w = Whereabouts()
    w.parse_tsv("""
name	2014-07-14
A	Not working
B	HOLIDAY
C	Holiday
D	Leave
E	AWAY
F	Annual leave
""")

    assert sorted(w.places('2014-07-14').keys()) == ['Not working']

