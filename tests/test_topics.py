import unittest2 as unittest
from pyot.models import OtList

from tests.base import PyOtTestCase


class TopicTestCase(PyOtTestCase):

    def test_topic_list(self):
        topics = self.api.get_topic_list()
        self.assertTrue(isinstance(topics, OtList))

        #assume that we have at least 1 topic in OT,
        #by default there is 3
        self.assertTrue(len(topics) > 0)

    def test_topic_detail(self):
        pass


if __name__ == '__main__':
    unittest.main()