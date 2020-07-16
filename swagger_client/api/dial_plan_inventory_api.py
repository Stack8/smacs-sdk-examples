# coding: utf-8

"""
    Helpdesk REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.8.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DialPlanInventoryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_dial_plan_inventories(self, **kwargs):  # noqa: E501
        """Get dial plan inventory report  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_dial_plan_inventories(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DialPlanGroupInventoryJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_dial_plan_inventories_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_dial_plan_inventories_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_dial_plan_inventories_with_http_info(self, **kwargs):  # noqa: E501
        """Get dial plan inventory report  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_dial_plan_inventories_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DialPlanGroupInventoryJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_dial_plan_inventories" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/reports/dial-plan-inventories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DialPlanGroupInventoryJson]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_dial_plan_inventories_detailed(self, **kwargs):  # noqa: E501
        """Get detailed inventory of all directory numbers on all clusters in a .xlsx format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_dial_plan_inventories_detailed(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_dial_plan_inventories_detailed_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_dial_plan_inventories_detailed_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_dial_plan_inventories_detailed_with_http_info(self, **kwargs):  # noqa: E501
        """Get detailed inventory of all directory numbers on all clusters in a .xlsx format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_dial_plan_inventories_detailed_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_dial_plan_inventories_detailed" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/reports/dial-plan-inventories/export', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dial_plan_inventory_by_group_id(self, group_id, **kwargs):  # noqa: E501
        """A report containing the corresponding DN/DID group ID and name along with all dial plan entries for the specified site.  # noqa: E501

        A report containing the corresponding DN/DID group ID and name along with all dial plan entries for the specified site. Each dial plan entry will contain:  <ul> <li>type - DN or TP.</li> <li>value - If DN, then extension. If TP, then pattern.</li> <li>status - AVAILABLE or ACTIVE or INACTIVE or RESTRICTED.</li> <li>description - If ACTIVE or INACTIVE then this is present and reflects whatever is on      the corresponding DN or TP respectively. </li> <li>deletionDate - If AVAILABLE and the DN or TP has been deleted then the last deletion      date is retrieved from the audits. </li> <li>exceptionGroupName - If RESTRICTED, then the exception group name.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dial_plan_inventory_by_group_id(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int group_id: The id of the group (required)
        :return: DialPlanGroupJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dial_plan_inventory_by_group_id_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dial_plan_inventory_by_group_id_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def get_dial_plan_inventory_by_group_id_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """A report containing the corresponding DN/DID group ID and name along with all dial plan entries for the specified site.  # noqa: E501

        A report containing the corresponding DN/DID group ID and name along with all dial plan entries for the specified site. Each dial plan entry will contain:  <ul> <li>type - DN or TP.</li> <li>value - If DN, then extension. If TP, then pattern.</li> <li>status - AVAILABLE or ACTIVE or INACTIVE or RESTRICTED.</li> <li>description - If ACTIVE or INACTIVE then this is present and reflects whatever is on      the corresponding DN or TP respectively. </li> <li>deletionDate - If AVAILABLE and the DN or TP has been deleted then the last deletion      date is retrieved from the audits. </li> <li>exceptionGroupName - If RESTRICTED, then the exception group name.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dial_plan_inventory_by_group_id_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int group_id: The id of the group (required)
        :return: DialPlanGroupJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dial_plan_inventory_by_group_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_dial_plan_inventory_by_group_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/reports/dial-plan-inventories/group/{groupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DialPlanGroupJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dial_plan_inventory_by_site_id(self, site_id, **kwargs):  # noqa: E501
        """A report containing the corresponding DN/DID group ID and name along with all dial plan entries for the specified site.  # noqa: E501

        A report containing the corresponding DN/DID group ID and name along with all dial plan entries for the specified site. Each dial plan entry will contain:  <ul> <li>type - DN or TP.</li> <li>value - If DN, then extension. If TP, then pattern.</li> <li>status - AVAILABLE or ACTIVE or INACTIVE or RESTRICTED.</li> <li>description - If ACTIVE or INACTIVE then this is present and reflects whatever is on      the corresponding DN or TP respectively. </li> <li>deletionDate - If AVAILABLE and the DN or TP has been deleted then the last deletion      date is retrieved from the audits. </li> <li>exceptionGroupName - If RESTRICTED, then the exception group name.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dial_plan_inventory_by_site_id(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: The site id (required)
        :return: list[DialPlanGroupJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dial_plan_inventory_by_site_id_with_http_info(site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dial_plan_inventory_by_site_id_with_http_info(site_id, **kwargs)  # noqa: E501
            return data

    def get_dial_plan_inventory_by_site_id_with_http_info(self, site_id, **kwargs):  # noqa: E501
        """A report containing the corresponding DN/DID group ID and name along with all dial plan entries for the specified site.  # noqa: E501

        A report containing the corresponding DN/DID group ID and name along with all dial plan entries for the specified site. Each dial plan entry will contain:  <ul> <li>type - DN or TP.</li> <li>value - If DN, then extension. If TP, then pattern.</li> <li>status - AVAILABLE or ACTIVE or INACTIVE or RESTRICTED.</li> <li>description - If ACTIVE or INACTIVE then this is present and reflects whatever is on      the corresponding DN or TP respectively. </li> <li>deletionDate - If AVAILABLE and the DN or TP has been deleted then the last deletion      date is retrieved from the audits. </li> <li>exceptionGroupName - If RESTRICTED, then the exception group name.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dial_plan_inventory_by_site_id_with_http_info(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: The site id (required)
        :return: list[DialPlanGroupJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dial_plan_inventory_by_site_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_dial_plan_inventory_by_site_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/reports/dial-plan-inventories/site/{siteId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DialPlanGroupJson]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
