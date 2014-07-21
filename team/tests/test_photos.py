import os
import pytest
import mock

from team.photos import Photos

@mock.patch('requests.get')
def test_get_photo_with_basic_authetication(mock_get):
    photos = Photos('http://example.com/%PHOTO%.jpg', username='token')
    content, content_type = photos.get('theodore')
    mock_get.assert_called_with('http://example.com/theodore.jpg',
        headers={},
        auth=('token', str('')))

@mock.patch('requests.get')
def test_get_photo_without_basic_authetication(mock_get):
    photos = Photos('https://api.github.com/repos/_organisation_/_repository_/contents/photos/%PHOTO%.jpg')
    content, content_type = photos.get('theodore')
    mock_get.assert_called_with(
        'https://api.github.com/repos/_organisation_/_repository_/contents/photos/theodore.jpg',
        headers={'Accept': 'application/vnd.github.VERSION.raw'},
        auth=None)
    assert content_type == 'image/jpeg'
