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


class LdapSyncJobStatusJson(object):
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
        'in_progress': 'bool',
        'clusters': 'list[ClusterLdapSyncInfoJson]'
    }

    attribute_map = {
        'in_progress': 'inProgress',
        'clusters': 'clusters'
    }

    def __init__(self, in_progress=None, clusters=None):  # noqa: E501
        """LdapSyncJobStatusJson - a model defined in Swagger"""  # noqa: E501
        self._in_progress = None
        self._clusters = None
        self.discriminator = None
        if in_progress is not None:
            self.in_progress = in_progress
        if clusters is not None:
            self.clusters = clusters

    @property
    def in_progress(self):
        """Gets the in_progress of this LdapSyncJobStatusJson.  # noqa: E501


        :return: The in_progress of this LdapSyncJobStatusJson.  # noqa: E501
        :rtype: bool
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """Sets the in_progress of this LdapSyncJobStatusJson.


        :param in_progress: The in_progress of this LdapSyncJobStatusJson.  # noqa: E501
        :type: bool
        """

        self._in_progress = in_progress

    @property
    def clusters(self):
        """Gets the clusters of this LdapSyncJobStatusJson.  # noqa: E501


        :return: The clusters of this LdapSyncJobStatusJson.  # noqa: E501
        :rtype: list[ClusterLdapSyncInfoJson]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this LdapSyncJobStatusJson.


        :param clusters: The clusters of this LdapSyncJobStatusJson.  # noqa: E501
        :type: list[ClusterLdapSyncInfoJson]
        """

        self._clusters = clusters

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
        if issubclass(LdapSyncJobStatusJson, dict):
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
        if not isinstance(other, LdapSyncJobStatusJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
