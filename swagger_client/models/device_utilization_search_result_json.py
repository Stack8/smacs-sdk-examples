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


class DeviceUtilizationSearchResultJson(object):
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
        'utilizations': 'list[DeviceUtilizationJson]',
        'total_results': 'int'
    }

    attribute_map = {
        'utilizations': 'utilizations',
        'total_results': 'totalResults'
    }

    def __init__(self, utilizations=None, total_results=None):  # noqa: E501
        """DeviceUtilizationSearchResultJson - a model defined in Swagger"""  # noqa: E501
        self._utilizations = None
        self._total_results = None
        self.discriminator = None
        if utilizations is not None:
            self.utilizations = utilizations
        if total_results is not None:
            self.total_results = total_results

    @property
    def utilizations(self):
        """Gets the utilizations of this DeviceUtilizationSearchResultJson.  # noqa: E501


        :return: The utilizations of this DeviceUtilizationSearchResultJson.  # noqa: E501
        :rtype: list[DeviceUtilizationJson]
        """
        return self._utilizations

    @utilizations.setter
    def utilizations(self, utilizations):
        """Sets the utilizations of this DeviceUtilizationSearchResultJson.


        :param utilizations: The utilizations of this DeviceUtilizationSearchResultJson.  # noqa: E501
        :type: list[DeviceUtilizationJson]
        """

        self._utilizations = utilizations

    @property
    def total_results(self):
        """Gets the total_results of this DeviceUtilizationSearchResultJson.  # noqa: E501


        :return: The total_results of this DeviceUtilizationSearchResultJson.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this DeviceUtilizationSearchResultJson.


        :param total_results: The total_results of this DeviceUtilizationSearchResultJson.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

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
        if issubclass(DeviceUtilizationSearchResultJson, dict):
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
        if not isinstance(other, DeviceUtilizationSearchResultJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
