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

class MobilityIdentityJson(object):
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
        'id': 'str',
        'name': 'str',
        'destination_number': 'str',
        'delay_before_ringing_in_seconds': 'float',
        'delay_stop_ringing_in_seconds': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'destination_number': 'destinationNumber',
        'delay_before_ringing_in_seconds': 'delayBeforeRingingInSeconds',
        'delay_stop_ringing_in_seconds': 'delayStopRingingInSeconds'
    }

    def __init__(self, id=None, name=None, destination_number=None, delay_before_ringing_in_seconds=None, delay_stop_ringing_in_seconds=None):  # noqa: E501
        """MobilityIdentityJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._destination_number = None
        self._delay_before_ringing_in_seconds = None
        self._delay_stop_ringing_in_seconds = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.destination_number = destination_number
        if delay_before_ringing_in_seconds is not None:
            self.delay_before_ringing_in_seconds = delay_before_ringing_in_seconds
        if delay_stop_ringing_in_seconds is not None:
            self.delay_stop_ringing_in_seconds = delay_stop_ringing_in_seconds

    @property
    def id(self):
        """Gets the id of this MobilityIdentityJson.  # noqa: E501


        :return: The id of this MobilityIdentityJson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MobilityIdentityJson.


        :param id: The id of this MobilityIdentityJson.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MobilityIdentityJson.  # noqa: E501


        :return: The name of this MobilityIdentityJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MobilityIdentityJson.


        :param name: The name of this MobilityIdentityJson.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def destination_number(self):
        """Gets the destination_number of this MobilityIdentityJson.  # noqa: E501


        :return: The destination_number of this MobilityIdentityJson.  # noqa: E501
        :rtype: str
        """
        return self._destination_number

    @destination_number.setter
    def destination_number(self, destination_number):
        """Sets the destination_number of this MobilityIdentityJson.


        :param destination_number: The destination_number of this MobilityIdentityJson.  # noqa: E501
        :type: str
        """
        if destination_number is None:
            raise ValueError("Invalid value for `destination_number`, must not be `None`")  # noqa: E501

        self._destination_number = destination_number

    @property
    def delay_before_ringing_in_seconds(self):
        """Gets the delay_before_ringing_in_seconds of this MobilityIdentityJson.  # noqa: E501


        :return: The delay_before_ringing_in_seconds of this MobilityIdentityJson.  # noqa: E501
        :rtype: float
        """
        return self._delay_before_ringing_in_seconds

    @delay_before_ringing_in_seconds.setter
    def delay_before_ringing_in_seconds(self, delay_before_ringing_in_seconds):
        """Sets the delay_before_ringing_in_seconds of this MobilityIdentityJson.


        :param delay_before_ringing_in_seconds: The delay_before_ringing_in_seconds of this MobilityIdentityJson.  # noqa: E501
        :type: float
        """

        self._delay_before_ringing_in_seconds = delay_before_ringing_in_seconds

    @property
    def delay_stop_ringing_in_seconds(self):
        """Gets the delay_stop_ringing_in_seconds of this MobilityIdentityJson.  # noqa: E501


        :return: The delay_stop_ringing_in_seconds of this MobilityIdentityJson.  # noqa: E501
        :rtype: float
        """
        return self._delay_stop_ringing_in_seconds

    @delay_stop_ringing_in_seconds.setter
    def delay_stop_ringing_in_seconds(self, delay_stop_ringing_in_seconds):
        """Sets the delay_stop_ringing_in_seconds of this MobilityIdentityJson.


        :param delay_stop_ringing_in_seconds: The delay_stop_ringing_in_seconds of this MobilityIdentityJson.  # noqa: E501
        :type: float
        """

        self._delay_stop_ringing_in_seconds = delay_stop_ringing_in_seconds

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
        if issubclass(MobilityIdentityJson, dict):
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
        if not isinstance(other, MobilityIdentityJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
