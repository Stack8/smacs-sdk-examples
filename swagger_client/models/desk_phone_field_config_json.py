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

class DeskPhoneFieldConfigJson(object):
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
        'always_use_prime_line': 'SelectFieldConfigJson',
        'always_use_prime_line_for_voice_message': 'SelectFieldConfigJson',
        'associated_end_users': 'CustomMultiSelectEndUserRefFieldConfigJson',
        'associated_app_users': 'CustomMultiSelectAppUserRefFieldConfigJson',
        'built_in_bridge': 'SelectFieldConfigJson',
        'calling_search_space': 'SelectFieldConfigJson',
        'common_device_configuration': 'SelectFieldConfigJson',
        'common_phone_profile': 'SelectFieldConfigJson',
        'description': 'TextFieldConfigJson',
        'device_mobility_mode': 'SelectFieldConfigJson',
        'location': 'SelectFieldConfigJson',
        'network_moh_audio_source': 'SelectFieldConfigJson',
        'preferred_security_profile_mode': 'str',
        'privacy': 'SelectFieldConfigJson',
        'sip_profile_name': 'SelectFieldConfigJson',
        'subscribe_css': 'SelectFieldConfigJson',
        'user_moh_audio_source': 'SelectFieldConfigJson',
        'phone_model': 'SelectFieldConfigJson',
        'preferred_protocol': 'str',
        'phone_services': 'MultiSelectFieldConfigJsonPhoneServiceSubscriptionJson',
        'aar_calling_search_space': 'SelectFieldConfigJson',
        'rerouting_calling_search_space': 'SelectFieldConfigJson',
        'feature_control_policy': 'SelectFieldConfigJson',
        'language': 'SelectFieldConfigJson',
        'softkey_template': 'SelectFieldConfigJson',
        'disable_speaker_phone': 'CustomCheckboxFieldConfigJson',
        'ext_data_location_auth_server': 'TextFieldConfigJson',
        'ext_data_location_secure_auth_url': 'TextFieldConfigJson',
        'expansion_modules': 'list[ExpansionModuleModelJson]'
    }

    attribute_map = {
        'device_pool': 'devicePool',
        'always_use_prime_line': 'alwaysUsePrimeLine',
        'always_use_prime_line_for_voice_message': 'alwaysUsePrimeLineForVoiceMessage',
        'associated_end_users': 'associatedEndUsers',
        'associated_app_users': 'associatedAppUsers',
        'built_in_bridge': 'builtInBridge',
        'calling_search_space': 'callingSearchSpace',
        'common_device_configuration': 'commonDeviceConfiguration',
        'common_phone_profile': 'commonPhoneProfile',
        'description': 'description',
        'device_mobility_mode': 'deviceMobilityMode',
        'location': 'location',
        'network_moh_audio_source': 'networkMohAudioSource',
        'preferred_security_profile_mode': 'preferredSecurityProfileMode',
        'privacy': 'privacy',
        'sip_profile_name': 'sipProfileName',
        'subscribe_css': 'subscribeCss',
        'user_moh_audio_source': 'userMohAudioSource',
        'phone_model': 'phoneModel',
        'preferred_protocol': 'preferredProtocol',
        'phone_services': 'phoneServices',
        'aar_calling_search_space': 'aarCallingSearchSpace',
        'rerouting_calling_search_space': 'reroutingCallingSearchSpace',
        'feature_control_policy': 'featureControlPolicy',
        'language': 'language',
        'softkey_template': 'softkeyTemplate',
        'disable_speaker_phone': 'disableSpeakerPhone',
        'ext_data_location_auth_server': 'extDataLocationAuthServer',
        'ext_data_location_secure_auth_url': 'extDataLocationSecureAuthUrl',
        'expansion_modules': 'expansionModules'
    }

    def __init__(self, device_pool=None, always_use_prime_line=None, always_use_prime_line_for_voice_message=None, associated_end_users=None, associated_app_users=None, built_in_bridge=None, calling_search_space=None, common_device_configuration=None, common_phone_profile=None, description=None, device_mobility_mode=None, location=None, network_moh_audio_source=None, preferred_security_profile_mode=None, privacy=None, sip_profile_name=None, subscribe_css=None, user_moh_audio_source=None, phone_model=None, preferred_protocol=None, phone_services=None, aar_calling_search_space=None, rerouting_calling_search_space=None, feature_control_policy=None, language=None, softkey_template=None, disable_speaker_phone=None, ext_data_location_auth_server=None, ext_data_location_secure_auth_url=None, expansion_modules=None):  # noqa: E501
        """DeskPhoneFieldConfigJson - a model defined in Swagger"""  # noqa: E501
        self._device_pool = None
        self._always_use_prime_line = None
        self._always_use_prime_line_for_voice_message = None
        self._associated_end_users = None
        self._associated_app_users = None
        self._built_in_bridge = None
        self._calling_search_space = None
        self._common_device_configuration = None
        self._common_phone_profile = None
        self._description = None
        self._device_mobility_mode = None
        self._location = None
        self._network_moh_audio_source = None
        self._preferred_security_profile_mode = None
        self._privacy = None
        self._sip_profile_name = None
        self._subscribe_css = None
        self._user_moh_audio_source = None
        self._phone_model = None
        self._preferred_protocol = None
        self._phone_services = None
        self._aar_calling_search_space = None
        self._rerouting_calling_search_space = None
        self._feature_control_policy = None
        self._language = None
        self._softkey_template = None
        self._disable_speaker_phone = None
        self._ext_data_location_auth_server = None
        self._ext_data_location_secure_auth_url = None
        self._expansion_modules = None
        self.discriminator = None
        self.device_pool = device_pool
        self.always_use_prime_line = always_use_prime_line
        self.always_use_prime_line_for_voice_message = always_use_prime_line_for_voice_message
        self.associated_end_users = associated_end_users
        self.associated_app_users = associated_app_users
        self.built_in_bridge = built_in_bridge
        self.calling_search_space = calling_search_space
        self.common_device_configuration = common_device_configuration
        self.common_phone_profile = common_phone_profile
        self.description = description
        self.device_mobility_mode = device_mobility_mode
        self.location = location
        self.network_moh_audio_source = network_moh_audio_source
        self.preferred_security_profile_mode = preferred_security_profile_mode
        self.privacy = privacy
        self.sip_profile_name = sip_profile_name
        self.subscribe_css = subscribe_css
        self.user_moh_audio_source = user_moh_audio_source
        self.phone_model = phone_model
        self.preferred_protocol = preferred_protocol
        self.phone_services = phone_services
        self.aar_calling_search_space = aar_calling_search_space
        self.rerouting_calling_search_space = rerouting_calling_search_space
        self.feature_control_policy = feature_control_policy
        self.language = language
        self.softkey_template = softkey_template
        self.disable_speaker_phone = disable_speaker_phone
        self.ext_data_location_auth_server = ext_data_location_auth_server
        self.ext_data_location_secure_auth_url = ext_data_location_secure_auth_url
        self.expansion_modules = expansion_modules

    @property
    def device_pool(self):
        """Gets the device_pool of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The device_pool of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: str
        """
        return self._device_pool

    @device_pool.setter
    def device_pool(self, device_pool):
        """Sets the device_pool of this DeskPhoneFieldConfigJson.


        :param device_pool: The device_pool of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: str
        """
        if device_pool is None:
            raise ValueError("Invalid value for `device_pool`, must not be `None`")  # noqa: E501

        self._device_pool = device_pool

    @property
    def always_use_prime_line(self):
        """Gets the always_use_prime_line of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The always_use_prime_line of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._always_use_prime_line

    @always_use_prime_line.setter
    def always_use_prime_line(self, always_use_prime_line):
        """Sets the always_use_prime_line of this DeskPhoneFieldConfigJson.


        :param always_use_prime_line: The always_use_prime_line of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if always_use_prime_line is None:
            raise ValueError("Invalid value for `always_use_prime_line`, must not be `None`")  # noqa: E501

        self._always_use_prime_line = always_use_prime_line

    @property
    def always_use_prime_line_for_voice_message(self):
        """Gets the always_use_prime_line_for_voice_message of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The always_use_prime_line_for_voice_message of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._always_use_prime_line_for_voice_message

    @always_use_prime_line_for_voice_message.setter
    def always_use_prime_line_for_voice_message(self, always_use_prime_line_for_voice_message):
        """Sets the always_use_prime_line_for_voice_message of this DeskPhoneFieldConfigJson.


        :param always_use_prime_line_for_voice_message: The always_use_prime_line_for_voice_message of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if always_use_prime_line_for_voice_message is None:
            raise ValueError("Invalid value for `always_use_prime_line_for_voice_message`, must not be `None`")  # noqa: E501

        self._always_use_prime_line_for_voice_message = always_use_prime_line_for_voice_message

    @property
    def associated_end_users(self):
        """Gets the associated_end_users of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The associated_end_users of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: CustomMultiSelectEndUserRefFieldConfigJson
        """
        return self._associated_end_users

    @associated_end_users.setter
    def associated_end_users(self, associated_end_users):
        """Sets the associated_end_users of this DeskPhoneFieldConfigJson.


        :param associated_end_users: The associated_end_users of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: CustomMultiSelectEndUserRefFieldConfigJson
        """
        if associated_end_users is None:
            raise ValueError("Invalid value for `associated_end_users`, must not be `None`")  # noqa: E501

        self._associated_end_users = associated_end_users

    @property
    def associated_app_users(self):
        """Gets the associated_app_users of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The associated_app_users of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: CustomMultiSelectAppUserRefFieldConfigJson
        """
        return self._associated_app_users

    @associated_app_users.setter
    def associated_app_users(self, associated_app_users):
        """Sets the associated_app_users of this DeskPhoneFieldConfigJson.


        :param associated_app_users: The associated_app_users of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: CustomMultiSelectAppUserRefFieldConfigJson
        """
        if associated_app_users is None:
            raise ValueError("Invalid value for `associated_app_users`, must not be `None`")  # noqa: E501

        self._associated_app_users = associated_app_users

    @property
    def built_in_bridge(self):
        """Gets the built_in_bridge of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The built_in_bridge of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._built_in_bridge

    @built_in_bridge.setter
    def built_in_bridge(self, built_in_bridge):
        """Sets the built_in_bridge of this DeskPhoneFieldConfigJson.


        :param built_in_bridge: The built_in_bridge of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if built_in_bridge is None:
            raise ValueError("Invalid value for `built_in_bridge`, must not be `None`")  # noqa: E501

        self._built_in_bridge = built_in_bridge

    @property
    def calling_search_space(self):
        """Gets the calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._calling_search_space

    @calling_search_space.setter
    def calling_search_space(self, calling_search_space):
        """Sets the calling_search_space of this DeskPhoneFieldConfigJson.


        :param calling_search_space: The calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if calling_search_space is None:
            raise ValueError("Invalid value for `calling_search_space`, must not be `None`")  # noqa: E501

        self._calling_search_space = calling_search_space

    @property
    def common_device_configuration(self):
        """Gets the common_device_configuration of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The common_device_configuration of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._common_device_configuration

    @common_device_configuration.setter
    def common_device_configuration(self, common_device_configuration):
        """Sets the common_device_configuration of this DeskPhoneFieldConfigJson.


        :param common_device_configuration: The common_device_configuration of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if common_device_configuration is None:
            raise ValueError("Invalid value for `common_device_configuration`, must not be `None`")  # noqa: E501

        self._common_device_configuration = common_device_configuration

    @property
    def common_phone_profile(self):
        """Gets the common_phone_profile of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The common_phone_profile of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._common_phone_profile

    @common_phone_profile.setter
    def common_phone_profile(self, common_phone_profile):
        """Sets the common_phone_profile of this DeskPhoneFieldConfigJson.


        :param common_phone_profile: The common_phone_profile of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if common_phone_profile is None:
            raise ValueError("Invalid value for `common_phone_profile`, must not be `None`")  # noqa: E501

        self._common_phone_profile = common_phone_profile

    @property
    def description(self):
        """Gets the description of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The description of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeskPhoneFieldConfigJson.


        :param description: The description of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def device_mobility_mode(self):
        """Gets the device_mobility_mode of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The device_mobility_mode of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._device_mobility_mode

    @device_mobility_mode.setter
    def device_mobility_mode(self, device_mobility_mode):
        """Sets the device_mobility_mode of this DeskPhoneFieldConfigJson.


        :param device_mobility_mode: The device_mobility_mode of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if device_mobility_mode is None:
            raise ValueError("Invalid value for `device_mobility_mode`, must not be `None`")  # noqa: E501

        self._device_mobility_mode = device_mobility_mode

    @property
    def location(self):
        """Gets the location of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The location of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DeskPhoneFieldConfigJson.


        :param location: The location of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def network_moh_audio_source(self):
        """Gets the network_moh_audio_source of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The network_moh_audio_source of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._network_moh_audio_source

    @network_moh_audio_source.setter
    def network_moh_audio_source(self, network_moh_audio_source):
        """Sets the network_moh_audio_source of this DeskPhoneFieldConfigJson.


        :param network_moh_audio_source: The network_moh_audio_source of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if network_moh_audio_source is None:
            raise ValueError("Invalid value for `network_moh_audio_source`, must not be `None`")  # noqa: E501

        self._network_moh_audio_source = network_moh_audio_source

    @property
    def preferred_security_profile_mode(self):
        """Gets the preferred_security_profile_mode of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The preferred_security_profile_mode of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: str
        """
        return self._preferred_security_profile_mode

    @preferred_security_profile_mode.setter
    def preferred_security_profile_mode(self, preferred_security_profile_mode):
        """Sets the preferred_security_profile_mode of this DeskPhoneFieldConfigJson.


        :param preferred_security_profile_mode: The preferred_security_profile_mode of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: str
        """
        if preferred_security_profile_mode is None:
            raise ValueError("Invalid value for `preferred_security_profile_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["Encrypted", "Authenticated", "Non-Secure"]  # noqa: E501
        if preferred_security_profile_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `preferred_security_profile_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_security_profile_mode, allowed_values)
            )

        self._preferred_security_profile_mode = preferred_security_profile_mode

    @property
    def privacy(self):
        """Gets the privacy of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The privacy of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this DeskPhoneFieldConfigJson.


        :param privacy: The privacy of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if privacy is None:
            raise ValueError("Invalid value for `privacy`, must not be `None`")  # noqa: E501

        self._privacy = privacy

    @property
    def sip_profile_name(self):
        """Gets the sip_profile_name of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The sip_profile_name of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._sip_profile_name

    @sip_profile_name.setter
    def sip_profile_name(self, sip_profile_name):
        """Sets the sip_profile_name of this DeskPhoneFieldConfigJson.


        :param sip_profile_name: The sip_profile_name of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if sip_profile_name is None:
            raise ValueError("Invalid value for `sip_profile_name`, must not be `None`")  # noqa: E501

        self._sip_profile_name = sip_profile_name

    @property
    def subscribe_css(self):
        """Gets the subscribe_css of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The subscribe_css of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._subscribe_css

    @subscribe_css.setter
    def subscribe_css(self, subscribe_css):
        """Sets the subscribe_css of this DeskPhoneFieldConfigJson.


        :param subscribe_css: The subscribe_css of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if subscribe_css is None:
            raise ValueError("Invalid value for `subscribe_css`, must not be `None`")  # noqa: E501

        self._subscribe_css = subscribe_css

    @property
    def user_moh_audio_source(self):
        """Gets the user_moh_audio_source of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The user_moh_audio_source of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._user_moh_audio_source

    @user_moh_audio_source.setter
    def user_moh_audio_source(self, user_moh_audio_source):
        """Sets the user_moh_audio_source of this DeskPhoneFieldConfigJson.


        :param user_moh_audio_source: The user_moh_audio_source of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if user_moh_audio_source is None:
            raise ValueError("Invalid value for `user_moh_audio_source`, must not be `None`")  # noqa: E501

        self._user_moh_audio_source = user_moh_audio_source

    @property
    def phone_model(self):
        """Gets the phone_model of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The phone_model of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._phone_model

    @phone_model.setter
    def phone_model(self, phone_model):
        """Sets the phone_model of this DeskPhoneFieldConfigJson.


        :param phone_model: The phone_model of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if phone_model is None:
            raise ValueError("Invalid value for `phone_model`, must not be `None`")  # noqa: E501

        self._phone_model = phone_model

    @property
    def preferred_protocol(self):
        """Gets the preferred_protocol of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The preferred_protocol of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: str
        """
        return self._preferred_protocol

    @preferred_protocol.setter
    def preferred_protocol(self, preferred_protocol):
        """Sets the preferred_protocol of this DeskPhoneFieldConfigJson.


        :param preferred_protocol: The preferred_protocol of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: str
        """
        if preferred_protocol is None:
            raise ValueError("Invalid value for `preferred_protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["SCCP", "SIP", "NONE"]  # noqa: E501
        if preferred_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `preferred_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_protocol, allowed_values)
            )

        self._preferred_protocol = preferred_protocol

    @property
    def phone_services(self):
        """Gets the phone_services of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The phone_services of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: MultiSelectFieldConfigJsonPhoneServiceSubscriptionJson
        """
        return self._phone_services

    @phone_services.setter
    def phone_services(self, phone_services):
        """Sets the phone_services of this DeskPhoneFieldConfigJson.


        :param phone_services: The phone_services of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: MultiSelectFieldConfigJsonPhoneServiceSubscriptionJson
        """
        if phone_services is None:
            raise ValueError("Invalid value for `phone_services`, must not be `None`")  # noqa: E501

        self._phone_services = phone_services

    @property
    def aar_calling_search_space(self):
        """Gets the aar_calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The aar_calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._aar_calling_search_space

    @aar_calling_search_space.setter
    def aar_calling_search_space(self, aar_calling_search_space):
        """Sets the aar_calling_search_space of this DeskPhoneFieldConfigJson.


        :param aar_calling_search_space: The aar_calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if aar_calling_search_space is None:
            raise ValueError("Invalid value for `aar_calling_search_space`, must not be `None`")  # noqa: E501

        self._aar_calling_search_space = aar_calling_search_space

    @property
    def rerouting_calling_search_space(self):
        """Gets the rerouting_calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The rerouting_calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._rerouting_calling_search_space

    @rerouting_calling_search_space.setter
    def rerouting_calling_search_space(self, rerouting_calling_search_space):
        """Sets the rerouting_calling_search_space of this DeskPhoneFieldConfigJson.


        :param rerouting_calling_search_space: The rerouting_calling_search_space of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if rerouting_calling_search_space is None:
            raise ValueError("Invalid value for `rerouting_calling_search_space`, must not be `None`")  # noqa: E501

        self._rerouting_calling_search_space = rerouting_calling_search_space

    @property
    def feature_control_policy(self):
        """Gets the feature_control_policy of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The feature_control_policy of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._feature_control_policy

    @feature_control_policy.setter
    def feature_control_policy(self, feature_control_policy):
        """Sets the feature_control_policy of this DeskPhoneFieldConfigJson.


        :param feature_control_policy: The feature_control_policy of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if feature_control_policy is None:
            raise ValueError("Invalid value for `feature_control_policy`, must not be `None`")  # noqa: E501

        self._feature_control_policy = feature_control_policy

    @property
    def language(self):
        """Gets the language of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The language of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DeskPhoneFieldConfigJson.


        :param language: The language of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def softkey_template(self):
        """Gets the softkey_template of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The softkey_template of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._softkey_template

    @softkey_template.setter
    def softkey_template(self, softkey_template):
        """Sets the softkey_template of this DeskPhoneFieldConfigJson.


        :param softkey_template: The softkey_template of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if softkey_template is None:
            raise ValueError("Invalid value for `softkey_template`, must not be `None`")  # noqa: E501

        self._softkey_template = softkey_template

    @property
    def disable_speaker_phone(self):
        """Gets the disable_speaker_phone of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The disable_speaker_phone of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: CustomCheckboxFieldConfigJson
        """
        return self._disable_speaker_phone

    @disable_speaker_phone.setter
    def disable_speaker_phone(self, disable_speaker_phone):
        """Sets the disable_speaker_phone of this DeskPhoneFieldConfigJson.


        :param disable_speaker_phone: The disable_speaker_phone of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: CustomCheckboxFieldConfigJson
        """
        if disable_speaker_phone is None:
            raise ValueError("Invalid value for `disable_speaker_phone`, must not be `None`")  # noqa: E501

        self._disable_speaker_phone = disable_speaker_phone

    @property
    def ext_data_location_auth_server(self):
        """Gets the ext_data_location_auth_server of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The ext_data_location_auth_server of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._ext_data_location_auth_server

    @ext_data_location_auth_server.setter
    def ext_data_location_auth_server(self, ext_data_location_auth_server):
        """Sets the ext_data_location_auth_server of this DeskPhoneFieldConfigJson.


        :param ext_data_location_auth_server: The ext_data_location_auth_server of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """
        if ext_data_location_auth_server is None:
            raise ValueError("Invalid value for `ext_data_location_auth_server`, must not be `None`")  # noqa: E501

        self._ext_data_location_auth_server = ext_data_location_auth_server

    @property
    def ext_data_location_secure_auth_url(self):
        """Gets the ext_data_location_secure_auth_url of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The ext_data_location_secure_auth_url of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._ext_data_location_secure_auth_url

    @ext_data_location_secure_auth_url.setter
    def ext_data_location_secure_auth_url(self, ext_data_location_secure_auth_url):
        """Sets the ext_data_location_secure_auth_url of this DeskPhoneFieldConfigJson.


        :param ext_data_location_secure_auth_url: The ext_data_location_secure_auth_url of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """
        if ext_data_location_secure_auth_url is None:
            raise ValueError("Invalid value for `ext_data_location_secure_auth_url`, must not be `None`")  # noqa: E501

        self._ext_data_location_secure_auth_url = ext_data_location_secure_auth_url

    @property
    def expansion_modules(self):
        """Gets the expansion_modules of this DeskPhoneFieldConfigJson.  # noqa: E501


        :return: The expansion_modules of this DeskPhoneFieldConfigJson.  # noqa: E501
        :rtype: list[ExpansionModuleModelJson]
        """
        return self._expansion_modules

    @expansion_modules.setter
    def expansion_modules(self, expansion_modules):
        """Sets the expansion_modules of this DeskPhoneFieldConfigJson.


        :param expansion_modules: The expansion_modules of this DeskPhoneFieldConfigJson.  # noqa: E501
        :type: list[ExpansionModuleModelJson]
        """
        if expansion_modules is None:
            raise ValueError("Invalid value for `expansion_modules`, must not be `None`")  # noqa: E501

        self._expansion_modules = expansion_modules

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
        if issubclass(DeskPhoneFieldConfigJson, dict):
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
        if not isinstance(other, DeskPhoneFieldConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
