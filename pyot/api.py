import consts


class Api(object):

    def __init__(self, site_slug, username, api_key,
                 response_format=consts.FORMAT_JSON,
                 timeout=consts.TIMEOUT):

        self.site_slug = site_slug
        self.username = username
        self.api_key = api_key
        self.response_format = response_format
        self.timeout = timeout

    def request(self, path):
        pass