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


class LdapPublicConfigurationJson(object):
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
        'configured': 'bool',
        'extension_attribute_name': 'str',
        'e164_number_attribute_name': 'str'
    }

    attribute_map = {
        'configured': 'configured',
        'extension_attribute_name': 'extensionAttributeName',
        'e164_number_attribute_name': 'e164NumberAttributeName'
    }

    def __init__(self, configured=None, extension_attribute_name=None, e164_number_attribute_name=None):  # noqa: E501
        """LdapPublicConfigurationJson - a model defined in Swagger"""  # noqa: E501
        self._configured = None
        self._extension_attribute_name = None
        self._e164_number_attribute_name = None
        self.discriminator = None
        if configured is not None:
            self.configured = configured
        if extension_attribute_name is not None:
            self.extension_attribute_name = extension_attribute_name
        if e164_number_attribute_name is not None:
            self.e164_number_attribute_name = e164_number_attribute_name

    @property
    def configured(self):
        """Gets the configured of this LdapPublicConfigurationJson.  # noqa: E501


        :return: The configured of this LdapPublicConfigurationJson.  # noqa: E501
        :rtype: bool
        """
        return self._configured

    @configured.setter
    def configured(self, configured):
        """Sets the configured of this LdapPublicConfigurationJson.


        :param configured: The configured of this LdapPublicConfigurationJson.  # noqa: E501
        :type: bool
        """

        self._configured = configured

    @property
    def extension_attribute_name(self):
        """Gets the extension_attribute_name of this LdapPublicConfigurationJson.  # noqa: E501


        :return: The extension_attribute_name of this LdapPublicConfigurationJson.  # noqa: E501
        :rtype: str
        """
        return self._extension_attribute_name

    @extension_attribute_name.setter
    def extension_attribute_name(self, extension_attribute_name):
        """Sets the extension_attribute_name of this LdapPublicConfigurationJson.


        :param extension_attribute_name: The extension_attribute_name of this LdapPublicConfigurationJson.  # noqa: E501
        :type: str
        """

        self._extension_attribute_name = extension_attribute_name

    @property
    def e164_number_attribute_name(self):
        """Gets the e164_number_attribute_name of this LdapPublicConfigurationJson.  # noqa: E501


        :return: The e164_number_attribute_name of this LdapPublicConfigurationJson.  # noqa: E501
        :rtype: str
        """
        return self._e164_number_attribute_name

    @e164_number_attribute_name.setter
    def e164_number_attribute_name(self, e164_number_attribute_name):
        """Sets the e164_number_attribute_name of this LdapPublicConfigurationJson.


        :param e164_number_attribute_name: The e164_number_attribute_name of this LdapPublicConfigurationJson.  # noqa: E501
        :type: str
        """

        self._e164_number_attribute_name = e164_number_attribute_name

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
        if issubclass(LdapPublicConfigurationJson, dict):
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
        if not isinstance(other, LdapPublicConfigurationJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
