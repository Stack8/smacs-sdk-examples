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

class DestinationFieldConfigJson(object):
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
        'name': 'TextFieldConfigJson',
        'destination': 'TextFieldConfigJson',
        'delay_before_ring': 'TextFieldConfigJson'
    }

    attribute_map = {
        'name': 'name',
        'destination': 'destination',
        'delay_before_ring': 'delayBeforeRing'
    }

    def __init__(self, name=None, destination=None, delay_before_ring=None):  # noqa: E501
        """DestinationFieldConfigJson - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._destination = None
        self._delay_before_ring = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if destination is not None:
            self.destination = destination
        if delay_before_ring is not None:
            self.delay_before_ring = delay_before_ring

    @property
    def name(self):
        """Gets the name of this DestinationFieldConfigJson.  # noqa: E501


        :return: The name of this DestinationFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DestinationFieldConfigJson.


        :param name: The name of this DestinationFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """

        self._name = name

    @property
    def destination(self):
        """Gets the destination of this DestinationFieldConfigJson.  # noqa: E501


        :return: The destination of this DestinationFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this DestinationFieldConfigJson.


        :param destination: The destination of this DestinationFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """

        self._destination = destination

    @property
    def delay_before_ring(self):
        """Gets the delay_before_ring of this DestinationFieldConfigJson.  # noqa: E501


        :return: The delay_before_ring of this DestinationFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._delay_before_ring

    @delay_before_ring.setter
    def delay_before_ring(self, delay_before_ring):
        """Sets the delay_before_ring of this DestinationFieldConfigJson.


        :param delay_before_ring: The delay_before_ring of this DestinationFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """

        self._delay_before_ring = delay_before_ring

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
        if issubclass(DestinationFieldConfigJson, dict):
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
        if not isinstance(other, DestinationFieldConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
