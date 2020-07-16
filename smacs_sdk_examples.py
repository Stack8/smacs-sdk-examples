import swagger_client

"""
Don't have SMACS yet? Our world-class UC Provisioning Tool enables users to manage moves, adds, changes, deletes and so 
much more. Visit https://stack8.com to book your demo today!
"""

"""
In this example script, we will be be using the APIs to provision and then deprovision an end user with a DN on a 
specified site. We will also provision a deskphone and Single Number Reach if 1-Click provisioning is enabled for those
services on the selected site. (You can use the automation API to provision a user with any services as long as they 
have 1-click enabled.) In order to run this script the following parameters will need to be provided: 
"""

username = ''  # The username of the user you wish to provision.
dial_plan_group_name = ''  # The name of the dial plan group you wish to assign a DN from.
site_id = 0  # The id of the site they will be provisioned on.
mac_address = ''  # The MAC Address of the phone to be assigned to the user, if 1-Click provisioning is
# enabled for deskphones on the selected site. A dummy MAC Address can be provided as long as it is in a valid format.

"""
If you don't have the id for the site you wish to provision to, you can search for it using the site name, like so:

search_params = {"site_name": "Your site name"}
site_id = swagger_client.SitesApi().search_sites(**search_params)[0].id
"""

# This script will consume the following APIs:

end_user_deprovisioning_api = swagger_client.EndUserDeprovisioningApi()
end_user_provisioning_api = swagger_client.EndUserProvisioningApi()
global_360_view_api = swagger_client.Global360ViewApi()

"""
First we will call the Automated Deprovisioning API in order to make sure the user is in a clean state before 
attempting to provision them with a new DN, deskphone and SNR.
"""

deprovisioning_settings_json = {"username": username, "makeDeskphonesPublic": False}
print('Deprovisioning End User:', username)
print('Calling SMACS End User Deprovisioning API...')
end_user_deprovisioning_api.post_end_user_deprovisioning(deprovisioning_settings_json)
print('End User Deprovisioning completed successfully!')

"""
Next we'll need to get the End User Provisioning Settings for the site we wish to provision the user on. This will allow
us to determine whether or not they can be provisioned for a deskphone and/or SNR, as well as enable us to get the id
for the dial plan group we've chosen to assign them a DN from.
"""

print('Getting end user provisioning settings for site', site_id)
print('Calling SMACS End User Provisioning Settings API...')
provisioning_settings = end_user_provisioning_api.get_end_user_provisioning_setting(site_id = site_id)
print('End user provisioning settings for site', site_id, ':')
print(provisioning_settings)

deskphone_enabled = provisioning_settings.deskphone
print('Deskphone 1-Click provisioning enabled for site', site_id, '?')
print(deskphone_enabled)

snr_enabled = provisioning_settings.snr
print('Single Number Reach 1-Click provisioning enabled for site', site_id, '?')
print(snr_enabled)

dial_plan_groups = provisioning_settings.dial_plan_groups
dial_plan_group_id = list(dial_plan_groups.keys())[list(dial_plan_groups.values()).index(dial_plan_group_name)]
print('Dial plan group id for', dial_plan_group_name, ':')
print(dial_plan_group_id)

"""
Now that we have our required info, we can set up the json request body required to provision our user with the desired
options.
"""

print('Configuring end user provisioning post request body...')
end_user_provisioning_post_body = {
    "username": username,
    "siteId": site_id,
    "dn": {
        "dialPlanGroupIds": [
            dial_plan_group_id
        ],
        # When assigning a DN you can either provide a list of dial plan group ids for an available extension to
        # be chosen from, or provide a specific extension using the following attribute in place of "dialPlanGroupIds":
        # "extension": "string"
    },
    "agentExtension": False,
    "voicemail": False,
    "snr": snr_enabled,
    "mobility": False,
    "imSoftphone": False,
    "imp": False,
    "cipc": False,
    "iphone": False,
    "android": False,
    "tablet": False
}

if deskphone_enabled:
    end_user_provisioning_post_body["deskphone"] = {"phoneModel": "Cisco 8851", "macAddress": mac_address}

print('End User Provisioning Post Request Body:')
print(end_user_provisioning_post_body)

"""
"With the request body configured, we are now ready to provision our End User. With 1-Click Provisioning set up we can 
provision our user for all of the services we've selected with a single call to our End User Provisioning API.
"""

print('Provisioning End User:', username)
print('Calling SMACS End User Provisioning API...')
end_user_provisioning_api.post_end_user_provisioning(end_user_provisioning_post_body)
print('End User Provisioning completed successfully!')

"""
Our End User has now been provisioned successfully! To verify this, we can call the Global 360 View API, which provides
a list of a user's services across all clusters.
"""

print('Getting list of services for user:', username)
print('Calling SMACS Global 360 View API...')
response = global_360_view_api.get_global360_view(username)
print('List of services for user', username, ':')
print(response)
print('We can see that the desired services have been provisioned.')

"""
That was quick! Since this is just an example we'll make sure to clean things up and finish by deprovisioning our  
user. Though it only shows a fraction of what can be done with our APIs, we hope this sample script has given you an 
idea of how instrumental they can be in speeding up your UC workflow and giving your users more time to focus on the 
work that really matters. For more information on how to consume our APIs please contact customer support.  
"""

print('Deprovisioning End User:', username)
print('Calling SMACS End User Deprovisioning API...')
end_user_deprovisioning_api.post_end_user_deprovisioning(deprovisioning_settings_json)
print('End User Deprovosioning completed successfully!')

print('Thanks for trying out the SMACS APIs. We at Stack8 would like to thank you for your continued support!')
