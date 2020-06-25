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


class CallForwardJson(object):
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
        'class_of_service': 'str',
        'destination': 'str',
        'forward_to_voicemail': 'bool'
    }

    attribute_map = {
        'class_of_service': 'classOfService',
        'destination': 'destination',
        'forward_to_voicemail': 'forwardToVoicemail'
    }

    def __init__(self, class_of_service=None, destination=None, forward_to_voicemail=None):  # noqa: E501
        """CallForwardJson - a model defined in Swagger"""  # noqa: E501
        self._class_of_service = None
        self._destination = None
        self._forward_to_voicemail = None
        self.discriminator = None
        self.class_of_service = class_of_service
        self.destination = destination
        self.forward_to_voicemail = forward_to_voicemail

    @property
    def class_of_service(self):
        """Gets the class_of_service of this CallForwardJson.  # noqa: E501


        :return: The class_of_service of this CallForwardJson.  # noqa: E501
        :rtype: str
        """
        return self._class_of_service

    @class_of_service.setter
    def class_of_service(self, class_of_service):
        """Sets the class_of_service of this CallForwardJson.


        :param class_of_service: The class_of_service of this CallForwardJson.  # noqa: E501
        :type: str
        """
        if class_of_service is None:
            raise ValueError("Invalid value for `class_of_service`, must not be `None`")  # noqa: E501

        self._class_of_service = class_of_service

    @property
    def destination(self):
        """Gets the destination of this CallForwardJson.  # noqa: E501


        :return: The destination of this CallForwardJson.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this CallForwardJson.


        :param destination: The destination of this CallForwardJson.  # noqa: E501
        :type: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def forward_to_voicemail(self):
        """Gets the forward_to_voicemail of this CallForwardJson.  # noqa: E501


        :return: The forward_to_voicemail of this CallForwardJson.  # noqa: E501
        :rtype: bool
        """
        return self._forward_to_voicemail

    @forward_to_voicemail.setter
    def forward_to_voicemail(self, forward_to_voicemail):
        """Sets the forward_to_voicemail of this CallForwardJson.


        :param forward_to_voicemail: The forward_to_voicemail of this CallForwardJson.  # noqa: E501
        :type: bool
        """
        if forward_to_voicemail is None:
            raise ValueError("Invalid value for `forward_to_voicemail`, must not be `None`")  # noqa: E501

        self._forward_to_voicemail = forward_to_voicemail

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
        if issubclass(CallForwardJson, dict):
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
        if not isinstance(other, CallForwardJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
