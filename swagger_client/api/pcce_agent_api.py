# coding: utf-8

"""
    Helpdesk REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.8.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PCCEAgentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_pcce_agent(self, server_id, agent_uuid, **kwargs):  # noqa: E501
        """Delete a PCCE agent on the server  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_pcce_agent(server_id, agent_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: (required)
        :param str agent_uuid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_pcce_agent_with_http_info(server_id, agent_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_pcce_agent_with_http_info(server_id, agent_uuid, **kwargs)  # noqa: E501
            return data

    def delete_pcce_agent_with_http_info(self, server_id, agent_uuid, **kwargs):  # noqa: E501
        """Delete a PCCE agent on the server  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_pcce_agent_with_http_info(server_id, agent_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: (required)
        :param str agent_uuid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'agent_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pcce_agent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `delete_pcce_agent`")  # noqa: E501
        # verify the required parameter 'agent_uuid' is set
        if ('agent_uuid' not in params or
                params['agent_uuid'] is None):
            raise ValueError("Missing the required parameter `agent_uuid` when calling `delete_pcce_agent`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['serverId'] = params['server_id']  # noqa: E501
        if 'agent_uuid' in params:
            path_params['agentUuid'] = params['agent_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mac/pcce-servers/{serverId}/pcce-agents/{agentUuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pcce_agent(self, server_id, agent_uuid, **kwargs):  # noqa: E501
        """Retrieve a PCCE agent from the server  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pcce_agent(server_id, agent_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: (required)
        :param str agent_uuid: (required)
        :return: PcceAgentJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pcce_agent_with_http_info(server_id, agent_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pcce_agent_with_http_info(server_id, agent_uuid, **kwargs)  # noqa: E501
            return data

    def get_pcce_agent_with_http_info(self, server_id, agent_uuid, **kwargs):  # noqa: E501
        """Retrieve a PCCE agent from the server  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pcce_agent_with_http_info(server_id, agent_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: (required)
        :param str agent_uuid: (required)
        :return: PcceAgentJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'agent_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pcce_agent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `get_pcce_agent`")  # noqa: E501
        # verify the required parameter 'agent_uuid' is set
        if ('agent_uuid' not in params or
                params['agent_uuid'] is None):
            raise ValueError("Missing the required parameter `agent_uuid` when calling `get_pcce_agent`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['serverId'] = params['server_id']  # noqa: E501
        if 'agent_uuid' in params:
            path_params['agentUuid'] = params['agent_uuid']  # noqa: E501

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
            '/mac/pcce-servers/{serverId}/pcce-agents/{agentUuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PcceAgentJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_pcce_agent(self, server_id, **kwargs):  # noqa: E501
        """Create a PCCE agent on the server  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pcce_agent(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: (required)
        :param PcceAgentJson body:
        :return: PcceAgentRefJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_pcce_agent_with_http_info(server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_pcce_agent_with_http_info(server_id, **kwargs)  # noqa: E501
            return data

    def post_pcce_agent_with_http_info(self, server_id, **kwargs):  # noqa: E501
        """Create a PCCE agent on the server  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pcce_agent_with_http_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: (required)
        :param PcceAgentJson body:
        :return: PcceAgentRefJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pcce_agent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `post_pcce_agent`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['serverId'] = params['server_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mac/pcce-servers/{serverId}/pcce-agents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PcceAgentRefJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_pcce_agent(self, server_id, agent_uuid, **kwargs):  # noqa: E501
        """Update a PCCE agent on the server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_pcce_agent(server_id, agent_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: (required)
        :param str agent_uuid: (required)
        :param PcceAgentJson body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_pcce_agent_with_http_info(server_id, agent_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.put_pcce_agent_with_http_info(server_id, agent_uuid, **kwargs)  # noqa: E501
            return data

    def put_pcce_agent_with_http_info(self, server_id, agent_uuid, **kwargs):  # noqa: E501
        """Update a PCCE agent on the server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_pcce_agent_with_http_info(server_id, agent_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: (required)
        :param str agent_uuid: (required)
        :param PcceAgentJson body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'agent_uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_pcce_agent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `put_pcce_agent`")  # noqa: E501
        # verify the required parameter 'agent_uuid' is set
        if ('agent_uuid' not in params or
                params['agent_uuid'] is None):
            raise ValueError("Missing the required parameter `agent_uuid` when calling `put_pcce_agent`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['serverId'] = params['server_id']  # noqa: E501
        if 'agent_uuid' in params:
            path_params['agentUuid'] = params['agent_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mac/pcce-servers/{serverId}/pcce-agents/{agentUuid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
