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


class ErrorItem(object):
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
        'title': 'ResponseErrorTitle',
        'detail': 'str',
        'code': 'ResponseErrorCode',
        'source': 'str'
    }

    attribute_map = {
        'title': 'title',
        'detail': 'detail',
        'code': 'code',
        'source': 'source'
    }

    def __init__(self, title=None, detail=None, code=None, source=None):  # noqa: E501
        """ErrorItem - a model defined in OpenAPI"""  # noqa: E501

        self._title = None
        self._detail = None
        self._code = None
        self._source = None
        self.discriminator = None

        self.title = title
        self.detail = detail
        self.code = code
        self.source = source

    @property
    def title(self):
        """Gets the title of this ErrorItem.  # noqa: E501


        :return: The title of this ErrorItem.  # noqa: E501
        :rtype: ResponseErrorTitle
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ErrorItem.


        :param title: The title of this ErrorItem.  # noqa: E501
        :type: ResponseErrorTitle
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this ErrorItem.  # noqa: E501

        Free form more detailed description of the error.  # noqa: E501

        :return: The detail of this ErrorItem.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorItem.

        Free form more detailed description of the error.  # noqa: E501

        :param detail: The detail of this ErrorItem.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def code(self):
        """Gets the code of this ErrorItem.  # noqa: E501


        :return: The code of this ErrorItem.  # noqa: E501
        :rtype: ResponseErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorItem.


        :param code: The code of this ErrorItem.  # noqa: E501
        :type: ResponseErrorCode
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def source(self):
        """Gets the source of this ErrorItem.  # noqa: E501

        Describes which field is causing the issue in the payload, null for non 400 status code responses  # noqa: E501

        :return: The source of this ErrorItem.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ErrorItem.

        Describes which field is causing the issue in the payload, null for non 400 status code responses  # noqa: E501

        :param source: The source of this ErrorItem.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

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
        if not isinstance(other, ErrorItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
