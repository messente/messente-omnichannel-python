# coding: utf-8

"""
    Omnichannel API

    This is the beta version of Omnichannel API  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: admin@messente.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ScenarioItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel': 'str',
        'validity': 'int'
    }

    attribute_map = {
        'channel': 'channel',
        'validity': 'validity'
    }

    def __init__(self, channel=None, validity=None):  # noqa: E501
        """ScenarioItem - a model defined in Swagger"""  # noqa: E501

        self._channel = None
        self._validity = None
        self.discriminator = None

        self.channel = channel
        if validity is not None:
            self.validity = validity

    @property
    def channel(self):
        """Gets the channel of this ScenarioItem.  # noqa: E501

        Defines the delivery channel  # noqa: E501

        :return: The channel of this ScenarioItem.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ScenarioItem.

        Defines the delivery channel  # noqa: E501

        :param channel: The channel of this ScenarioItem.  # noqa: E501
        :type: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501
        allowed_values = ["viber", "sms"]  # noqa: E501
        if channel not in allowed_values:
            raise ValueError(
                "Invalid value for `channel` ({0}), must be one of {1}"  # noqa: E501
                .format(channel, allowed_values)
            )

        self._channel = channel

    @property
    def validity(self):
        """Gets the validity of this ScenarioItem.  # noqa: E501

        After how many minutes this channel is considered as failed and the next channel is attempted  # noqa: E501

        :return: The validity of this ScenarioItem.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this ScenarioItem.

        After how many minutes this channel is considered as failed and the next channel is attempted  # noqa: E501

        :param validity: The validity of this ScenarioItem.  # noqa: E501
        :type: int
        """

        self._validity = validity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, ScenarioItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
