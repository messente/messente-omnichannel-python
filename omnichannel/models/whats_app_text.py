# coding: utf-8

"""
    Omnichannel API

    Messente's API which allows sending messages via various channels with fallback options.  # noqa: E501

    OpenAPI spec version: 0.0.2
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class WhatsAppText(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'preview_url': 'bool',
        'body': 'str'
    }

    attribute_map = {
        'preview_url': 'preview_url',
        'body': 'body'
    }

    def __init__(self, preview_url=True, body=None):  # noqa: E501
        """WhatsAppText - a model defined in OpenAPI"""  # noqa: E501

        self._preview_url = None
        self._body = None
        self.discriminator = None

        if preview_url is not None:
            self.preview_url = preview_url
        self.body = body

    @property
    def preview_url(self):
        """Gets the preview_url of this WhatsAppText.  # noqa: E501

        Whether to display link preview if the message contains a hyperlink.  # noqa: E501

        :return: The preview_url of this WhatsAppText.  # noqa: E501
        :rtype: bool
        """
        return self._preview_url

    @preview_url.setter
    def preview_url(self, preview_url):
        """Sets the preview_url of this WhatsAppText.

        Whether to display link preview if the message contains a hyperlink.  # noqa: E501

        :param preview_url: The preview_url of this WhatsAppText.  # noqa: E501
        :type: bool
        """

        self._preview_url = preview_url

    @property
    def body(self):
        """Gets the body of this WhatsAppText.  # noqa: E501

        Plaintext content for WhatsApp, can contains URLs, emojis and formatting  # noqa: E501

        :return: The body of this WhatsAppText.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this WhatsAppText.

        Plaintext content for WhatsApp, can contains URLs, emojis and formatting  # noqa: E501

        :param body: The body of this WhatsAppText.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WhatsAppText):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
