import time
import requests

class Photos:
    template_url = None
    auth = None
    cache = {}

    def __init__(self, template_url, username='', password=''):
        self.template_url = template_url
        if username:
            self.auth = (username, password)

    def clear(self):
        self.cache = {}

    def fetch(self, photo):
        headers = {}
        content_type = None

        url = str.replace(self.template_url, '%PHOTO%', photo)

        # GitHub's API is oblivious to the media type
        if url.startswith('https://api.github.com'):
            headers['Accept'] = 'application/vnd.github.VERSION.raw'
            content_type = 'image/jpeg'

        r = requests.get(url, headers=headers, auth=self.auth)

        # TBD: should sniff content, ensure is actually an image
        if content_type:
            r.content_type = content_type

        return r.content, r.content_type

    def get(self, photo):
        if not self.cache.has_key(photo):
             self.cache[photo] = self.fetch(photo)

        return self.cache[photo]
