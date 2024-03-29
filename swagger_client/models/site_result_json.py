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

class SiteResultJson(object):
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
        'id': 'int',
        'name': 'str',
        'ldap_site_name': 'str',
        'device_pools': 'list[DevicePoolResultJson]',
        'has_permission': 'bool',
        'unity_server_id': 'int',
        'unity_server_description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ldap_site_name': 'ldapSiteName',
        'device_pools': 'devicePools',
        'has_permission': 'hasPermission',
        'unity_server_id': 'unityServerId',
        'unity_server_description': 'unityServerDescription'
    }

    def __init__(self, id=None, name=None, ldap_site_name=None, device_pools=None, has_permission=None, unity_server_id=None, unity_server_description=None):  # noqa: E501
        """SiteResultJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._ldap_site_name = None
        self._device_pools = None
        self._has_permission = None
        self._unity_server_id = None
        self._unity_server_description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ldap_site_name is not None:
            self.ldap_site_name = ldap_site_name
        if device_pools is not None:
            self.device_pools = device_pools
        if has_permission is not None:
            self.has_permission = has_permission
        if unity_server_id is not None:
            self.unity_server_id = unity_server_id
        if unity_server_description is not None:
            self.unity_server_description = unity_server_description

    @property
    def id(self):
        """Gets the id of this SiteResultJson.  # noqa: E501


        :return: The id of this SiteResultJson.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SiteResultJson.


        :param id: The id of this SiteResultJson.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SiteResultJson.  # noqa: E501


        :return: The name of this SiteResultJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteResultJson.


        :param name: The name of this SiteResultJson.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ldap_site_name(self):
        """Gets the ldap_site_name of this SiteResultJson.  # noqa: E501


        :return: The ldap_site_name of this SiteResultJson.  # noqa: E501
        :rtype: str
        """
        return self._ldap_site_name

    @ldap_site_name.setter
    def ldap_site_name(self, ldap_site_name):
        """Sets the ldap_site_name of this SiteResultJson.


        :param ldap_site_name: The ldap_site_name of this SiteResultJson.  # noqa: E501
        :type: str
        """

        self._ldap_site_name = ldap_site_name

    @property
    def device_pools(self):
        """Gets the device_pools of this SiteResultJson.  # noqa: E501


        :return: The device_pools of this SiteResultJson.  # noqa: E501
        :rtype: list[DevicePoolResultJson]
        """
        return self._device_pools

    @device_pools.setter
    def device_pools(self, device_pools):
        """Sets the device_pools of this SiteResultJson.


        :param device_pools: The device_pools of this SiteResultJson.  # noqa: E501
        :type: list[DevicePoolResultJson]
        """

        self._device_pools = device_pools

    @property
    def has_permission(self):
        """Gets the has_permission of this SiteResultJson.  # noqa: E501


        :return: The has_permission of this SiteResultJson.  # noqa: E501
        :rtype: bool
        """
        return self._has_permission

    @has_permission.setter
    def has_permission(self, has_permission):
        """Sets the has_permission of this SiteResultJson.


        :param has_permission: The has_permission of this SiteResultJson.  # noqa: E501
        :type: bool
        """

        self._has_permission = has_permission

    @property
    def unity_server_id(self):
        """Gets the unity_server_id of this SiteResultJson.  # noqa: E501


        :return: The unity_server_id of this SiteResultJson.  # noqa: E501
        :rtype: int
        """
        return self._unity_server_id

    @unity_server_id.setter
    def unity_server_id(self, unity_server_id):
        """Sets the unity_server_id of this SiteResultJson.


        :param unity_server_id: The unity_server_id of this SiteResultJson.  # noqa: E501
        :type: int
        """

        self._unity_server_id = unity_server_id

    @property
    def unity_server_description(self):
        """Gets the unity_server_description of this SiteResultJson.  # noqa: E501


        :return: The unity_server_description of this SiteResultJson.  # noqa: E501
        :rtype: str
        """
        return self._unity_server_description

    @unity_server_description.setter
    def unity_server_description(self, unity_server_description):
        """Sets the unity_server_description of this SiteResultJson.


        :param unity_server_description: The unity_server_description of this SiteResultJson.  # noqa: E501
        :type: str
        """

        self._unity_server_description = unity_server_description

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
        if issubclass(SiteResultJson, dict):
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
        if not isinstance(other, SiteResultJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
