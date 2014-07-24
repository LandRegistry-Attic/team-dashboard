import pytest
import mock

from team.server import app

def is_html(r):
    assert r.status_code == 200
    assert r.headers['Content-type'] == 'text/html; charset=utf-8'


def test_get_home():
    client = app.test_client()
    r = client.get('/')
    is_html(r)

def test_get_cards():
    client = app.test_client()
    r = client.get('/cards')
    is_html(r)
    assert '<div class="page">' in r.data

def test_get_whereabouts_date():
    client = app.test_client()
    r = client.get('/whereabouts/2014-07-17')
    is_html(r)
    assert '<h1>Team whereabouts for 2014-07-17' in r.data

def test_get_whereabouts_today():
    client = app.test_client()
    r = client.get('/whereabouts')
    is_html(r)
    assert '<h1>Team whereabouts for 20' in r.data

@mock.patch('team.server.photos.get', return_value=("IMAGE", "image/jpeg"))
def test_get_photos(mock_get):
    client = app.test_client()
    r = client.get('/photo/nickname')
    mock_get.assert_called_with('nickname')
    assert r.data == "IMAGE"
    assert r.content_type == "image/jpeg"
