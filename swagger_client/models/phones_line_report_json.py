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

class PhonesLineReportJson(object):
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
        'line_feature_json': 'LineFeatureJson',
        'phone_result_json': 'PhoneResultJson',
        'applicable_fields_json': 'ApplicableFieldsJson'
    }

    attribute_map = {
        'line_feature_json': 'lineFeatureJson',
        'phone_result_json': 'phoneResultJson',
        'applicable_fields_json': 'applicableFieldsJson'
    }

    def __init__(self, line_feature_json=None, phone_result_json=None, applicable_fields_json=None):  # noqa: E501
        """PhonesLineReportJson - a model defined in Swagger"""  # noqa: E501
        self._line_feature_json = None
        self._phone_result_json = None
        self._applicable_fields_json = None
        self.discriminator = None
        if line_feature_json is not None:
            self.line_feature_json = line_feature_json
        self.phone_result_json = phone_result_json
        if applicable_fields_json is not None:
            self.applicable_fields_json = applicable_fields_json

    @property
    def line_feature_json(self):
        """Gets the line_feature_json of this PhonesLineReportJson.  # noqa: E501


        :return: The line_feature_json of this PhonesLineReportJson.  # noqa: E501
        :rtype: LineFeatureJson
        """
        return self._line_feature_json

    @line_feature_json.setter
    def line_feature_json(self, line_feature_json):
        """Sets the line_feature_json of this PhonesLineReportJson.


        :param line_feature_json: The line_feature_json of this PhonesLineReportJson.  # noqa: E501
        :type: LineFeatureJson
        """

        self._line_feature_json = line_feature_json

    @property
    def phone_result_json(self):
        """Gets the phone_result_json of this PhonesLineReportJson.  # noqa: E501


        :return: The phone_result_json of this PhonesLineReportJson.  # noqa: E501
        :rtype: PhoneResultJson
        """
        return self._phone_result_json

    @phone_result_json.setter
    def phone_result_json(self, phone_result_json):
        """Sets the phone_result_json of this PhonesLineReportJson.


        :param phone_result_json: The phone_result_json of this PhonesLineReportJson.  # noqa: E501
        :type: PhoneResultJson
        """
        if phone_result_json is None:
            raise ValueError("Invalid value for `phone_result_json`, must not be `None`")  # noqa: E501

        self._phone_result_json = phone_result_json

    @property
    def applicable_fields_json(self):
        """Gets the applicable_fields_json of this PhonesLineReportJson.  # noqa: E501


        :return: The applicable_fields_json of this PhonesLineReportJson.  # noqa: E501
        :rtype: ApplicableFieldsJson
        """
        return self._applicable_fields_json

    @applicable_fields_json.setter
    def applicable_fields_json(self, applicable_fields_json):
        """Sets the applicable_fields_json of this PhonesLineReportJson.


        :param applicable_fields_json: The applicable_fields_json of this PhonesLineReportJson.  # noqa: E501
        :type: ApplicableFieldsJson
        """

        self._applicable_fields_json = applicable_fields_json

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
        if issubclass(PhonesLineReportJson, dict):
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
        if not isinstance(other, PhonesLineReportJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
