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


class SnrProfileResultJson(object):
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
        'ref': 'SnrProfileRefJson',
        'owner': 'EndUserRefJson',
        'device_pool': 'str',
        'model': 'str'
    }

    attribute_map = {
        'ref': 'ref',
        'owner': 'owner',
        'device_pool': 'devicePool',
        'model': 'model'
    }

    def __init__(self, ref=None, owner=None, device_pool=None, model=None):  # noqa: E501
        """SnrProfileResultJson - a model defined in Swagger"""  # noqa: E501
        self._ref = None
        self._owner = None
        self._device_pool = None
        self._model = None
        self.discriminator = None
        if ref is not None:
            self.ref = ref
        if owner is not None:
            self.owner = owner
        if device_pool is not None:
            self.device_pool = device_pool
        if model is not None:
            self.model = model

    @property
    def ref(self):
        """Gets the ref of this SnrProfileResultJson.  # noqa: E501


        :return: The ref of this SnrProfileResultJson.  # noqa: E501
        :rtype: SnrProfileRefJson
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this SnrProfileResultJson.


        :param ref: The ref of this SnrProfileResultJson.  # noqa: E501
        :type: SnrProfileRefJson
        """

        self._ref = ref

    @property
    def owner(self):
        """Gets the owner of this SnrProfileResultJson.  # noqa: E501


        :return: The owner of this SnrProfileResultJson.  # noqa: E501
        :rtype: EndUserRefJson
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SnrProfileResultJson.


        :param owner: The owner of this SnrProfileResultJson.  # noqa: E501
        :type: EndUserRefJson
        """

        self._owner = owner

    @property
    def device_pool(self):
        """Gets the device_pool of this SnrProfileResultJson.  # noqa: E501


        :return: The device_pool of this SnrProfileResultJson.  # noqa: E501
        :rtype: str
        """
        return self._device_pool

    @device_pool.setter
    def device_pool(self, device_pool):
        """Sets the device_pool of this SnrProfileResultJson.


        :param device_pool: The device_pool of this SnrProfileResultJson.  # noqa: E501
        :type: str
        """

        self._device_pool = device_pool

    @property
    def model(self):
        """Gets the model of this SnrProfileResultJson.  # noqa: E501


        :return: The model of this SnrProfileResultJson.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this SnrProfileResultJson.


        :param model: The model of this SnrProfileResultJson.  # noqa: E501
        :type: str
        """

        self._model = model

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
        if issubclass(SnrProfileResultJson, dict):
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
        if not isinstance(other, SnrProfileResultJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
