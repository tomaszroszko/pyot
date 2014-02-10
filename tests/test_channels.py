import unittest2 as unittest
from pyot.models import OtList

from tests.base import PyOtTestCase


class ChannelTestCase(PyOtTestCase):

    def test_channel_list(self):
        channels = self.api.get_channel_list()
        self.assertTrue(isinstance(channels, OtList))
        self.assertTrue(len(channels) > 0)

    def test_topic_detail(self):
        channels = self.api.get_channel_list()
        channel = self.api.get_channel_detail(channels[0].id)
        self.assertEqual(channel.id, channels[0].id)
        self.assertEqual(channel.name, channels[0].name)


if __name__ == '__main__':
    unittest.main()