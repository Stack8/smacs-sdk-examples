# coding: utf-8

"""
    Helpdesk REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.8.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LdapPermissionGroupJson(object):
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
        'admin_group': 'str',
        'mac_site_group': 'str',
        'mac_group': 'str',
        'helpdesk_group': 'str',
        'lookup_nested_groups': 'bool'
    }

    attribute_map = {
        'admin_group': 'adminGroup',
        'mac_site_group': 'macSiteGroup',
        'mac_group': 'macGroup',
        'helpdesk_group': 'helpdeskGroup',
        'lookup_nested_groups': 'lookupNestedGroups'
    }

    def __init__(self, admin_group=None, mac_site_group=None, mac_group=None, helpdesk_group=None, lookup_nested_groups=None):  # noqa: E501
        """LdapPermissionGroupJson - a model defined in Swagger"""  # noqa: E501
        self._admin_group = None
        self._mac_site_group = None
        self._mac_group = None
        self._helpdesk_group = None
        self._lookup_nested_groups = None
        self.discriminator = None
        self.admin_group = admin_group
        self.mac_site_group = mac_site_group
        self.mac_group = mac_group
        self.helpdesk_group = helpdesk_group
        if lookup_nested_groups is not None:
            self.lookup_nested_groups = lookup_nested_groups

    @property
    def admin_group(self):
        """Gets the admin_group of this LdapPermissionGroupJson.  # noqa: E501


        :return: The admin_group of this LdapPermissionGroupJson.  # noqa: E501
        :rtype: str
        """
        return self._admin_group

    @admin_group.setter
    def admin_group(self, admin_group):
        """Sets the admin_group of this LdapPermissionGroupJson.


        :param admin_group: The admin_group of this LdapPermissionGroupJson.  # noqa: E501
        :type: str
        """
        if admin_group is None:
            raise ValueError("Invalid value for `admin_group`, must not be `None`")  # noqa: E501

        self._admin_group = admin_group

    @property
    def mac_site_group(self):
        """Gets the mac_site_group of this LdapPermissionGroupJson.  # noqa: E501


        :return: The mac_site_group of this LdapPermissionGroupJson.  # noqa: E501
        :rtype: str
        """
        return self._mac_site_group

    @mac_site_group.setter
    def mac_site_group(self, mac_site_group):
        """Sets the mac_site_group of this LdapPermissionGroupJson.


        :param mac_site_group: The mac_site_group of this LdapPermissionGroupJson.  # noqa: E501
        :type: str
        """
        if mac_site_group is None:
            raise ValueError("Invalid value for `mac_site_group`, must not be `None`")  # noqa: E501

        self._mac_site_group = mac_site_group

    @property
    def mac_group(self):
        """Gets the mac_group of this LdapPermissionGroupJson.  # noqa: E501


        :return: The mac_group of this LdapPermissionGroupJson.  # noqa: E501
        :rtype: str
        """
        return self._mac_group

    @mac_group.setter
    def mac_group(self, mac_group):
        """Sets the mac_group of this LdapPermissionGroupJson.


        :param mac_group: The mac_group of this LdapPermissionGroupJson.  # noqa: E501
        :type: str
        """
        if mac_group is None:
            raise ValueError("Invalid value for `mac_group`, must not be `None`")  # noqa: E501

        self._mac_group = mac_group

    @property
    def helpdesk_group(self):
        """Gets the helpdesk_group of this LdapPermissionGroupJson.  # noqa: E501


        :return: The helpdesk_group of this LdapPermissionGroupJson.  # noqa: E501
        :rtype: str
        """
        return self._helpdesk_group

    @helpdesk_group.setter
    def helpdesk_group(self, helpdesk_group):
        """Sets the helpdesk_group of this LdapPermissionGroupJson.


        :param helpdesk_group: The helpdesk_group of this LdapPermissionGroupJson.  # noqa: E501
        :type: str
        """
        if helpdesk_group is None:
            raise ValueError("Invalid value for `helpdesk_group`, must not be `None`")  # noqa: E501

        self._helpdesk_group = helpdesk_group

    @property
    def lookup_nested_groups(self):
        """Gets the lookup_nested_groups of this LdapPermissionGroupJson.  # noqa: E501


        :return: The lookup_nested_groups of this LdapPermissionGroupJson.  # noqa: E501
        :rtype: bool
        """
        return self._lookup_nested_groups

    @lookup_nested_groups.setter
    def lookup_nested_groups(self, lookup_nested_groups):
        """Sets the lookup_nested_groups of this LdapPermissionGroupJson.


        :param lookup_nested_groups: The lookup_nested_groups of this LdapPermissionGroupJson.  # noqa: E501
        :type: bool
        """

        self._lookup_nested_groups = lookup_nested_groups

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
        if issubclass(LdapPermissionGroupJson, dict):
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
        if not isinstance(other, LdapPermissionGroupJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
