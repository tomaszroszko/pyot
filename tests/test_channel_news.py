import unittest2 as unittest

from tests.base import PyOtTestCase


class ChannelNewsTestCase(PyOtTestCase):

    def test_channelnews_for_channel(self):
        channels = self.api.get_channel_list()
        news = channels[-1].get_news()
        self.assertTrue(len(news) > 0)


if __name__ == '__main__':
    unittest.main()