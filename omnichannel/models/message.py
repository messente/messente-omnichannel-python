# coding: utf-8

"""
    Omnichannel API

    This is the beta version of Omnichannel API  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Message(object):
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
        'channel': 'str'
    }

    attribute_map = {
        'channel': 'channel'
    }

    discriminator_value_class_map = {
        'Viber': 'Viber',
        'SMS': 'SMS'
    }

    def __init__(self, channel=None):  # noqa: E501
        """Message - a model defined in OpenAPI"""  # noqa: E501

        self._channel = None
        self.discriminator = 'channel'

        self.channel = channel

    @property
    def channel(self):
        """Gets the channel of this Message.  # noqa: E501


        :return: The channel of this Message.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this Message.


        :param channel: The channel of this Message.  # noqa: E501
        :type: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
