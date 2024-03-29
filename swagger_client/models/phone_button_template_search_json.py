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

class PhoneButtonTemplateSearchJson(object):
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
        'model': 'str',
        'protocol': 'str',
        'features': 'list[str]',
        'cucm_server_id': 'int',
        'match_limit': 'int'
    }

    attribute_map = {
        'model': 'model',
        'protocol': 'protocol',
        'features': 'features',
        'cucm_server_id': 'cucmServerId',
        'match_limit': 'matchLimit'
    }

    def __init__(self, model=None, protocol=None, features=None, cucm_server_id=None, match_limit=None):  # noqa: E501
        """PhoneButtonTemplateSearchJson - a model defined in Swagger"""  # noqa: E501
        self._model = None
        self._protocol = None
        self._features = None
        self._cucm_server_id = None
        self._match_limit = None
        self.discriminator = None
        self.model = model
        self.protocol = protocol
        self.features = features
        self.cucm_server_id = cucm_server_id
        if match_limit is not None:
            self.match_limit = match_limit

    @property
    def model(self):
        """Gets the model of this PhoneButtonTemplateSearchJson.  # noqa: E501


        :return: The model of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PhoneButtonTemplateSearchJson.


        :param model: The model of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def protocol(self):
        """Gets the protocol of this PhoneButtonTemplateSearchJson.  # noqa: E501


        :return: The protocol of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PhoneButtonTemplateSearchJson.


        :param protocol: The protocol of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def features(self):
        """Gets the features of this PhoneButtonTemplateSearchJson.  # noqa: E501


        :return: The features of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this PhoneButtonTemplateSearchJson.


        :param features: The features of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :type: list[str]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def cucm_server_id(self):
        """Gets the cucm_server_id of this PhoneButtonTemplateSearchJson.  # noqa: E501


        :return: The cucm_server_id of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :rtype: int
        """
        return self._cucm_server_id

    @cucm_server_id.setter
    def cucm_server_id(self, cucm_server_id):
        """Sets the cucm_server_id of this PhoneButtonTemplateSearchJson.


        :param cucm_server_id: The cucm_server_id of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :type: int
        """
        if cucm_server_id is None:
            raise ValueError("Invalid value for `cucm_server_id`, must not be `None`")  # noqa: E501

        self._cucm_server_id = cucm_server_id

    @property
    def match_limit(self):
        """Gets the match_limit of this PhoneButtonTemplateSearchJson.  # noqa: E501


        :return: The match_limit of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :rtype: int
        """
        return self._match_limit

    @match_limit.setter
    def match_limit(self, match_limit):
        """Sets the match_limit of this PhoneButtonTemplateSearchJson.


        :param match_limit: The match_limit of this PhoneButtonTemplateSearchJson.  # noqa: E501
        :type: int
        """

        self._match_limit = match_limit

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
        if issubclass(PhoneButtonTemplateSearchJson, dict):
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
        if not isinstance(other, PhoneButtonTemplateSearchJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
