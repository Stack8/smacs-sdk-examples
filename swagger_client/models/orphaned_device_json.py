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

class OrphanedDeviceJson(object):
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
        'cluster_id': 'str',
        'pkid': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'cluster_id': 'clusterId',
        'pkid': 'pkid',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, cluster_id=None, pkid=None, name=None, type=None):  # noqa: E501
        """OrphanedDeviceJson - a model defined in Swagger"""  # noqa: E501
        self._cluster_id = None
        self._pkid = None
        self._name = None
        self._type = None
        self.discriminator = None
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if pkid is not None:
            self.pkid = pkid
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this OrphanedDeviceJson.  # noqa: E501


        :return: The cluster_id of this OrphanedDeviceJson.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this OrphanedDeviceJson.


        :param cluster_id: The cluster_id of this OrphanedDeviceJson.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def pkid(self):
        """Gets the pkid of this OrphanedDeviceJson.  # noqa: E501


        :return: The pkid of this OrphanedDeviceJson.  # noqa: E501
        :rtype: str
        """
        return self._pkid

    @pkid.setter
    def pkid(self, pkid):
        """Sets the pkid of this OrphanedDeviceJson.


        :param pkid: The pkid of this OrphanedDeviceJson.  # noqa: E501
        :type: str
        """

        self._pkid = pkid

    @property
    def name(self):
        """Gets the name of this OrphanedDeviceJson.  # noqa: E501


        :return: The name of this OrphanedDeviceJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrphanedDeviceJson.


        :param name: The name of this OrphanedDeviceJson.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this OrphanedDeviceJson.  # noqa: E501


        :return: The type of this OrphanedDeviceJson.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrphanedDeviceJson.


        :param type: The type of this OrphanedDeviceJson.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(OrphanedDeviceJson, dict):
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
        if not isinstance(other, OrphanedDeviceJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
