import requests
import consts

from .exceptions import PyOtConfigException, PyOtResponseError
from .models import Topic, Channel, News


class Api(object):

    API_VERSION = 'v1'
    API_URL = 'https://app.opentopic.com/%(site_slug)s/api/%(api_version)s/'

    def __init__(self, site_slug, username, api_key,
                 response_format=consts.FORMAT_JSON,
                 timeout=consts.TIMEOUT):

        if not (site_slug and username and api_key):
            raise PyOtConfigException(
                'site_slug, username and api_key fields are required')

        self.site_slug = site_slug
        self.username = username
        self.api_key = api_key
        self.response_format = response_format
        self.timeout = timeout
        self.base_url = self.API_URL % {
            'site_slug': self.site_slug,
            'api_version': self.API_VERSION
        }

    def get_api_path(self, path):
        return '%(base)s%(path)s/?username=%(username)s&api_key=%(key)s' % {
            'base': self.base_url,
            'path': path,
            'username': self.username,
            'key': self.api_key
        }

    def get_topic_list(self):
        path = self.get_api_path('topics')
        json = self.request(path)
        return Topic.parse_list(self, json)

    def parse_response(self, response):
        if self.response_format == consts.FORMAT_JSON:
            return response.json()
        else:
            raise PyOtConfigException(
                'Only JSON format is supported in this version')

    def request(self, path):
        response = requests.get(path)
        if response.status_code == 200:
            return self.parse_response(response)
        raise PyOtResponseError('Bad Response: %d' % (response.status_code))