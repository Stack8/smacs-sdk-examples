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

class PhoneServiceSubscriptionJson(object):
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
        'name': 'str',
        'phone_service_id': 'str',
        'phone_service_name': 'str',
        'parameters': 'list[NvpJson]'
    }

    attribute_map = {
        'name': 'name',
        'phone_service_id': 'phoneServiceId',
        'phone_service_name': 'phoneServiceName',
        'parameters': 'parameters'
    }

    def __init__(self, name=None, phone_service_id=None, phone_service_name=None, parameters=None):  # noqa: E501
        """PhoneServiceSubscriptionJson - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._phone_service_id = None
        self._phone_service_name = None
        self._parameters = None
        self.discriminator = None
        self.name = name
        self.phone_service_id = phone_service_id
        self.phone_service_name = phone_service_name
        self.parameters = parameters

    @property
    def name(self):
        """Gets the name of this PhoneServiceSubscriptionJson.  # noqa: E501


        :return: The name of this PhoneServiceSubscriptionJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhoneServiceSubscriptionJson.


        :param name: The name of this PhoneServiceSubscriptionJson.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def phone_service_id(self):
        """Gets the phone_service_id of this PhoneServiceSubscriptionJson.  # noqa: E501


        :return: The phone_service_id of this PhoneServiceSubscriptionJson.  # noqa: E501
        :rtype: str
        """
        return self._phone_service_id

    @phone_service_id.setter
    def phone_service_id(self, phone_service_id):
        """Sets the phone_service_id of this PhoneServiceSubscriptionJson.


        :param phone_service_id: The phone_service_id of this PhoneServiceSubscriptionJson.  # noqa: E501
        :type: str
        """
        if phone_service_id is None:
            raise ValueError("Invalid value for `phone_service_id`, must not be `None`")  # noqa: E501

        self._phone_service_id = phone_service_id

    @property
    def phone_service_name(self):
        """Gets the phone_service_name of this PhoneServiceSubscriptionJson.  # noqa: E501


        :return: The phone_service_name of this PhoneServiceSubscriptionJson.  # noqa: E501
        :rtype: str
        """
        return self._phone_service_name

    @phone_service_name.setter
    def phone_service_name(self, phone_service_name):
        """Sets the phone_service_name of this PhoneServiceSubscriptionJson.


        :param phone_service_name: The phone_service_name of this PhoneServiceSubscriptionJson.  # noqa: E501
        :type: str
        """
        if phone_service_name is None:
            raise ValueError("Invalid value for `phone_service_name`, must not be `None`")  # noqa: E501

        self._phone_service_name = phone_service_name

    @property
    def parameters(self):
        """Gets the parameters of this PhoneServiceSubscriptionJson.  # noqa: E501


        :return: The parameters of this PhoneServiceSubscriptionJson.  # noqa: E501
        :rtype: list[NvpJson]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PhoneServiceSubscriptionJson.


        :param parameters: The parameters of this PhoneServiceSubscriptionJson.  # noqa: E501
        :type: list[NvpJson]
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if issubclass(PhoneServiceSubscriptionJson, dict):
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
        if not isinstance(other, PhoneServiceSubscriptionJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
