# swagger_client.NotificationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mib_resources_messages_get_notifications**](NotificationsApi.md#mib_resources_messages_get_notifications) | **GET** /notifications/{user_email} | Get the number of notifications for the user with user_email

# **mib_resources_messages_get_notifications**
> Notifications mib_resources_messages_get_notifications(user_email)

Get the number of notifications for the user with user_email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
user_email = 'user_email_example' # str | User unique email

try:
    # Get the number of notifications for the user with user_email
    api_response = api_instance.mib_resources_messages_get_notifications(user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->mib_resources_messages_get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**| User unique email | 

### Return type

[**Notifications**](Notifications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

