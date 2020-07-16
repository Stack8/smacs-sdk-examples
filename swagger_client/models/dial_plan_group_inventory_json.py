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


class DialPlanGroupInventoryJson(object):
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
        'group_name': 'str',
        'site_ids': 'list[int]',
        'cluster_id': 'int',
        'available_and_undefined': 'int',
        'available_and_defined': 'int',
        'unavailable': 'int'
    }

    attribute_map = {
        'group_name': 'groupName',
        'site_ids': 'siteIds',
        'cluster_id': 'clusterId',
        'available_and_undefined': 'availableAndUndefined',
        'available_and_defined': 'availableAndDefined',
        'unavailable': 'unavailable'
    }

    def __init__(self, group_name=None, site_ids=None, cluster_id=None, available_and_undefined=None, available_and_defined=None, unavailable=None):  # noqa: E501
        """DialPlanGroupInventoryJson - a model defined in Swagger"""  # noqa: E501
        self._group_name = None
        self._site_ids = None
        self._cluster_id = None
        self._available_and_undefined = None
        self._available_and_defined = None
        self._unavailable = None
        self.discriminator = None
        if group_name is not None:
            self.group_name = group_name
        if site_ids is not None:
            self.site_ids = site_ids
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if available_and_undefined is not None:
            self.available_and_undefined = available_and_undefined
        if available_and_defined is not None:
            self.available_and_defined = available_and_defined
        if unavailable is not None:
            self.unavailable = unavailable

    @property
    def group_name(self):
        """Gets the group_name of this DialPlanGroupInventoryJson.  # noqa: E501


        :return: The group_name of this DialPlanGroupInventoryJson.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this DialPlanGroupInventoryJson.


        :param group_name: The group_name of this DialPlanGroupInventoryJson.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def site_ids(self):
        """Gets the site_ids of this DialPlanGroupInventoryJson.  # noqa: E501


        :return: The site_ids of this DialPlanGroupInventoryJson.  # noqa: E501
        :rtype: list[int]
        """
        return self._site_ids

    @site_ids.setter
    def site_ids(self, site_ids):
        """Sets the site_ids of this DialPlanGroupInventoryJson.


        :param site_ids: The site_ids of this DialPlanGroupInventoryJson.  # noqa: E501
        :type: list[int]
        """

        self._site_ids = site_ids

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DialPlanGroupInventoryJson.  # noqa: E501


        :return: The cluster_id of this DialPlanGroupInventoryJson.  # noqa: E501
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DialPlanGroupInventoryJson.


        :param cluster_id: The cluster_id of this DialPlanGroupInventoryJson.  # noqa: E501
        :type: int
        """

        self._cluster_id = cluster_id

    @property
    def available_and_undefined(self):
        """Gets the available_and_undefined of this DialPlanGroupInventoryJson.  # noqa: E501


        :return: The available_and_undefined of this DialPlanGroupInventoryJson.  # noqa: E501
        :rtype: int
        """
        return self._available_and_undefined

    @available_and_undefined.setter
    def available_and_undefined(self, available_and_undefined):
        """Sets the available_and_undefined of this DialPlanGroupInventoryJson.


        :param available_and_undefined: The available_and_undefined of this DialPlanGroupInventoryJson.  # noqa: E501
        :type: int
        """

        self._available_and_undefined = available_and_undefined

    @property
    def available_and_defined(self):
        """Gets the available_and_defined of this DialPlanGroupInventoryJson.  # noqa: E501


        :return: The available_and_defined of this DialPlanGroupInventoryJson.  # noqa: E501
        :rtype: int
        """
        return self._available_and_defined

    @available_and_defined.setter
    def available_and_defined(self, available_and_defined):
        """Sets the available_and_defined of this DialPlanGroupInventoryJson.


        :param available_and_defined: The available_and_defined of this DialPlanGroupInventoryJson.  # noqa: E501
        :type: int
        """

        self._available_and_defined = available_and_defined

    @property
    def unavailable(self):
        """Gets the unavailable of this DialPlanGroupInventoryJson.  # noqa: E501


        :return: The unavailable of this DialPlanGroupInventoryJson.  # noqa: E501
        :rtype: int
        """
        return self._unavailable

    @unavailable.setter
    def unavailable(self, unavailable):
        """Sets the unavailable of this DialPlanGroupInventoryJson.


        :param unavailable: The unavailable of this DialPlanGroupInventoryJson.  # noqa: E501
        :type: int
        """

        self._unavailable = unavailable

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
        if issubclass(DialPlanGroupInventoryJson, dict):
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
        if not isinstance(other, DialPlanGroupInventoryJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
