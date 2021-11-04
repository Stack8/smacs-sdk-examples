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

class HighAvailabilitySettingsJson(object):
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
        'ha_enabled': 'bool',
        'sync_interval_in_hours': 'int',
        'url': 'str'
    }

    attribute_map = {
        'ha_enabled': 'haEnabled',
        'sync_interval_in_hours': 'syncIntervalInHours',
        'url': 'url'
    }

    def __init__(self, ha_enabled=None, sync_interval_in_hours=None, url=None):  # noqa: E501
        """HighAvailabilitySettingsJson - a model defined in Swagger"""  # noqa: E501
        self._ha_enabled = None
        self._sync_interval_in_hours = None
        self._url = None
        self.discriminator = None
        self.ha_enabled = ha_enabled
        self.sync_interval_in_hours = sync_interval_in_hours
        self.url = url

    @property
    def ha_enabled(self):
        """Gets the ha_enabled of this HighAvailabilitySettingsJson.  # noqa: E501


        :return: The ha_enabled of this HighAvailabilitySettingsJson.  # noqa: E501
        :rtype: bool
        """
        return self._ha_enabled

    @ha_enabled.setter
    def ha_enabled(self, ha_enabled):
        """Sets the ha_enabled of this HighAvailabilitySettingsJson.


        :param ha_enabled: The ha_enabled of this HighAvailabilitySettingsJson.  # noqa: E501
        :type: bool
        """
        if ha_enabled is None:
            raise ValueError("Invalid value for `ha_enabled`, must not be `None`")  # noqa: E501

        self._ha_enabled = ha_enabled

    @property
    def sync_interval_in_hours(self):
        """Gets the sync_interval_in_hours of this HighAvailabilitySettingsJson.  # noqa: E501


        :return: The sync_interval_in_hours of this HighAvailabilitySettingsJson.  # noqa: E501
        :rtype: int
        """
        return self._sync_interval_in_hours

    @sync_interval_in_hours.setter
    def sync_interval_in_hours(self, sync_interval_in_hours):
        """Sets the sync_interval_in_hours of this HighAvailabilitySettingsJson.


        :param sync_interval_in_hours: The sync_interval_in_hours of this HighAvailabilitySettingsJson.  # noqa: E501
        :type: int
        """
        if sync_interval_in_hours is None:
            raise ValueError("Invalid value for `sync_interval_in_hours`, must not be `None`")  # noqa: E501

        self._sync_interval_in_hours = sync_interval_in_hours

    @property
    def url(self):
        """Gets the url of this HighAvailabilitySettingsJson.  # noqa: E501


        :return: The url of this HighAvailabilitySettingsJson.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HighAvailabilitySettingsJson.


        :param url: The url of this HighAvailabilitySettingsJson.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if issubclass(HighAvailabilitySettingsJson, dict):
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
        if not isinstance(other, HighAvailabilitySettingsJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other