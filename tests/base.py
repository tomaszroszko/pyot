import os
from unittest2 import TestCase

from pyot import Api


ot_site_slug = os.environ.get('OT_SITE_SLUG', None)
ot_username = os.environ.get('OT_USERNAME', None)
ot_api_key = os.environ.get('OT_API_KEY', None)


class PyOtTestCase(TestCase):

    def setUp(self):
        self.api = Api(ot_site_slug, ot_username, ot_api_key)
