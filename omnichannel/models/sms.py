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


class SMS(object):
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
        'sender': 'str',
        'validity': 'int',
        'text': 'str',
        'autoconvert': 'str',
        'udh': 'str',
        'channel': 'str'
    }

    attribute_map = {
        'sender': 'sender',
        'validity': 'validity',
        'text': 'text',
        'autoconvert': 'autoconvert',
        'udh': 'udh',
        'channel': 'channel'
    }

    def __init__(self, sender=None, validity=None, text=None, autoconvert=None, udh=None, channel='sms'):  # noqa: E501
        """SMS - a model defined in OpenAPI"""  # noqa: E501

        self._sender = None
        self._validity = None
        self._text = None
        self._autoconvert = None
        self._udh = None
        self._channel = None
        self.discriminator = None

        if sender is not None:
            self.sender = sender
        if validity is not None:
            self.validity = validity
        self.text = text
        if autoconvert is not None:
            self.autoconvert = autoconvert
        if udh is not None:
            self.udh = udh
        if channel is not None:
            self.channel = channel

    @property
    def sender(self):
        """Gets the sender of this SMS.  # noqa: E501

        Phone number or alphanumeric sender name  # noqa: E501

        :return: The sender of this SMS.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SMS.

        Phone number or alphanumeric sender name  # noqa: E501

        :param sender: The sender of this SMS.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def validity(self):
        """Gets the validity of this SMS.  # noqa: E501

        After how many minutes this channel is considered as failed and the next channel is attempted  # noqa: E501

        :return: The validity of this SMS.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this SMS.

        After how many minutes this channel is considered as failed and the next channel is attempted  # noqa: E501

        :param validity: The validity of this SMS.  # noqa: E501
        :type: int
        """

        self._validity = validity

    @property
    def text(self):
        """Gets the text of this SMS.  # noqa: E501

        Text content of the SMS  # noqa: E501

        :return: The text of this SMS.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SMS.

        Text content of the SMS  # noqa: E501

        :param text: The text of this SMS.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def autoconvert(self):
        """Gets the autoconvert of this SMS.  # noqa: E501

        Defines how non-GSM characters will be treated: - \"on\" Use replacement settings from the account's [API Auto Replace settings page](https://dashboard.messente.com/api-settings/auto-replace)(default) - \"full\" All non GSM 03.38 characters will be replaced with suitable alternatives - \"off\" Message content is not modified in any way   # noqa: E501

        :return: The autoconvert of this SMS.  # noqa: E501
        :rtype: str
        """
        return self._autoconvert

    @autoconvert.setter
    def autoconvert(self, autoconvert):
        """Sets the autoconvert of this SMS.

        Defines how non-GSM characters will be treated: - \"on\" Use replacement settings from the account's [API Auto Replace settings page](https://dashboard.messente.com/api-settings/auto-replace)(default) - \"full\" All non GSM 03.38 characters will be replaced with suitable alternatives - \"off\" Message content is not modified in any way   # noqa: E501

        :param autoconvert: The autoconvert of this SMS.  # noqa: E501
        :type: str
        """
        allowed_values = ["full", "on", "off"]  # noqa: E501
        if autoconvert not in allowed_values:
            raise ValueError(
                "Invalid value for `autoconvert` ({0}), must be one of {1}"  # noqa: E501
                .format(autoconvert, allowed_values)
            )

        self._autoconvert = autoconvert

    @property
    def udh(self):
        """Gets the udh of this SMS.  # noqa: E501

        hex-encoded string containing SMS UDH  # noqa: E501

        :return: The udh of this SMS.  # noqa: E501
        :rtype: str
        """
        return self._udh

    @udh.setter
    def udh(self, udh):
        """Sets the udh of this SMS.

        hex-encoded string containing SMS UDH  # noqa: E501

        :param udh: The udh of this SMS.  # noqa: E501
        :type: str
        """

        self._udh = udh

    @property
    def channel(self):
        """Gets the channel of this SMS.  # noqa: E501


        :return: The channel of this SMS.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this SMS.


        :param channel: The channel of this SMS.  # noqa: E501
        :type: str
        """

        self._channel = channel

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
        if not isinstance(other, SMS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
