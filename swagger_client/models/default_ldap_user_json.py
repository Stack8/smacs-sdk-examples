# coding: utf-8

"""
    Helpdesk REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.8.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class DefaultLdapUserJson(object):
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
        'extension': 'str',
        'e164_number': 'str'
    }

    attribute_map = {
        'extension': 'extension',
        'e164_number': 'e164Number'
    }

    def __init__(self, extension=None, e164_number=None):  # noqa: E501
        """DefaultLdapUserJson - a model defined in Swagger"""  # noqa: E501
        self._extension = None
        self._e164_number = None
        self.discriminator = None
        if extension is not None:
            self.extension = extension
        if e164_number is not None:
            self.e164_number = e164_number

    @property
    def extension(self):
        """Gets the extension of this DefaultLdapUserJson.  # noqa: E501


        :return: The extension of this DefaultLdapUserJson.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this DefaultLdapUserJson.


        :param extension: The extension of this DefaultLdapUserJson.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def e164_number(self):
        """Gets the e164_number of this DefaultLdapUserJson.  # noqa: E501


        :return: The e164_number of this DefaultLdapUserJson.  # noqa: E501
        :rtype: str
        """
        return self._e164_number

    @e164_number.setter
    def e164_number(self, e164_number):
        """Sets the e164_number of this DefaultLdapUserJson.


        :param e164_number: The e164_number of this DefaultLdapUserJson.  # noqa: E501
        :type: str
        """

        self._e164_number = e164_number

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
        if issubclass(DefaultLdapUserJson, dict):
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
        if not isinstance(other, DefaultLdapUserJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
