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

class Microsoft365LicenseJson(object):
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
        'product_name': 'str',
        'sku_id': 'str',
        'sku_part_number': 'str',
        'associated_service_plans': 'list[str]'
    }

    attribute_map = {
        'product_name': 'productName',
        'sku_id': 'skuId',
        'sku_part_number': 'skuPartNumber',
        'associated_service_plans': 'associatedServicePlans'
    }

    def __init__(self, product_name=None, sku_id=None, sku_part_number=None, associated_service_plans=None):  # noqa: E501
        """Microsoft365LicenseJson - a model defined in Swagger"""  # noqa: E501
        self._product_name = None
        self._sku_id = None
        self._sku_part_number = None
        self._associated_service_plans = None
        self.discriminator = None
        if product_name is not None:
            self.product_name = product_name
        if sku_id is not None:
            self.sku_id = sku_id
        if sku_part_number is not None:
            self.sku_part_number = sku_part_number
        if associated_service_plans is not None:
            self.associated_service_plans = associated_service_plans

    @property
    def product_name(self):
        """Gets the product_name of this Microsoft365LicenseJson.  # noqa: E501


        :return: The product_name of this Microsoft365LicenseJson.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this Microsoft365LicenseJson.


        :param product_name: The product_name of this Microsoft365LicenseJson.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def sku_id(self):
        """Gets the sku_id of this Microsoft365LicenseJson.  # noqa: E501


        :return: The sku_id of this Microsoft365LicenseJson.  # noqa: E501
        :rtype: str
        """
        return self._sku_id

    @sku_id.setter
    def sku_id(self, sku_id):
        """Sets the sku_id of this Microsoft365LicenseJson.


        :param sku_id: The sku_id of this Microsoft365LicenseJson.  # noqa: E501
        :type: str
        """

        self._sku_id = sku_id

    @property
    def sku_part_number(self):
        """Gets the sku_part_number of this Microsoft365LicenseJson.  # noqa: E501


        :return: The sku_part_number of this Microsoft365LicenseJson.  # noqa: E501
        :rtype: str
        """
        return self._sku_part_number

    @sku_part_number.setter
    def sku_part_number(self, sku_part_number):
        """Sets the sku_part_number of this Microsoft365LicenseJson.


        :param sku_part_number: The sku_part_number of this Microsoft365LicenseJson.  # noqa: E501
        :type: str
        """

        self._sku_part_number = sku_part_number

    @property
    def associated_service_plans(self):
        """Gets the associated_service_plans of this Microsoft365LicenseJson.  # noqa: E501


        :return: The associated_service_plans of this Microsoft365LicenseJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._associated_service_plans

    @associated_service_plans.setter
    def associated_service_plans(self, associated_service_plans):
        """Sets the associated_service_plans of this Microsoft365LicenseJson.


        :param associated_service_plans: The associated_service_plans of this Microsoft365LicenseJson.  # noqa: E501
        :type: list[str]
        """

        self._associated_service_plans = associated_service_plans

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
        if issubclass(Microsoft365LicenseJson, dict):
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
        if not isinstance(other, Microsoft365LicenseJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
