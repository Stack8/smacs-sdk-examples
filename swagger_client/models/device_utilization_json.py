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

class DeviceUtilizationJson(object):
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
        'device_name': 'str',
        'owner_id': 'str',
        'model_name': 'str',
        'device_type': 'str',
        'description': 'str',
        'device_pool': 'str',
        'cluster_id': 'str',
        'total_duration': 'int',
        'recently_created_date': 'str',
        'registration_status': 'str',
        'last_used_date': 'str'
    }

    attribute_map = {
        'device_name': 'deviceName',
        'owner_id': 'ownerId',
        'model_name': 'modelName',
        'device_type': 'deviceType',
        'description': 'description',
        'device_pool': 'devicePool',
        'cluster_id': 'clusterId',
        'total_duration': 'totalDuration',
        'recently_created_date': 'recentlyCreatedDate',
        'registration_status': 'registrationStatus',
        'last_used_date': 'lastUsedDate'
    }

    def __init__(self, device_name=None, owner_id=None, model_name=None, device_type=None, description=None, device_pool=None, cluster_id=None, total_duration=None, recently_created_date=None, registration_status=None, last_used_date=None):  # noqa: E501
        """DeviceUtilizationJson - a model defined in Swagger"""  # noqa: E501
        self._device_name = None
        self._owner_id = None
        self._model_name = None
        self._device_type = None
        self._description = None
        self._device_pool = None
        self._cluster_id = None
        self._total_duration = None
        self._recently_created_date = None
        self._registration_status = None
        self._last_used_date = None
        self.discriminator = None
        if device_name is not None:
            self.device_name = device_name
        if owner_id is not None:
            self.owner_id = owner_id
        if model_name is not None:
            self.model_name = model_name
        if device_type is not None:
            self.device_type = device_type
        if description is not None:
            self.description = description
        if device_pool is not None:
            self.device_pool = device_pool
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if total_duration is not None:
            self.total_duration = total_duration
        if recently_created_date is not None:
            self.recently_created_date = recently_created_date
        if registration_status is not None:
            self.registration_status = registration_status
        if last_used_date is not None:
            self.last_used_date = last_used_date

    @property
    def device_name(self):
        """Gets the device_name of this DeviceUtilizationJson.  # noqa: E501


        :return: The device_name of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this DeviceUtilizationJson.


        :param device_name: The device_name of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def owner_id(self):
        """Gets the owner_id of this DeviceUtilizationJson.  # noqa: E501


        :return: The owner_id of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this DeviceUtilizationJson.


        :param owner_id: The owner_id of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def model_name(self):
        """Gets the model_name of this DeviceUtilizationJson.  # noqa: E501


        :return: The model_name of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this DeviceUtilizationJson.


        :param model_name: The model_name of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def device_type(self):
        """Gets the device_type of this DeviceUtilizationJson.  # noqa: E501


        :return: The device_type of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this DeviceUtilizationJson.


        :param device_type: The device_type of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """
        allowed_values = ["Desk Phone", "IM Softphone", "Android", "iPhone", "Tablet", "Extension Mobility", "CIPC", "Single Number Reach", "CTI Port", "CTI Remote Device", "Cisco Spark Remote Device"]  # noqa: E501
        if device_type not in allowed_values:
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def description(self):
        """Gets the description of this DeviceUtilizationJson.  # noqa: E501


        :return: The description of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceUtilizationJson.


        :param description: The description of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_pool(self):
        """Gets the device_pool of this DeviceUtilizationJson.  # noqa: E501


        :return: The device_pool of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._device_pool

    @device_pool.setter
    def device_pool(self, device_pool):
        """Sets the device_pool of this DeviceUtilizationJson.


        :param device_pool: The device_pool of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._device_pool = device_pool

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeviceUtilizationJson.  # noqa: E501


        :return: The cluster_id of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeviceUtilizationJson.


        :param cluster_id: The cluster_id of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def total_duration(self):
        """Gets the total_duration of this DeviceUtilizationJson.  # noqa: E501


        :return: The total_duration of this DeviceUtilizationJson.  # noqa: E501
        :rtype: int
        """
        return self._total_duration

    @total_duration.setter
    def total_duration(self, total_duration):
        """Sets the total_duration of this DeviceUtilizationJson.


        :param total_duration: The total_duration of this DeviceUtilizationJson.  # noqa: E501
        :type: int
        """

        self._total_duration = total_duration

    @property
    def recently_created_date(self):
        """Gets the recently_created_date of this DeviceUtilizationJson.  # noqa: E501


        :return: The recently_created_date of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._recently_created_date

    @recently_created_date.setter
    def recently_created_date(self, recently_created_date):
        """Sets the recently_created_date of this DeviceUtilizationJson.


        :param recently_created_date: The recently_created_date of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._recently_created_date = recently_created_date

    @property
    def registration_status(self):
        """Gets the registration_status of this DeviceUtilizationJson.  # noqa: E501


        :return: The registration_status of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._registration_status

    @registration_status.setter
    def registration_status(self, registration_status):
        """Sets the registration_status of this DeviceUtilizationJson.


        :param registration_status: The registration_status of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._registration_status = registration_status

    @property
    def last_used_date(self):
        """Gets the last_used_date of this DeviceUtilizationJson.  # noqa: E501


        :return: The last_used_date of this DeviceUtilizationJson.  # noqa: E501
        :rtype: str
        """
        return self._last_used_date

    @last_used_date.setter
    def last_used_date(self, last_used_date):
        """Sets the last_used_date of this DeviceUtilizationJson.


        :param last_used_date: The last_used_date of this DeviceUtilizationJson.  # noqa: E501
        :type: str
        """

        self._last_used_date = last_used_date

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
        if issubclass(DeviceUtilizationJson, dict):
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
        if not isinstance(other, DeviceUtilizationJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
