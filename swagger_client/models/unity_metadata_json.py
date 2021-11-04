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

class UnityMetadataJson(object):
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
        'partition_object_ids': 'list[str]',
        'voicemail_templates': 'list[str]'
    }

    attribute_map = {
        'partition_object_ids': 'partitionObjectIds',
        'voicemail_templates': 'voicemailTemplates'
    }

    def __init__(self, partition_object_ids=None, voicemail_templates=None):  # noqa: E501
        """UnityMetadataJson - a model defined in Swagger"""  # noqa: E501
        self._partition_object_ids = None
        self._voicemail_templates = None
        self.discriminator = None
        self.partition_object_ids = partition_object_ids
        if voicemail_templates is not None:
            self.voicemail_templates = voicemail_templates

    @property
    def partition_object_ids(self):
        """Gets the partition_object_ids of this UnityMetadataJson.  # noqa: E501


        :return: The partition_object_ids of this UnityMetadataJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._partition_object_ids

    @partition_object_ids.setter
    def partition_object_ids(self, partition_object_ids):
        """Sets the partition_object_ids of this UnityMetadataJson.


        :param partition_object_ids: The partition_object_ids of this UnityMetadataJson.  # noqa: E501
        :type: list[str]
        """
        if partition_object_ids is None:
            raise ValueError("Invalid value for `partition_object_ids`, must not be `None`")  # noqa: E501

        self._partition_object_ids = partition_object_ids

    @property
    def voicemail_templates(self):
        """Gets the voicemail_templates of this UnityMetadataJson.  # noqa: E501


        :return: The voicemail_templates of this UnityMetadataJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._voicemail_templates

    @voicemail_templates.setter
    def voicemail_templates(self, voicemail_templates):
        """Sets the voicemail_templates of this UnityMetadataJson.


        :param voicemail_templates: The voicemail_templates of this UnityMetadataJson.  # noqa: E501
        :type: list[str]
        """

        self._voicemail_templates = voicemail_templates

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
        if issubclass(UnityMetadataJson, dict):
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
        if not isinstance(other, UnityMetadataJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other