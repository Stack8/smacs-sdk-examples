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


class DirectoryNumberResultJson(object):
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
        'ref': 'DirectoryNumberRefJson',
        'route_partition': 'str',
        'callable': 'bool'
    }

    attribute_map = {
        'ref': 'ref',
        'route_partition': 'routePartition',
        'callable': 'callable'
    }

    def __init__(self, ref=None, route_partition=None, callable=None):  # noqa: E501
        """DirectoryNumberResultJson - a model defined in Swagger"""  # noqa: E501
        self._ref = None
        self._route_partition = None
        self._callable = None
        self.discriminator = None
        if ref is not None:
            self.ref = ref
        if route_partition is not None:
            self.route_partition = route_partition
        if callable is not None:
            self.callable = callable

    @property
    def ref(self):
        """Gets the ref of this DirectoryNumberResultJson.  # noqa: E501


        :return: The ref of this DirectoryNumberResultJson.  # noqa: E501
        :rtype: DirectoryNumberRefJson
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this DirectoryNumberResultJson.


        :param ref: The ref of this DirectoryNumberResultJson.  # noqa: E501
        :type: DirectoryNumberRefJson
        """

        self._ref = ref

    @property
    def route_partition(self):
        """Gets the route_partition of this DirectoryNumberResultJson.  # noqa: E501


        :return: The route_partition of this DirectoryNumberResultJson.  # noqa: E501
        :rtype: str
        """
        return self._route_partition

    @route_partition.setter
    def route_partition(self, route_partition):
        """Sets the route_partition of this DirectoryNumberResultJson.


        :param route_partition: The route_partition of this DirectoryNumberResultJson.  # noqa: E501
        :type: str
        """

        self._route_partition = route_partition

    @property
    def callable(self):
        """Gets the callable of this DirectoryNumberResultJson.  # noqa: E501


        :return: The callable of this DirectoryNumberResultJson.  # noqa: E501
        :rtype: bool
        """
        return self._callable

    @callable.setter
    def callable(self, callable):
        """Sets the callable of this DirectoryNumberResultJson.


        :param callable: The callable of this DirectoryNumberResultJson.  # noqa: E501
        :type: bool
        """

        self._callable = callable

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
        if issubclass(DirectoryNumberResultJson, dict):
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
        if not isinstance(other, DirectoryNumberResultJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
