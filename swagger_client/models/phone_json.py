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

class PhoneJson(object):
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
        'name': 'str',
        'description': 'str',
        'device_pool': 'str',
        'model': 'str',
        'protocol': 'str',
        'owner': 'EndUserRefJson',
        'class_of_service': 'str',
        'aar_class_of_service': 'str',
        'rerouting_calling_search_space': 'str',
        'phone_button_template': 'PhoneButtonTemplateRefJson',
        'common_phone_profile': 'str',
        'common_device_configuration': 'str',
        'user_locale': 'str',
        'user_moh_source_name': 'str',
        'network_moh_source_name': 'str',
        'location': 'str',
        'softkey_template': 'str',
        'disable_speaker_phone': 'bool',
        'privacy': 'str',
        'device_mobility_mode': 'str',
        'security_profile_name': 'str',
        'sip_profile_name': 'str',
        'always_use_prime_line': 'str',
        'always_use_prime_line_for_voice_message': 'str',
        'built_in_bridge': 'str',
        'feature_control_policy_name': 'str',
        'buttons': 'list[ButtonJson]',
        'expansion_modules': 'list[str]',
        'associated_app_users': 'list[AppUserRefJson]',
        'associated_end_users': 'list[EndUserRefJson]',
        'service_subscriptions': 'list[PhoneServiceSubscriptionJson]',
        'phone_load_name': 'str',
        'subscribe_css': 'str',
        'emergency_numbers': 'str',
        'cisco_support_field': 'str',
        'ext_data_location_auth_server': 'str',
        'ext_data_location_secure_auth_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'device_pool': 'devicePool',
        'model': 'model',
        'protocol': 'protocol',
        'owner': 'owner',
        'class_of_service': 'classOfService',
        'aar_class_of_service': 'aarClassOfService',
        'rerouting_calling_search_space': 'reroutingCallingSearchSpace',
        'phone_button_template': 'phoneButtonTemplate',
        'common_phone_profile': 'commonPhoneProfile',
        'common_device_configuration': 'commonDeviceConfiguration',
        'user_locale': 'userLocale',
        'user_moh_source_name': 'userMohSourceName',
        'network_moh_source_name': 'networkMohSourceName',
        'location': 'location',
        'softkey_template': 'softkeyTemplate',
        'disable_speaker_phone': 'disableSpeakerPhone',
        'privacy': 'privacy',
        'device_mobility_mode': 'deviceMobilityMode',
        'security_profile_name': 'securityProfileName',
        'sip_profile_name': 'sipProfileName',
        'always_use_prime_line': 'alwaysUsePrimeLine',
        'always_use_prime_line_for_voice_message': 'alwaysUsePrimeLineForVoiceMessage',
        'built_in_bridge': 'builtInBridge',
        'feature_control_policy_name': 'featureControlPolicyName',
        'buttons': 'buttons',
        'expansion_modules': 'expansionModules',
        'associated_app_users': 'associatedAppUsers',
        'associated_end_users': 'associatedEndUsers',
        'service_subscriptions': 'serviceSubscriptions',
        'phone_load_name': 'phoneLoadName',
        'subscribe_css': 'subscribeCss',
        'emergency_numbers': 'emergencyNumbers',
        'cisco_support_field': 'ciscoSupportField',
        'ext_data_location_auth_server': 'extDataLocationAuthServer',
        'ext_data_location_secure_auth_url': 'extDataLocationSecureAuthUrl'
    }

    def __init__(self, id=None, name=None, description=None, device_pool=None, model=None, protocol=None, owner=None, class_of_service=None, aar_class_of_service=None, rerouting_calling_search_space=None, phone_button_template=None, common_phone_profile=None, common_device_configuration=None, user_locale=None, user_moh_source_name=None, network_moh_source_name=None, location=None, softkey_template=None, disable_speaker_phone=None, privacy=None, device_mobility_mode=None, security_profile_name=None, sip_profile_name=None, always_use_prime_line=None, always_use_prime_line_for_voice_message=None, built_in_bridge=None, feature_control_policy_name=None, buttons=None, expansion_modules=None, associated_app_users=None, associated_end_users=None, service_subscriptions=None, phone_load_name=None, subscribe_css=None, emergency_numbers=None, cisco_support_field=None, ext_data_location_auth_server=None, ext_data_location_secure_auth_url=None):  # noqa: E501
        """PhoneJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._device_pool = None
        self._model = None
        self._protocol = None
        self._owner = None
        self._class_of_service = None
        self._aar_class_of_service = None
        self._rerouting_calling_search_space = None
        self._phone_button_template = None
        self._common_phone_profile = None
        self._common_device_configuration = None
        self._user_locale = None
        self._user_moh_source_name = None
        self._network_moh_source_name = None
        self._location = None
        self._softkey_template = None
        self._disable_speaker_phone = None
        self._privacy = None
        self._device_mobility_mode = None
        self._security_profile_name = None
        self._sip_profile_name = None
        self._always_use_prime_line = None
        self._always_use_prime_line_for_voice_message = None
        self._built_in_bridge = None
        self._feature_control_policy_name = None
        self._buttons = None
        self._expansion_modules = None
        self._associated_app_users = None
        self._associated_end_users = None
        self._service_subscriptions = None
        self._phone_load_name = None
        self._subscribe_css = None
        self._emergency_numbers = None
        self._cisco_support_field = None
        self._ext_data_location_auth_server = None
        self._ext_data_location_secure_auth_url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.description = description
        self.device_pool = device_pool
        self.model = model
        self.protocol = protocol
        if owner is not None:
            self.owner = owner
        self.class_of_service = class_of_service
        self.aar_class_of_service = aar_class_of_service
        self.rerouting_calling_search_space = rerouting_calling_search_space
        self.phone_button_template = phone_button_template
        self.common_phone_profile = common_phone_profile
        self.common_device_configuration = common_device_configuration
        self.user_locale = user_locale
        self.user_moh_source_name = user_moh_source_name
        self.network_moh_source_name = network_moh_source_name
        self.location = location
        if softkey_template is not None:
            self.softkey_template = softkey_template
        self.disable_speaker_phone = disable_speaker_phone
        self.privacy = privacy
        self.device_mobility_mode = device_mobility_mode
        self.security_profile_name = security_profile_name
        self.sip_profile_name = sip_profile_name
        self.always_use_prime_line = always_use_prime_line
        self.always_use_prime_line_for_voice_message = always_use_prime_line_for_voice_message
        self.built_in_bridge = built_in_bridge
        self.feature_control_policy_name = feature_control_policy_name
        self.buttons = buttons
        self.expansion_modules = expansion_modules
        self.associated_app_users = associated_app_users
        self.associated_end_users = associated_end_users
        self.service_subscriptions = service_subscriptions
        self.phone_load_name = phone_load_name
        self.subscribe_css = subscribe_css
        self.emergency_numbers = emergency_numbers
        self.cisco_support_field = cisco_support_field
        self.ext_data_location_auth_server = ext_data_location_auth_server
        self.ext_data_location_secure_auth_url = ext_data_location_secure_auth_url

    @property
    def id(self):
        """Gets the id of this PhoneJson.  # noqa: E501


        :return: The id of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhoneJson.


        :param id: The id of this PhoneJson.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PhoneJson.  # noqa: E501


        :return: The name of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhoneJson.


        :param name: The name of this PhoneJson.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this PhoneJson.  # noqa: E501


        :return: The description of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PhoneJson.


        :param description: The description of this PhoneJson.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def device_pool(self):
        """Gets the device_pool of this PhoneJson.  # noqa: E501


        :return: The device_pool of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._device_pool

    @device_pool.setter
    def device_pool(self, device_pool):
        """Sets the device_pool of this PhoneJson.


        :param device_pool: The device_pool of this PhoneJson.  # noqa: E501
        :type: str
        """
        if device_pool is None:
            raise ValueError("Invalid value for `device_pool`, must not be `None`")  # noqa: E501

        self._device_pool = device_pool

    @property
    def model(self):
        """Gets the model of this PhoneJson.  # noqa: E501


        :return: The model of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PhoneJson.


        :param model: The model of this PhoneJson.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def protocol(self):
        """Gets the protocol of this PhoneJson.  # noqa: E501


        :return: The protocol of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PhoneJson.


        :param protocol: The protocol of this PhoneJson.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def owner(self):
        """Gets the owner of this PhoneJson.  # noqa: E501


        :return: The owner of this PhoneJson.  # noqa: E501
        :rtype: EndUserRefJson
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this PhoneJson.


        :param owner: The owner of this PhoneJson.  # noqa: E501
        :type: EndUserRefJson
        """

        self._owner = owner

    @property
    def class_of_service(self):
        """Gets the class_of_service of this PhoneJson.  # noqa: E501


        :return: The class_of_service of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._class_of_service

    @class_of_service.setter
    def class_of_service(self, class_of_service):
        """Sets the class_of_service of this PhoneJson.


        :param class_of_service: The class_of_service of this PhoneJson.  # noqa: E501
        :type: str
        """
        if class_of_service is None:
            raise ValueError("Invalid value for `class_of_service`, must not be `None`")  # noqa: E501

        self._class_of_service = class_of_service

    @property
    def aar_class_of_service(self):
        """Gets the aar_class_of_service of this PhoneJson.  # noqa: E501


        :return: The aar_class_of_service of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._aar_class_of_service

    @aar_class_of_service.setter
    def aar_class_of_service(self, aar_class_of_service):
        """Sets the aar_class_of_service of this PhoneJson.


        :param aar_class_of_service: The aar_class_of_service of this PhoneJson.  # noqa: E501
        :type: str
        """
        if aar_class_of_service is None:
            raise ValueError("Invalid value for `aar_class_of_service`, must not be `None`")  # noqa: E501

        self._aar_class_of_service = aar_class_of_service

    @property
    def rerouting_calling_search_space(self):
        """Gets the rerouting_calling_search_space of this PhoneJson.  # noqa: E501


        :return: The rerouting_calling_search_space of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._rerouting_calling_search_space

    @rerouting_calling_search_space.setter
    def rerouting_calling_search_space(self, rerouting_calling_search_space):
        """Sets the rerouting_calling_search_space of this PhoneJson.


        :param rerouting_calling_search_space: The rerouting_calling_search_space of this PhoneJson.  # noqa: E501
        :type: str
        """
        if rerouting_calling_search_space is None:
            raise ValueError("Invalid value for `rerouting_calling_search_space`, must not be `None`")  # noqa: E501

        self._rerouting_calling_search_space = rerouting_calling_search_space

    @property
    def phone_button_template(self):
        """Gets the phone_button_template of this PhoneJson.  # noqa: E501


        :return: The phone_button_template of this PhoneJson.  # noqa: E501
        :rtype: PhoneButtonTemplateRefJson
        """
        return self._phone_button_template

    @phone_button_template.setter
    def phone_button_template(self, phone_button_template):
        """Sets the phone_button_template of this PhoneJson.


        :param phone_button_template: The phone_button_template of this PhoneJson.  # noqa: E501
        :type: PhoneButtonTemplateRefJson
        """
        if phone_button_template is None:
            raise ValueError("Invalid value for `phone_button_template`, must not be `None`")  # noqa: E501

        self._phone_button_template = phone_button_template

    @property
    def common_phone_profile(self):
        """Gets the common_phone_profile of this PhoneJson.  # noqa: E501


        :return: The common_phone_profile of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._common_phone_profile

    @common_phone_profile.setter
    def common_phone_profile(self, common_phone_profile):
        """Sets the common_phone_profile of this PhoneJson.


        :param common_phone_profile: The common_phone_profile of this PhoneJson.  # noqa: E501
        :type: str
        """
        if common_phone_profile is None:
            raise ValueError("Invalid value for `common_phone_profile`, must not be `None`")  # noqa: E501

        self._common_phone_profile = common_phone_profile

    @property
    def common_device_configuration(self):
        """Gets the common_device_configuration of this PhoneJson.  # noqa: E501


        :return: The common_device_configuration of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._common_device_configuration

    @common_device_configuration.setter
    def common_device_configuration(self, common_device_configuration):
        """Sets the common_device_configuration of this PhoneJson.


        :param common_device_configuration: The common_device_configuration of this PhoneJson.  # noqa: E501
        :type: str
        """
        if common_device_configuration is None:
            raise ValueError("Invalid value for `common_device_configuration`, must not be `None`")  # noqa: E501

        self._common_device_configuration = common_device_configuration

    @property
    def user_locale(self):
        """Gets the user_locale of this PhoneJson.  # noqa: E501


        :return: The user_locale of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._user_locale

    @user_locale.setter
    def user_locale(self, user_locale):
        """Sets the user_locale of this PhoneJson.


        :param user_locale: The user_locale of this PhoneJson.  # noqa: E501
        :type: str
        """
        if user_locale is None:
            raise ValueError("Invalid value for `user_locale`, must not be `None`")  # noqa: E501

        self._user_locale = user_locale

    @property
    def user_moh_source_name(self):
        """Gets the user_moh_source_name of this PhoneJson.  # noqa: E501


        :return: The user_moh_source_name of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._user_moh_source_name

    @user_moh_source_name.setter
    def user_moh_source_name(self, user_moh_source_name):
        """Sets the user_moh_source_name of this PhoneJson.


        :param user_moh_source_name: The user_moh_source_name of this PhoneJson.  # noqa: E501
        :type: str
        """
        if user_moh_source_name is None:
            raise ValueError("Invalid value for `user_moh_source_name`, must not be `None`")  # noqa: E501

        self._user_moh_source_name = user_moh_source_name

    @property
    def network_moh_source_name(self):
        """Gets the network_moh_source_name of this PhoneJson.  # noqa: E501


        :return: The network_moh_source_name of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._network_moh_source_name

    @network_moh_source_name.setter
    def network_moh_source_name(self, network_moh_source_name):
        """Sets the network_moh_source_name of this PhoneJson.


        :param network_moh_source_name: The network_moh_source_name of this PhoneJson.  # noqa: E501
        :type: str
        """
        if network_moh_source_name is None:
            raise ValueError("Invalid value for `network_moh_source_name`, must not be `None`")  # noqa: E501

        self._network_moh_source_name = network_moh_source_name

    @property
    def location(self):
        """Gets the location of this PhoneJson.  # noqa: E501


        :return: The location of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PhoneJson.


        :param location: The location of this PhoneJson.  # noqa: E501
        :type: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def softkey_template(self):
        """Gets the softkey_template of this PhoneJson.  # noqa: E501


        :return: The softkey_template of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._softkey_template

    @softkey_template.setter
    def softkey_template(self, softkey_template):
        """Sets the softkey_template of this PhoneJson.


        :param softkey_template: The softkey_template of this PhoneJson.  # noqa: E501
        :type: str
        """

        self._softkey_template = softkey_template

    @property
    def disable_speaker_phone(self):
        """Gets the disable_speaker_phone of this PhoneJson.  # noqa: E501


        :return: The disable_speaker_phone of this PhoneJson.  # noqa: E501
        :rtype: bool
        """
        return self._disable_speaker_phone

    @disable_speaker_phone.setter
    def disable_speaker_phone(self, disable_speaker_phone):
        """Sets the disable_speaker_phone of this PhoneJson.


        :param disable_speaker_phone: The disable_speaker_phone of this PhoneJson.  # noqa: E501
        :type: bool
        """
        if disable_speaker_phone is None:
            raise ValueError("Invalid value for `disable_speaker_phone`, must not be `None`")  # noqa: E501

        self._disable_speaker_phone = disable_speaker_phone

    @property
    def privacy(self):
        """Gets the privacy of this PhoneJson.  # noqa: E501


        :return: The privacy of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this PhoneJson.


        :param privacy: The privacy of this PhoneJson.  # noqa: E501
        :type: str
        """
        if privacy is None:
            raise ValueError("Invalid value for `privacy`, must not be `None`")  # noqa: E501

        self._privacy = privacy

    @property
    def device_mobility_mode(self):
        """Gets the device_mobility_mode of this PhoneJson.  # noqa: E501


        :return: The device_mobility_mode of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._device_mobility_mode

    @device_mobility_mode.setter
    def device_mobility_mode(self, device_mobility_mode):
        """Sets the device_mobility_mode of this PhoneJson.


        :param device_mobility_mode: The device_mobility_mode of this PhoneJson.  # noqa: E501
        :type: str
        """
        if device_mobility_mode is None:
            raise ValueError("Invalid value for `device_mobility_mode`, must not be `None`")  # noqa: E501

        self._device_mobility_mode = device_mobility_mode

    @property
    def security_profile_name(self):
        """Gets the security_profile_name of this PhoneJson.  # noqa: E501


        :return: The security_profile_name of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._security_profile_name

    @security_profile_name.setter
    def security_profile_name(self, security_profile_name):
        """Sets the security_profile_name of this PhoneJson.


        :param security_profile_name: The security_profile_name of this PhoneJson.  # noqa: E501
        :type: str
        """
        if security_profile_name is None:
            raise ValueError("Invalid value for `security_profile_name`, must not be `None`")  # noqa: E501

        self._security_profile_name = security_profile_name

    @property
    def sip_profile_name(self):
        """Gets the sip_profile_name of this PhoneJson.  # noqa: E501


        :return: The sip_profile_name of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._sip_profile_name

    @sip_profile_name.setter
    def sip_profile_name(self, sip_profile_name):
        """Sets the sip_profile_name of this PhoneJson.


        :param sip_profile_name: The sip_profile_name of this PhoneJson.  # noqa: E501
        :type: str
        """
        if sip_profile_name is None:
            raise ValueError("Invalid value for `sip_profile_name`, must not be `None`")  # noqa: E501

        self._sip_profile_name = sip_profile_name

    @property
    def always_use_prime_line(self):
        """Gets the always_use_prime_line of this PhoneJson.  # noqa: E501


        :return: The always_use_prime_line of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._always_use_prime_line

    @always_use_prime_line.setter
    def always_use_prime_line(self, always_use_prime_line):
        """Sets the always_use_prime_line of this PhoneJson.


        :param always_use_prime_line: The always_use_prime_line of this PhoneJson.  # noqa: E501
        :type: str
        """
        if always_use_prime_line is None:
            raise ValueError("Invalid value for `always_use_prime_line`, must not be `None`")  # noqa: E501

        self._always_use_prime_line = always_use_prime_line

    @property
    def always_use_prime_line_for_voice_message(self):
        """Gets the always_use_prime_line_for_voice_message of this PhoneJson.  # noqa: E501


        :return: The always_use_prime_line_for_voice_message of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._always_use_prime_line_for_voice_message

    @always_use_prime_line_for_voice_message.setter
    def always_use_prime_line_for_voice_message(self, always_use_prime_line_for_voice_message):
        """Sets the always_use_prime_line_for_voice_message of this PhoneJson.


        :param always_use_prime_line_for_voice_message: The always_use_prime_line_for_voice_message of this PhoneJson.  # noqa: E501
        :type: str
        """
        if always_use_prime_line_for_voice_message is None:
            raise ValueError("Invalid value for `always_use_prime_line_for_voice_message`, must not be `None`")  # noqa: E501

        self._always_use_prime_line_for_voice_message = always_use_prime_line_for_voice_message

    @property
    def built_in_bridge(self):
        """Gets the built_in_bridge of this PhoneJson.  # noqa: E501


        :return: The built_in_bridge of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._built_in_bridge

    @built_in_bridge.setter
    def built_in_bridge(self, built_in_bridge):
        """Sets the built_in_bridge of this PhoneJson.


        :param built_in_bridge: The built_in_bridge of this PhoneJson.  # noqa: E501
        :type: str
        """
        if built_in_bridge is None:
            raise ValueError("Invalid value for `built_in_bridge`, must not be `None`")  # noqa: E501

        self._built_in_bridge = built_in_bridge

    @property
    def feature_control_policy_name(self):
        """Gets the feature_control_policy_name of this PhoneJson.  # noqa: E501


        :return: The feature_control_policy_name of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._feature_control_policy_name

    @feature_control_policy_name.setter
    def feature_control_policy_name(self, feature_control_policy_name):
        """Sets the feature_control_policy_name of this PhoneJson.


        :param feature_control_policy_name: The feature_control_policy_name of this PhoneJson.  # noqa: E501
        :type: str
        """
        if feature_control_policy_name is None:
            raise ValueError("Invalid value for `feature_control_policy_name`, must not be `None`")  # noqa: E501

        self._feature_control_policy_name = feature_control_policy_name

    @property
    def buttons(self):
        """Gets the buttons of this PhoneJson.  # noqa: E501


        :return: The buttons of this PhoneJson.  # noqa: E501
        :rtype: list[ButtonJson]
        """
        return self._buttons

    @buttons.setter
    def buttons(self, buttons):
        """Sets the buttons of this PhoneJson.


        :param buttons: The buttons of this PhoneJson.  # noqa: E501
        :type: list[ButtonJson]
        """
        if buttons is None:
            raise ValueError("Invalid value for `buttons`, must not be `None`")  # noqa: E501

        self._buttons = buttons

    @property
    def expansion_modules(self):
        """Gets the expansion_modules of this PhoneJson.  # noqa: E501


        :return: The expansion_modules of this PhoneJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._expansion_modules

    @expansion_modules.setter
    def expansion_modules(self, expansion_modules):
        """Sets the expansion_modules of this PhoneJson.


        :param expansion_modules: The expansion_modules of this PhoneJson.  # noqa: E501
        :type: list[str]
        """
        if expansion_modules is None:
            raise ValueError("Invalid value for `expansion_modules`, must not be `None`")  # noqa: E501

        self._expansion_modules = expansion_modules

    @property
    def associated_app_users(self):
        """Gets the associated_app_users of this PhoneJson.  # noqa: E501


        :return: The associated_app_users of this PhoneJson.  # noqa: E501
        :rtype: list[AppUserRefJson]
        """
        return self._associated_app_users

    @associated_app_users.setter
    def associated_app_users(self, associated_app_users):
        """Sets the associated_app_users of this PhoneJson.


        :param associated_app_users: The associated_app_users of this PhoneJson.  # noqa: E501
        :type: list[AppUserRefJson]
        """
        if associated_app_users is None:
            raise ValueError("Invalid value for `associated_app_users`, must not be `None`")  # noqa: E501

        self._associated_app_users = associated_app_users

    @property
    def associated_end_users(self):
        """Gets the associated_end_users of this PhoneJson.  # noqa: E501


        :return: The associated_end_users of this PhoneJson.  # noqa: E501
        :rtype: list[EndUserRefJson]
        """
        return self._associated_end_users

    @associated_end_users.setter
    def associated_end_users(self, associated_end_users):
        """Sets the associated_end_users of this PhoneJson.


        :param associated_end_users: The associated_end_users of this PhoneJson.  # noqa: E501
        :type: list[EndUserRefJson]
        """
        if associated_end_users is None:
            raise ValueError("Invalid value for `associated_end_users`, must not be `None`")  # noqa: E501

        self._associated_end_users = associated_end_users

    @property
    def service_subscriptions(self):
        """Gets the service_subscriptions of this PhoneJson.  # noqa: E501


        :return: The service_subscriptions of this PhoneJson.  # noqa: E501
        :rtype: list[PhoneServiceSubscriptionJson]
        """
        return self._service_subscriptions

    @service_subscriptions.setter
    def service_subscriptions(self, service_subscriptions):
        """Sets the service_subscriptions of this PhoneJson.


        :param service_subscriptions: The service_subscriptions of this PhoneJson.  # noqa: E501
        :type: list[PhoneServiceSubscriptionJson]
        """
        if service_subscriptions is None:
            raise ValueError("Invalid value for `service_subscriptions`, must not be `None`")  # noqa: E501

        self._service_subscriptions = service_subscriptions

    @property
    def phone_load_name(self):
        """Gets the phone_load_name of this PhoneJson.  # noqa: E501


        :return: The phone_load_name of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._phone_load_name

    @phone_load_name.setter
    def phone_load_name(self, phone_load_name):
        """Sets the phone_load_name of this PhoneJson.


        :param phone_load_name: The phone_load_name of this PhoneJson.  # noqa: E501
        :type: str
        """
        if phone_load_name is None:
            raise ValueError("Invalid value for `phone_load_name`, must not be `None`")  # noqa: E501

        self._phone_load_name = phone_load_name

    @property
    def subscribe_css(self):
        """Gets the subscribe_css of this PhoneJson.  # noqa: E501


        :return: The subscribe_css of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._subscribe_css

    @subscribe_css.setter
    def subscribe_css(self, subscribe_css):
        """Sets the subscribe_css of this PhoneJson.


        :param subscribe_css: The subscribe_css of this PhoneJson.  # noqa: E501
        :type: str
        """
        if subscribe_css is None:
            raise ValueError("Invalid value for `subscribe_css`, must not be `None`")  # noqa: E501

        self._subscribe_css = subscribe_css

    @property
    def emergency_numbers(self):
        """Gets the emergency_numbers of this PhoneJson.  # noqa: E501


        :return: The emergency_numbers of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._emergency_numbers

    @emergency_numbers.setter
    def emergency_numbers(self, emergency_numbers):
        """Sets the emergency_numbers of this PhoneJson.


        :param emergency_numbers: The emergency_numbers of this PhoneJson.  # noqa: E501
        :type: str
        """
        if emergency_numbers is None:
            raise ValueError("Invalid value for `emergency_numbers`, must not be `None`")  # noqa: E501

        self._emergency_numbers = emergency_numbers

    @property
    def cisco_support_field(self):
        """Gets the cisco_support_field of this PhoneJson.  # noqa: E501


        :return: The cisco_support_field of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._cisco_support_field

    @cisco_support_field.setter
    def cisco_support_field(self, cisco_support_field):
        """Sets the cisco_support_field of this PhoneJson.


        :param cisco_support_field: The cisco_support_field of this PhoneJson.  # noqa: E501
        :type: str
        """
        if cisco_support_field is None:
            raise ValueError("Invalid value for `cisco_support_field`, must not be `None`")  # noqa: E501

        self._cisco_support_field = cisco_support_field

    @property
    def ext_data_location_auth_server(self):
        """Gets the ext_data_location_auth_server of this PhoneJson.  # noqa: E501


        :return: The ext_data_location_auth_server of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._ext_data_location_auth_server

    @ext_data_location_auth_server.setter
    def ext_data_location_auth_server(self, ext_data_location_auth_server):
        """Sets the ext_data_location_auth_server of this PhoneJson.


        :param ext_data_location_auth_server: The ext_data_location_auth_server of this PhoneJson.  # noqa: E501
        :type: str
        """
        if ext_data_location_auth_server is None:
            raise ValueError("Invalid value for `ext_data_location_auth_server`, must not be `None`")  # noqa: E501

        self._ext_data_location_auth_server = ext_data_location_auth_server

    @property
    def ext_data_location_secure_auth_url(self):
        """Gets the ext_data_location_secure_auth_url of this PhoneJson.  # noqa: E501


        :return: The ext_data_location_secure_auth_url of this PhoneJson.  # noqa: E501
        :rtype: str
        """
        return self._ext_data_location_secure_auth_url

    @ext_data_location_secure_auth_url.setter
    def ext_data_location_secure_auth_url(self, ext_data_location_secure_auth_url):
        """Sets the ext_data_location_secure_auth_url of this PhoneJson.


        :param ext_data_location_secure_auth_url: The ext_data_location_secure_auth_url of this PhoneJson.  # noqa: E501
        :type: str
        """
        if ext_data_location_secure_auth_url is None:
            raise ValueError("Invalid value for `ext_data_location_secure_auth_url`, must not be `None`")  # noqa: E501

        self._ext_data_location_secure_auth_url = ext_data_location_secure_auth_url

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
        if issubclass(PhoneJson, dict):
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
        if not isinstance(other, PhoneJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
