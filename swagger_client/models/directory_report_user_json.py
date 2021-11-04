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

class DirectoryReportUserJson(object):
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
        'ldap_user_id': 'str',
        'cucm_extension': 'str',
        'ldap_current_extension': 'str',
        'ldap_current_did': 'str',
        'ldap_expected_extension': 'str',
        'ldap_expected_did': 'str'
    }

    attribute_map = {
        'ldap_user_id': 'ldapUserId',
        'cucm_extension': 'cucmExtension',
        'ldap_current_extension': 'ldapCurrentExtension',
        'ldap_current_did': 'ldapCurrentDid',
        'ldap_expected_extension': 'ldapExpectedExtension',
        'ldap_expected_did': 'ldapExpectedDid'
    }

    def __init__(self, ldap_user_id=None, cucm_extension=None, ldap_current_extension=None, ldap_current_did=None, ldap_expected_extension=None, ldap_expected_did=None):  # noqa: E501
        """DirectoryReportUserJson - a model defined in Swagger"""  # noqa: E501
        self._ldap_user_id = None
        self._cucm_extension = None
        self._ldap_current_extension = None
        self._ldap_current_did = None
        self._ldap_expected_extension = None
        self._ldap_expected_did = None
        self.discriminator = None
        self.ldap_user_id = ldap_user_id
        if cucm_extension is not None:
            self.cucm_extension = cucm_extension
        if ldap_current_extension is not None:
            self.ldap_current_extension = ldap_current_extension
        if ldap_current_did is not None:
            self.ldap_current_did = ldap_current_did
        if ldap_expected_extension is not None:
            self.ldap_expected_extension = ldap_expected_extension
        if ldap_expected_did is not None:
            self.ldap_expected_did = ldap_expected_did

    @property
    def ldap_user_id(self):
        """Gets the ldap_user_id of this DirectoryReportUserJson.  # noqa: E501


        :return: The ldap_user_id of this DirectoryReportUserJson.  # noqa: E501
        :rtype: str
        """
        return self._ldap_user_id

    @ldap_user_id.setter
    def ldap_user_id(self, ldap_user_id):
        """Sets the ldap_user_id of this DirectoryReportUserJson.


        :param ldap_user_id: The ldap_user_id of this DirectoryReportUserJson.  # noqa: E501
        :type: str
        """
        if ldap_user_id is None:
            raise ValueError("Invalid value for `ldap_user_id`, must not be `None`")  # noqa: E501

        self._ldap_user_id = ldap_user_id

    @property
    def cucm_extension(self):
        """Gets the cucm_extension of this DirectoryReportUserJson.  # noqa: E501


        :return: The cucm_extension of this DirectoryReportUserJson.  # noqa: E501
        :rtype: str
        """
        return self._cucm_extension

    @cucm_extension.setter
    def cucm_extension(self, cucm_extension):
        """Sets the cucm_extension of this DirectoryReportUserJson.


        :param cucm_extension: The cucm_extension of this DirectoryReportUserJson.  # noqa: E501
        :type: str
        """

        self._cucm_extension = cucm_extension

    @property
    def ldap_current_extension(self):
        """Gets the ldap_current_extension of this DirectoryReportUserJson.  # noqa: E501


        :return: The ldap_current_extension of this DirectoryReportUserJson.  # noqa: E501
        :rtype: str
        """
        return self._ldap_current_extension

    @ldap_current_extension.setter
    def ldap_current_extension(self, ldap_current_extension):
        """Sets the ldap_current_extension of this DirectoryReportUserJson.


        :param ldap_current_extension: The ldap_current_extension of this DirectoryReportUserJson.  # noqa: E501
        :type: str
        """

        self._ldap_current_extension = ldap_current_extension

    @property
    def ldap_current_did(self):
        """Gets the ldap_current_did of this DirectoryReportUserJson.  # noqa: E501


        :return: The ldap_current_did of this DirectoryReportUserJson.  # noqa: E501
        :rtype: str
        """
        return self._ldap_current_did

    @ldap_current_did.setter
    def ldap_current_did(self, ldap_current_did):
        """Sets the ldap_current_did of this DirectoryReportUserJson.


        :param ldap_current_did: The ldap_current_did of this DirectoryReportUserJson.  # noqa: E501
        :type: str
        """

        self._ldap_current_did = ldap_current_did

    @property
    def ldap_expected_extension(self):
        """Gets the ldap_expected_extension of this DirectoryReportUserJson.  # noqa: E501


        :return: The ldap_expected_extension of this DirectoryReportUserJson.  # noqa: E501
        :rtype: str
        """
        return self._ldap_expected_extension

    @ldap_expected_extension.setter
    def ldap_expected_extension(self, ldap_expected_extension):
        """Sets the ldap_expected_extension of this DirectoryReportUserJson.


        :param ldap_expected_extension: The ldap_expected_extension of this DirectoryReportUserJson.  # noqa: E501
        :type: str
        """

        self._ldap_expected_extension = ldap_expected_extension

    @property
    def ldap_expected_did(self):
        """Gets the ldap_expected_did of this DirectoryReportUserJson.  # noqa: E501


        :return: The ldap_expected_did of this DirectoryReportUserJson.  # noqa: E501
        :rtype: str
        """
        return self._ldap_expected_did

    @ldap_expected_did.setter
    def ldap_expected_did(self, ldap_expected_did):
        """Sets the ldap_expected_did of this DirectoryReportUserJson.


        :param ldap_expected_did: The ldap_expected_did of this DirectoryReportUserJson.  # noqa: E501
        :type: str
        """

        self._ldap_expected_did = ldap_expected_did

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
        if issubclass(DirectoryReportUserJson, dict):
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
        if not isinstance(other, DirectoryReportUserJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
