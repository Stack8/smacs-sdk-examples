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

class LdapUserDialPlanAttributesJson(object):
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
        'username': 'str',
        'extension': 'str',
        'did': 'str'
    }

    attribute_map = {
        'username': 'username',
        'extension': 'extension',
        'did': 'did'
    }

    def __init__(self, username=None, extension=None, did=None):  # noqa: E501
        """LdapUserDialPlanAttributesJson - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._extension = None
        self._did = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if extension is not None:
            self.extension = extension
        if did is not None:
            self.did = did

    @property
    def username(self):
        """Gets the username of this LdapUserDialPlanAttributesJson.  # noqa: E501


        :return: The username of this LdapUserDialPlanAttributesJson.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LdapUserDialPlanAttributesJson.


        :param username: The username of this LdapUserDialPlanAttributesJson.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def extension(self):
        """Gets the extension of this LdapUserDialPlanAttributesJson.  # noqa: E501


        :return: The extension of this LdapUserDialPlanAttributesJson.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this LdapUserDialPlanAttributesJson.


        :param extension: The extension of this LdapUserDialPlanAttributesJson.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def did(self):
        """Gets the did of this LdapUserDialPlanAttributesJson.  # noqa: E501


        :return: The did of this LdapUserDialPlanAttributesJson.  # noqa: E501
        :rtype: str
        """
        return self._did

    @did.setter
    def did(self, did):
        """Sets the did of this LdapUserDialPlanAttributesJson.


        :param did: The did of this LdapUserDialPlanAttributesJson.  # noqa: E501
        :type: str
        """

        self._did = did

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
        if issubclass(LdapUserDialPlanAttributesJson, dict):
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
        if not isinstance(other, LdapUserDialPlanAttributesJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other