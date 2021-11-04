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

class CheckboxFieldConfigJson(object):
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
        'default_value': 'bool'
    }

    attribute_map = {
        'default_value': 'defaultValue'
    }

    def __init__(self, default_value=None):  # noqa: E501
        """CheckboxFieldConfigJson - a model defined in Swagger"""  # noqa: E501
        self._default_value = None
        self.discriminator = None
        self.default_value = default_value

    @property
    def default_value(self):
        """Gets the default_value of this CheckboxFieldConfigJson.  # noqa: E501


        :return: The default_value of this CheckboxFieldConfigJson.  # noqa: E501
        :rtype: bool
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this CheckboxFieldConfigJson.


        :param default_value: The default_value of this CheckboxFieldConfigJson.  # noqa: E501
        :type: bool
        """
        if default_value is None:
            raise ValueError("Invalid value for `default_value`, must not be `None`")  # noqa: E501

        self._default_value = default_value

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
        if issubclass(CheckboxFieldConfigJson, dict):
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
        if not isinstance(other, CheckboxFieldConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
