# coding: utf-8

"""
    Omnichannel API

    Messente's API which allows sending messages via various channels with fallback options.  # noqa: E501

    OpenAPI spec version: 0.0.2
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import omnichannel
from omnichannel.api.omnimessage_api import OmnimessageApi  # noqa: E501
from omnichannel.rest import ApiException


class TestOmnimessageApi(unittest.TestCase):
    """OmnimessageApi unit test stubs"""

    def setUp(self):
        self.api = omnichannel.api.omnimessage_api.OmnimessageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_scheduled_message(self):
        """Test case for cancel_scheduled_message

        Cancels a scheduled Omnimessage  # noqa: E501
        """
        pass

    def test_send_omnimessage(self):
        """Test case for send_omnimessage

        Sends an Omnimessage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
