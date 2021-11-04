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

class SecurityProfile(object):
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
        'mode': 'str',
        'product_info_data': 'ProductInfoData'
    }

    attribute_map = {
        'name': 'name',
        'mode': 'mode',
        'product_info_data': 'productInfoData'
    }

    def __init__(self, name=None, mode=None, product_info_data=None):  # noqa: E501
        """SecurityProfile - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._mode = None
        self._product_info_data = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if product_info_data is not None:
            self.product_info_data = product_info_data

    @property
    def name(self):
        """Gets the name of this SecurityProfile.  # noqa: E501


        :return: The name of this SecurityProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityProfile.


        :param name: The name of this SecurityProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mode(self):
        """Gets the mode of this SecurityProfile.  # noqa: E501


        :return: The mode of this SecurityProfile.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this SecurityProfile.


        :param mode: The mode of this SecurityProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["NON_SECURE", "AUTHENTICATED", "ENCRYPTED"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def product_info_data(self):
        """Gets the product_info_data of this SecurityProfile.  # noqa: E501


        :return: The product_info_data of this SecurityProfile.  # noqa: E501
        :rtype: ProductInfoData
        """
        return self._product_info_data

    @product_info_data.setter
    def product_info_data(self, product_info_data):
        """Sets the product_info_data of this SecurityProfile.


        :param product_info_data: The product_info_data of this SecurityProfile.  # noqa: E501
        :type: ProductInfoData
        """

        self._product_info_data = product_info_data

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
        if issubclass(SecurityProfile, dict):
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
        if not isinstance(other, SecurityProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
