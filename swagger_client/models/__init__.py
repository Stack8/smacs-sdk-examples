# coding: utf-8

# flake8: noqa
"""
    Helpdesk REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.8.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.admin_global_configuration_json import AdminGlobalConfigurationJson
from swagger_client.models.app_user_json import AppUserJson
from swagger_client.models.app_user_ref_json import AppUserRefJson
from swagger_client.models.app_user_result_json import AppUserResultJson
from swagger_client.models.audit_criteria_json import AuditCriteriaJson
from swagger_client.models.audit_json import AuditJson
from swagger_client.models.audit_report_category_json import AuditReportCategoryJson
from swagger_client.models.audit_report_json import AuditReportJson
from swagger_client.models.audit_report_queries_json import AuditReportQueriesJson
from swagger_client.models.audit_report_query_json import AuditReportQueryJson
from swagger_client.models.audit_search_result_json import AuditSearchResultJson
from swagger_client.models.blf_button_json import BlfButtonJson
from swagger_client.models.body import Body
from swagger_client.models.body1 import Body1
from swagger_client.models.body2 import Body2
from swagger_client.models.body3 import Body3
from swagger_client.models.body4 import Body4
from swagger_client.models.body5 import Body5
from swagger_client.models.body6 import Body6
from swagger_client.models.build_properties_json import BuildPropertiesJson
from swagger_client.models.bulk_field_copy_request_json import BulkFieldCopyRequestJson
from swagger_client.models.button_json import ButtonJson
from swagger_client.models.button_metadata import ButtonMetadata
from swagger_client.models.button_template_json import ButtonTemplateJson
from swagger_client.models.button_template_override_json import ButtonTemplateOverrideJson
from swagger_client.models.call_forward_json import CallForwardJson
from swagger_client.models.cdr_import_json import CdrImportJson
from swagger_client.models.cluster_json import ClusterJson
from swagger_client.models.cluster_ldap_sync_info_json import ClusterLdapSyncInfoJson
from swagger_client.models.cluster_result_json import ClusterResultJson
from swagger_client.models.cluster_setting_json import ClusterSettingJson
from swagger_client.models.common_phone_profile_json import CommonPhoneProfileJson
from swagger_client.models.csr_json import CsrJson
from swagger_client.models.cucm_cdr_json import CucmCdrJson
from swagger_client.models.cucm_metadata_json import CucmMetadataJson
from swagger_client.models.cucm_sql_query_json import CucmSqlQueryJson
from swagger_client.models.current_user_json import CurrentUserJson
from swagger_client.models.custom_checkbox_json import CustomCheckboxJson
from swagger_client.models.custom_input_text_json import CustomInputTextJson
from swagger_client.models.custom_multi_select_json import CustomMultiSelectJson
from swagger_client.models.custom_select_json import CustomSelectJson
from swagger_client.models.database_import_request_json import DatabaseImportRequestJson
from swagger_client.models.default_cipc_request_json import DefaultCipcRequestJson
from swagger_client.models.default_desk_phone_request_json import DefaultDeskPhoneRequestJson
from swagger_client.models.default_directory_number_request_json import DefaultDirectoryNumberRequestJson
from swagger_client.models.default_extension_mobility_request_json import DefaultExtensionMobilityRequestJson
from swagger_client.models.default_ldap_user_json import DefaultLdapUserJson
from swagger_client.models.default_ldap_user_request_json import DefaultLdapUserRequestJson
from swagger_client.models.default_phone_request_json import DefaultPhoneRequestJson
from swagger_client.models.default_snr_request_json import DefaultSnrRequestJson
from swagger_client.models.default_voicemail_request_json import DefaultVoicemailRequestJson
from swagger_client.models.deprovisioning_schedule_json import DeprovisioningScheduleJson
from swagger_client.models.deskphone_provisioning_options_json import DeskphoneProvisioningOptionsJson
from swagger_client.models.device_model_settings_json import DeviceModelSettingsJson
from swagger_client.models.device_pool_result_json import DevicePoolResultJson
from swagger_client.models.device_pool_stat_json import DevicePoolStatJson
from swagger_client.models.device_protocol_setting_json import DeviceProtocolSettingJson
from swagger_client.models.device_utilization_json import DeviceUtilizationJson
from swagger_client.models.device_utilization_search_result_json import DeviceUtilizationSearchResultJson
from swagger_client.models.dial_plan_entry_json import DialPlanEntryJson
from swagger_client.models.dial_plan_exception_group_json import DialPlanExceptionGroupJson
from swagger_client.models.dial_plan_group_inventory_json import DialPlanGroupInventoryJson
from swagger_client.models.dial_plan_group_json import DialPlanGroupJson
from swagger_client.models.dial_plan_management_group_json import DialPlanManagementGroupJson
from swagger_client.models.dial_plan_management_group_search_result_json import DialPlanManagementGroupSearchResultJson
from swagger_client.models.directory_number_json import DirectoryNumberJson
from swagger_client.models.directory_number_ranges_section_json import DirectoryNumberRangesSectionJson
from swagger_client.models.directory_number_ref_json import DirectoryNumberRefJson
from swagger_client.models.directory_number_result_json import DirectoryNumberResultJson
from swagger_client.models.distinguished_name_properties_json import DistinguishedNamePropertiesJson
from swagger_client.models.distribution_list_json import DistributionListJson
from swagger_client.models.distribution_list_member_json import DistributionListMemberJson
from swagger_client.models.distribution_list_ref_json import DistributionListRefJson
from swagger_client.models.distribution_list_result_json import DistributionListResultJson
from swagger_client.models.dn_detail_summary_json import DnDetailSummaryJson
from swagger_client.models.dn_did_range_json import DnDidRangeJson
from swagger_client.models.dn_exception_range_json import DnExceptionRangeJson
from swagger_client.models.dn_provisioning_options_json import DnProvisioningOptionsJson
from swagger_client.models.dummy_job_json import DummyJobJson
from swagger_client.models.dummy_phone_json import DummyPhoneJson
from swagger_client.models.end_user_deprovisioning_json import EndUserDeprovisioningJson
from swagger_client.models.end_user_json import EndUserJson
from swagger_client.models.end_user_pin_reset_request_json import EndUserPinResetRequestJson
from swagger_client.models.end_user_provisioning_options_json import EndUserProvisioningOptionsJson
from swagger_client.models.end_user_provisioning_setting_json import EndUserProvisioningSettingJson
from swagger_client.models.end_user_ref_json import EndUserRefJson
from swagger_client.models.end_user_result_json import EndUserResultJson
from swagger_client.models.end_user_summary_json import EndUserSummaryJson
from swagger_client.models.extension_mobility_json import ExtensionMobilityJson
from swagger_client.models.extension_mobility_ref_json import ExtensionMobilityRefJson
from swagger_client.models.extension_mobility_result_json import ExtensionMobilityResultJson
from swagger_client.models.extension_mobility_summary_json import ExtensionMobilitySummaryJson
from swagger_client.models.frontend_error_json import FrontendErrorJson
from swagger_client.models.generic_entity_ref_json import GenericEntityRefJson
from swagger_client.models.global360_view_json import Global360ViewJson
from swagger_client.models.global_data_json import GlobalDataJson
from swagger_client.models.global_voicemail_json import GlobalVoicemailJson
from swagger_client.models.global_voicemail_result_json import GlobalVoicemailResultJson
from swagger_client.models.hold_button_json import HoldButtonJson
from swagger_client.models.ils_alternate_number_json import IlsAlternateNumberJson
from swagger_client.models.ils_alternate_number_section_json import IlsAlternateNumberSectionJson
from swagger_client.models.intercom_button_json import IntercomButtonJson
from swagger_client.models.intercom_directory_number_json import IntercomDirectoryNumberJson
from swagger_client.models.intercom_ref_json import IntercomRefJson
from swagger_client.models.job_status_json import JobStatusJson
from swagger_client.models.ldap_configuration_json import LdapConfigurationJson
from swagger_client.models.ldap_connection_json import LdapConnectionJson
from swagger_client.models.ldap_groups_json import LdapGroupsJson
from swagger_client.models.ldap_members_json import LdapMembersJson
from swagger_client.models.ldap_permission_group_json import LdapPermissionGroupJson
from swagger_client.models.ldap_public_configuration_json import LdapPublicConfigurationJson
from swagger_client.models.ldap_sync_config_json import LdapSyncConfigJson
from swagger_client.models.ldap_sync_job_status_json import LdapSyncJobStatusJson
from swagger_client.models.ldap_user_id_json import LdapUserIdJson
from swagger_client.models.ldap_user_json import LdapUserJson
from swagger_client.models.ldap_user_result_json import LdapUserResultJson
from swagger_client.models.license_count_json import LicenseCountJson
from swagger_client.models.license_info_json import LicenseInfoJson
from swagger_client.models.license_modules_json import LicenseModulesJson
from swagger_client.models.license_status_json import LicenseStatusJson
from swagger_client.models.line_button_json import LineButtonJson
from swagger_client.models.line_feature_json import LineFeatureJson
from swagger_client.models.line_group_json import LineGroupJson
from swagger_client.models.line_group_member_json import LineGroupMemberJson
from swagger_client.models.line_group_ref_json import LineGroupRefJson
from swagger_client.models.line_group_result_json import LineGroupResultJson
from swagger_client.models.login_request_json import LoginRequestJson
from swagger_client.models.ms_graph_registration_details_json import MsGraphRegistrationDetailsJson
from swagger_client.models.multi_select_json import MultiSelectJson
from swagger_client.models.none_button_json import NoneButtonJson
from swagger_client.models.nvp_json import NvpJson
from swagger_client.models.one_of_button_json import OneOfButtonJson
from swagger_client.models.open_nms_inventory_report_json import OpenNmsInventoryReportJson
from swagger_client.models.orphaned_device_json import OrphanedDeviceJson
from swagger_client.models.orphaned_device_list_json import OrphanedDeviceListJson
from swagger_client.models.pcce_agent_json import PcceAgentJson
from swagger_client.models.pcce_agent_ref_json import PcceAgentRefJson
from swagger_client.models.pcce_agent_result_json import PcceAgentResultJson
from swagger_client.models.pcce_department_json import PcceDepartmentJson
from swagger_client.models.pcce_metadata_json import PcceMetadataJson
from swagger_client.models.pcce_ref_json import PcceRefJson
from swagger_client.models.phone_button_template_inventory_json import PhoneButtonTemplateInventoryJson
from swagger_client.models.phone_button_template_json import PhoneButtonTemplateJson
from swagger_client.models.phone_button_template_ref_json import PhoneButtonTemplateRefJson
from swagger_client.models.phone_button_template_result_json import PhoneButtonTemplateResultJson
from swagger_client.models.phone_button_template_search_json import PhoneButtonTemplateSearchJson
from swagger_client.models.phone_inventory_json import PhoneInventoryJson
from swagger_client.models.phone_json import PhoneJson
from swagger_client.models.phone_ref_json import PhoneRefJson
from swagger_client.models.phone_result_json import PhoneResultJson
from swagger_client.models.phone_service_metadata_json import PhoneServiceMetadataJson
from swagger_client.models.phone_service_parameter_metadata_json import PhoneServiceParameterMetadataJson
from swagger_client.models.phone_service_subscription_json import PhoneServiceSubscriptionJson
from swagger_client.models.phone_status_json import PhoneStatusJson
from swagger_client.models.phone_summary_json import PhoneSummaryJson
from swagger_client.models.post_ldap_user_json import PostLdapUserJson
from swagger_client.models.post_phone_button_template_json import PostPhoneButtonTemplateJson
from swagger_client.models.post_voicemail_json import PostVoicemailJson
from swagger_client.models.provisioning_schedule_json import ProvisioningScheduleJson
from swagger_client.models.pstn_failover_section_json import PstnFailoverSectionJson
from swagger_client.models.roles_json import RolesJson
from swagger_client.models.saml_sso_config_json import SamlSsoConfigJson
from swagger_client.models.security_profile_json import SecurityProfileJson
from swagger_client.models.select_json import SelectJson
from swagger_client.models.server_json import ServerJson
from swagger_client.models.server_ldap_sync_info_json import ServerLdapSyncInfoJson
from swagger_client.models.server_status_json import ServerStatusJson
from swagger_client.models.service_setting_json import ServiceSettingJson
from swagger_client.models.service_url_button_json import ServiceUrlButtonJson
from swagger_client.models.site_json import SiteJson
from swagger_client.models.site_mac_user_permission_json import SiteMacUserPermissionJson
from swagger_client.models.site_mac_user_permissions_json import SiteMacUserPermissionsJson
from swagger_client.models.site_result_json import SiteResultJson
from swagger_client.models.site_search_result_json import SiteSearchResultJson
from swagger_client.models.site_summary_json import SiteSummaryJson
from swagger_client.models.smtp_address_ref_json import SmtpAddressRefJson
from swagger_client.models.snr_destination_json import SnrDestinationJson
from swagger_client.models.snr_destination_ref_json import SnrDestinationRefJson
from swagger_client.models.snr_destination_result_json import SnrDestinationResultJson
from swagger_client.models.snr_profile_json import SnrProfileJson
from swagger_client.models.snr_profile_ref_json import SnrProfileRefJson
from swagger_client.models.snr_profile_result_json import SnrProfileResultJson
from swagger_client.models.snr_summary_json import SnrSummaryJson
from swagger_client.models.speed_dial_button_json import SpeedDialButtonJson
from swagger_client.models.sql_query_result_json import SqlQueryResultJson
from swagger_client.models.system_health_status_json import SystemHealthStatusJson
from swagger_client.models.template_button_json import TemplateButtonJson
from swagger_client.models.timestamp_json import TimestampJson
from swagger_client.models.traffic_status_json import TrafficStatusJson
from swagger_client.models.translation_pattern_json import TranslationPatternJson
from swagger_client.models.translation_pattern_ranges_section_json import TranslationPatternRangesSectionJson
from swagger_client.models.translation_pattern_ref_json import TranslationPatternRefJson
from swagger_client.models.translation_pattern_result_json import TranslationPatternResultJson
from swagger_client.models.uccx_agent_json import UccxAgentJson
from swagger_client.models.uccx_agent_ref_json import UccxAgentRefJson
from swagger_client.models.uccx_agent_result_json import UccxAgentResultJson
from swagger_client.models.uccx_agent_skill_json import UccxAgentSkillJson
from swagger_client.models.uccx_metadata_json import UccxMetadataJson
from swagger_client.models.ui_properties_json import UiPropertiesJson
from swagger_client.models.unused_devices_report_json import UnusedDevicesReportJson
from swagger_client.models.validate_query_request_json import ValidateQueryRequestJson
from swagger_client.models.validate_query_response_json import ValidateQueryResponseJson
from swagger_client.models.version_json import VersionJson
from swagger_client.models.voicemail_alternate_extension_json import VoicemailAlternateExtensionJson
from swagger_client.models.voicemail_alternate_extension_ref_json import VoicemailAlternateExtensionRefJson
from swagger_client.models.voicemail_json import VoicemailJson
from swagger_client.models.voicemail_pin_reset_request_json import VoicemailPinResetRequestJson
from swagger_client.models.voicemail_ref_json import VoicemailRefJson
from swagger_client.models.voicemail_result_json import VoicemailResultJson
from swagger_client.models.write_ldap_section_json import WriteLdapSectionJson
from swagger_client.models.zero_touch_provisioning_options_json import ZeroTouchProvisioningOptionsJson
