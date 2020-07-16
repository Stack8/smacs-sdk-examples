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


class TranslationPatternJson(object):
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
        'pattern': 'str',
        'route_partition': 'str',
        'description': 'str',
        'destination': 'str',
        'class_of_service': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pattern': 'pattern',
        'route_partition': 'routePartition',
        'description': 'description',
        'destination': 'destination',
        'class_of_service': 'classOfService'
    }

    def __init__(self, id=None, pattern=None, route_partition=None, description=None, destination=None, class_of_service=None):  # noqa: E501
        """TranslationPatternJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._pattern = None
        self._route_partition = None
        self._description = None
        self._destination = None
        self._class_of_service = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.pattern = pattern
        self.route_partition = route_partition
        self.description = description
        self.destination = destination
        self.class_of_service = class_of_service

    @property
    def id(self):
        """Gets the id of this TranslationPatternJson.  # noqa: E501


        :return: The id of this TranslationPatternJson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationPatternJson.


        :param id: The id of this TranslationPatternJson.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def pattern(self):
        """Gets the pattern of this TranslationPatternJson.  # noqa: E501


        :return: The pattern of this TranslationPatternJson.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this TranslationPatternJson.


        :param pattern: The pattern of this TranslationPatternJson.  # noqa: E501
        :type: str
        """
        if pattern is None:
            raise ValueError("Invalid value for `pattern`, must not be `None`")  # noqa: E501

        self._pattern = pattern

    @property
    def route_partition(self):
        """Gets the route_partition of this TranslationPatternJson.  # noqa: E501


        :return: The route_partition of this TranslationPatternJson.  # noqa: E501
        :rtype: str
        """
        return self._route_partition

    @route_partition.setter
    def route_partition(self, route_partition):
        """Sets the route_partition of this TranslationPatternJson.


        :param route_partition: The route_partition of this TranslationPatternJson.  # noqa: E501
        :type: str
        """
        if route_partition is None:
            raise ValueError("Invalid value for `route_partition`, must not be `None`")  # noqa: E501

        self._route_partition = route_partition

    @property
    def description(self):
        """Gets the description of this TranslationPatternJson.  # noqa: E501


        :return: The description of this TranslationPatternJson.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TranslationPatternJson.


        :param description: The description of this TranslationPatternJson.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def destination(self):
        """Gets the destination of this TranslationPatternJson.  # noqa: E501


        :return: The destination of this TranslationPatternJson.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this TranslationPatternJson.


        :param destination: The destination of this TranslationPatternJson.  # noqa: E501
        :type: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def class_of_service(self):
        """Gets the class_of_service of this TranslationPatternJson.  # noqa: E501


        :return: The class_of_service of this TranslationPatternJson.  # noqa: E501
        :rtype: str
        """
        return self._class_of_service

    @class_of_service.setter
    def class_of_service(self, class_of_service):
        """Sets the class_of_service of this TranslationPatternJson.


        :param class_of_service: The class_of_service of this TranslationPatternJson.  # noqa: E501
        :type: str
        """
        if class_of_service is None:
            raise ValueError("Invalid value for `class_of_service`, must not be `None`")  # noqa: E501

        self._class_of_service = class_of_service

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
        if issubclass(TranslationPatternJson, dict):
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
        if not isinstance(other, TranslationPatternJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
