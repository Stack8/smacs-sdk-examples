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

class EndUserPinResetRequestJson(object):
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
        'pin': 'str',
        'reset_on_next_login': 'bool'
    }

    attribute_map = {
        'pin': 'pin',
        'reset_on_next_login': 'resetOnNextLogin'
    }

    def __init__(self, pin=None, reset_on_next_login=None):  # noqa: E501
        """EndUserPinResetRequestJson - a model defined in Swagger"""  # noqa: E501
        self._pin = None
        self._reset_on_next_login = None
        self.discriminator = None
        self.pin = pin
        self.reset_on_next_login = reset_on_next_login

    @property
    def pin(self):
        """Gets the pin of this EndUserPinResetRequestJson.  # noqa: E501


        :return: The pin of this EndUserPinResetRequestJson.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this EndUserPinResetRequestJson.


        :param pin: The pin of this EndUserPinResetRequestJson.  # noqa: E501
        :type: str
        """
        if pin is None:
            raise ValueError("Invalid value for `pin`, must not be `None`")  # noqa: E501

        self._pin = pin

    @property
    def reset_on_next_login(self):
        """Gets the reset_on_next_login of this EndUserPinResetRequestJson.  # noqa: E501


        :return: The reset_on_next_login of this EndUserPinResetRequestJson.  # noqa: E501
        :rtype: bool
        """
        return self._reset_on_next_login

    @reset_on_next_login.setter
    def reset_on_next_login(self, reset_on_next_login):
        """Sets the reset_on_next_login of this EndUserPinResetRequestJson.


        :param reset_on_next_login: The reset_on_next_login of this EndUserPinResetRequestJson.  # noqa: E501
        :type: bool
        """
        if reset_on_next_login is None:
            raise ValueError("Invalid value for `reset_on_next_login`, must not be `None`")  # noqa: E501

        self._reset_on_next_login = reset_on_next_login

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
        if issubclass(EndUserPinResetRequestJson, dict):
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
        if not isinstance(other, EndUserPinResetRequestJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
