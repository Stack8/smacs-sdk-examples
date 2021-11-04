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

class SnrFieldConfigJson(object):
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
        'device_pool': 'str',
        'snr_destination_for_teams': 'CheckboxFieldConfigJson',
        'profile_name': 'TextFieldConfigJson',
        'destination_name_for_microsoft_teams': 'TextFieldConfigJson',
        'destination_number_for_microsoft_teams': 'TextFieldConfigJson',
        'profile_description': 'TextFieldConfigJson',
        'calling_search_space': 'SelectFieldConfigJson',
        'aar_calling_search_space': 'SelectFieldConfigJson',
        'rerouting_calling_search_space': 'SelectFieldConfigJson',
        'user_moh_audio_source': 'SelectFieldConfigJson',
        'network_moh_audio_source': 'SelectFieldConfigJson',
        'destination_field_config_json': 'DestinationFieldConfigJson',
        'snr_destination_for_microsoft_teams': 'CheckboxFieldConfigJson',
        'privacy': 'SelectFieldConfigJson'
    }

    attribute_map = {
        'device_pool': 'devicePool',
        'snr_destination_for_teams': 'snrDestinationForTeams',
        'profile_name': 'profileName',
        'destination_name_for_microsoft_teams': 'destinationNameForMicrosoftTeams',
        'destination_number_for_microsoft_teams': 'destinationNumberForMicrosoftTeams',
        'profile_description': 'profileDescription',
        'calling_search_space': 'callingSearchSpace',
        'aar_calling_search_space': 'aarCallingSearchSpace',
        'rerouting_calling_search_space': 'reroutingCallingSearchSpace',
        'user_moh_audio_source': 'userMohAudioSource',
        'network_moh_audio_source': 'networkMohAudioSource',
        'destination_field_config_json': 'destinationFieldConfigJson',
        'snr_destination_for_microsoft_teams': 'snrDestinationForMicrosoftTeams',
        'privacy': 'privacy'
    }

    def __init__(self, device_pool=None, snr_destination_for_teams=None, profile_name=None, destination_name_for_microsoft_teams=None, destination_number_for_microsoft_teams=None, profile_description=None, calling_search_space=None, aar_calling_search_space=None, rerouting_calling_search_space=None, user_moh_audio_source=None, network_moh_audio_source=None, destination_field_config_json=None, snr_destination_for_microsoft_teams=None, privacy=None):  # noqa: E501
        """SnrFieldConfigJson - a model defined in Swagger"""  # noqa: E501
        self._device_pool = None
        self._snr_destination_for_teams = None
        self._profile_name = None
        self._destination_name_for_microsoft_teams = None
        self._destination_number_for_microsoft_teams = None
        self._profile_description = None
        self._calling_search_space = None
        self._aar_calling_search_space = None
        self._rerouting_calling_search_space = None
        self._user_moh_audio_source = None
        self._network_moh_audio_source = None
        self._destination_field_config_json = None
        self._snr_destination_for_microsoft_teams = None
        self._privacy = None
        self.discriminator = None
        self.device_pool = device_pool
        if snr_destination_for_teams is not None:
            self.snr_destination_for_teams = snr_destination_for_teams
        self.profile_name = profile_name
        self.destination_name_for_microsoft_teams = destination_name_for_microsoft_teams
        self.destination_number_for_microsoft_teams = destination_number_for_microsoft_teams
        self.profile_description = profile_description
        self.calling_search_space = calling_search_space
        self.aar_calling_search_space = aar_calling_search_space
        self.rerouting_calling_search_space = rerouting_calling_search_space
        self.user_moh_audio_source = user_moh_audio_source
        self.network_moh_audio_source = network_moh_audio_source
        self.destination_field_config_json = destination_field_config_json
        self.snr_destination_for_microsoft_teams = snr_destination_for_microsoft_teams
        self.privacy = privacy

    @property
    def device_pool(self):
        """Gets the device_pool of this SnrFieldConfigJson.  # noqa: E501


        :return: The device_pool of this SnrFieldConfigJson.  # noqa: E501
        :rtype: str
        """
        return self._device_pool

    @device_pool.setter
    def device_pool(self, device_pool):
        """Sets the device_pool of this SnrFieldConfigJson.


        :param device_pool: The device_pool of this SnrFieldConfigJson.  # noqa: E501
        :type: str
        """
        if device_pool is None:
            raise ValueError("Invalid value for `device_pool`, must not be `None`")  # noqa: E501

        self._device_pool = device_pool

    @property
    def snr_destination_for_teams(self):
        """Gets the snr_destination_for_teams of this SnrFieldConfigJson.  # noqa: E501


        :return: The snr_destination_for_teams of this SnrFieldConfigJson.  # noqa: E501
        :rtype: CheckboxFieldConfigJson
        """
        return self._snr_destination_for_teams

    @snr_destination_for_teams.setter
    def snr_destination_for_teams(self, snr_destination_for_teams):
        """Sets the snr_destination_for_teams of this SnrFieldConfigJson.


        :param snr_destination_for_teams: The snr_destination_for_teams of this SnrFieldConfigJson.  # noqa: E501
        :type: CheckboxFieldConfigJson
        """

        self._snr_destination_for_teams = snr_destination_for_teams

    @property
    def profile_name(self):
        """Gets the profile_name of this SnrFieldConfigJson.  # noqa: E501


        :return: The profile_name of this SnrFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this SnrFieldConfigJson.


        :param profile_name: The profile_name of this SnrFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """
        if profile_name is None:
            raise ValueError("Invalid value for `profile_name`, must not be `None`")  # noqa: E501

        self._profile_name = profile_name

    @property
    def destination_name_for_microsoft_teams(self):
        """Gets the destination_name_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501


        :return: The destination_name_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._destination_name_for_microsoft_teams

    @destination_name_for_microsoft_teams.setter
    def destination_name_for_microsoft_teams(self, destination_name_for_microsoft_teams):
        """Sets the destination_name_for_microsoft_teams of this SnrFieldConfigJson.


        :param destination_name_for_microsoft_teams: The destination_name_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """
        if destination_name_for_microsoft_teams is None:
            raise ValueError("Invalid value for `destination_name_for_microsoft_teams`, must not be `None`")  # noqa: E501

        self._destination_name_for_microsoft_teams = destination_name_for_microsoft_teams

    @property
    def destination_number_for_microsoft_teams(self):
        """Gets the destination_number_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501


        :return: The destination_number_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._destination_number_for_microsoft_teams

    @destination_number_for_microsoft_teams.setter
    def destination_number_for_microsoft_teams(self, destination_number_for_microsoft_teams):
        """Sets the destination_number_for_microsoft_teams of this SnrFieldConfigJson.


        :param destination_number_for_microsoft_teams: The destination_number_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """
        if destination_number_for_microsoft_teams is None:
            raise ValueError("Invalid value for `destination_number_for_microsoft_teams`, must not be `None`")  # noqa: E501

        self._destination_number_for_microsoft_teams = destination_number_for_microsoft_teams

    @property
    def profile_description(self):
        """Gets the profile_description of this SnrFieldConfigJson.  # noqa: E501


        :return: The profile_description of this SnrFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._profile_description

    @profile_description.setter
    def profile_description(self, profile_description):
        """Sets the profile_description of this SnrFieldConfigJson.


        :param profile_description: The profile_description of this SnrFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """
        if profile_description is None:
            raise ValueError("Invalid value for `profile_description`, must not be `None`")  # noqa: E501

        self._profile_description = profile_description

    @property
    def calling_search_space(self):
        """Gets the calling_search_space of this SnrFieldConfigJson.  # noqa: E501


        :return: The calling_search_space of this SnrFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._calling_search_space

    @calling_search_space.setter
    def calling_search_space(self, calling_search_space):
        """Sets the calling_search_space of this SnrFieldConfigJson.


        :param calling_search_space: The calling_search_space of this SnrFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if calling_search_space is None:
            raise ValueError("Invalid value for `calling_search_space`, must not be `None`")  # noqa: E501

        self._calling_search_space = calling_search_space

    @property
    def aar_calling_search_space(self):
        """Gets the aar_calling_search_space of this SnrFieldConfigJson.  # noqa: E501


        :return: The aar_calling_search_space of this SnrFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._aar_calling_search_space

    @aar_calling_search_space.setter
    def aar_calling_search_space(self, aar_calling_search_space):
        """Sets the aar_calling_search_space of this SnrFieldConfigJson.


        :param aar_calling_search_space: The aar_calling_search_space of this SnrFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if aar_calling_search_space is None:
            raise ValueError("Invalid value for `aar_calling_search_space`, must not be `None`")  # noqa: E501

        self._aar_calling_search_space = aar_calling_search_space

    @property
    def rerouting_calling_search_space(self):
        """Gets the rerouting_calling_search_space of this SnrFieldConfigJson.  # noqa: E501


        :return: The rerouting_calling_search_space of this SnrFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._rerouting_calling_search_space

    @rerouting_calling_search_space.setter
    def rerouting_calling_search_space(self, rerouting_calling_search_space):
        """Sets the rerouting_calling_search_space of this SnrFieldConfigJson.


        :param rerouting_calling_search_space: The rerouting_calling_search_space of this SnrFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if rerouting_calling_search_space is None:
            raise ValueError("Invalid value for `rerouting_calling_search_space`, must not be `None`")  # noqa: E501

        self._rerouting_calling_search_space = rerouting_calling_search_space

    @property
    def user_moh_audio_source(self):
        """Gets the user_moh_audio_source of this SnrFieldConfigJson.  # noqa: E501


        :return: The user_moh_audio_source of this SnrFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._user_moh_audio_source

    @user_moh_audio_source.setter
    def user_moh_audio_source(self, user_moh_audio_source):
        """Sets the user_moh_audio_source of this SnrFieldConfigJson.


        :param user_moh_audio_source: The user_moh_audio_source of this SnrFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if user_moh_audio_source is None:
            raise ValueError("Invalid value for `user_moh_audio_source`, must not be `None`")  # noqa: E501

        self._user_moh_audio_source = user_moh_audio_source

    @property
    def network_moh_audio_source(self):
        """Gets the network_moh_audio_source of this SnrFieldConfigJson.  # noqa: E501


        :return: The network_moh_audio_source of this SnrFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._network_moh_audio_source

    @network_moh_audio_source.setter
    def network_moh_audio_source(self, network_moh_audio_source):
        """Sets the network_moh_audio_source of this SnrFieldConfigJson.


        :param network_moh_audio_source: The network_moh_audio_source of this SnrFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if network_moh_audio_source is None:
            raise ValueError("Invalid value for `network_moh_audio_source`, must not be `None`")  # noqa: E501

        self._network_moh_audio_source = network_moh_audio_source

    @property
    def destination_field_config_json(self):
        """Gets the destination_field_config_json of this SnrFieldConfigJson.  # noqa: E501


        :return: The destination_field_config_json of this SnrFieldConfigJson.  # noqa: E501
        :rtype: DestinationFieldConfigJson
        """
        return self._destination_field_config_json

    @destination_field_config_json.setter
    def destination_field_config_json(self, destination_field_config_json):
        """Sets the destination_field_config_json of this SnrFieldConfigJson.


        :param destination_field_config_json: The destination_field_config_json of this SnrFieldConfigJson.  # noqa: E501
        :type: DestinationFieldConfigJson
        """
        if destination_field_config_json is None:
            raise ValueError("Invalid value for `destination_field_config_json`, must not be `None`")  # noqa: E501

        self._destination_field_config_json = destination_field_config_json

    @property
    def snr_destination_for_microsoft_teams(self):
        """Gets the snr_destination_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501


        :return: The snr_destination_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501
        :rtype: CheckboxFieldConfigJson
        """
        return self._snr_destination_for_microsoft_teams

    @snr_destination_for_microsoft_teams.setter
    def snr_destination_for_microsoft_teams(self, snr_destination_for_microsoft_teams):
        """Sets the snr_destination_for_microsoft_teams of this SnrFieldConfigJson.


        :param snr_destination_for_microsoft_teams: The snr_destination_for_microsoft_teams of this SnrFieldConfigJson.  # noqa: E501
        :type: CheckboxFieldConfigJson
        """
        if snr_destination_for_microsoft_teams is None:
            raise ValueError("Invalid value for `snr_destination_for_microsoft_teams`, must not be `None`")  # noqa: E501

        self._snr_destination_for_microsoft_teams = snr_destination_for_microsoft_teams

    @property
    def privacy(self):
        """Gets the privacy of this SnrFieldConfigJson.  # noqa: E501


        :return: The privacy of this SnrFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this SnrFieldConfigJson.


        :param privacy: The privacy of this SnrFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if privacy is None:
            raise ValueError("Invalid value for `privacy`, must not be `None`")  # noqa: E501

        self._privacy = privacy

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
        if issubclass(SnrFieldConfigJson, dict):
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
        if not isinstance(other, SnrFieldConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
