# coding: utf-8

"""
    SMACS REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 7.2.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CommonPhoneProfileJson(object):
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
        'name': 'str',
        'line_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'line_mode': 'lineMode'
    }

    def __init__(self, name=None, line_mode=None):  # noqa: E501
        """CommonPhoneProfileJson - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._line_mode = None
        self.discriminator = None
        self.name = name
        self.line_mode = line_mode

    @property
    def name(self):
        """Gets the name of this CommonPhoneProfileJson.  # noqa: E501


        :return: The name of this CommonPhoneProfileJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommonPhoneProfileJson.


        :param name: The name of this CommonPhoneProfileJson.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def line_mode(self):
        """Gets the line_mode of this CommonPhoneProfileJson.  # noqa: E501


        :return: The line_mode of this CommonPhoneProfileJson.  # noqa: E501
        :rtype: str
        """
        return self._line_mode

    @line_mode.setter
    def line_mode(self, line_mode):
        """Sets the line_mode of this CommonPhoneProfileJson.


        :param line_mode: The line_mode of this CommonPhoneProfileJson.  # noqa: E501
        :type: str
        """
        if line_mode is None:
            raise ValueError("Invalid value for `line_mode`, must not be `None`")  # noqa: E501

        self._line_mode = line_mode

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
        if issubclass(CommonPhoneProfileJson, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CommonPhoneProfileJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
