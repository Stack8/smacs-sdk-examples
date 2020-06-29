### Examples of how to use Stack8 SDKs

Welcome to Stack8's smacs-sdk-examples repo, which currently contains our Python SDK as well as an example script written in Python 3.6 to show how it can be used to make managing your UC environment simpler and more efficient. 

In order to call the SMACS APIs a bit of configuration is necessary. The following properties will need to be set in the configuration.py file within the swagger_client folder before opening the script:

```
self.host = "url to your instance of SMACS/services"
self.username = "username for user with admin privileges"
self.password = "password for user with admin privileges"
```

Once these properties are set, you can open smacs_sdk_examples.py in your text editor of choice and follow the instructions provided for an example of how to automate the provisioning and deprovisioning of an End User. 

Feel free to contact customer support for any questions you may have regarding the use of our APIs, and thank you for the continued support!
