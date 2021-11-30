# swagger_client.MessagesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mib_resources_messages_search_message**](MessagesApi.md#mib_resources_messages_search_message) | **POST** /search/{user_email} | Returns the searched messages of the user with user_email

# **mib_resources_messages_search_message**
> FilteredMessages mib_resources_messages_search_message(body, user_email)

Returns the searched messages of the user with user_email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagesApi()
body = swagger_client.Search() # Search | Fields to search in the messages
user_email = 'user_email_example' # str | User requester unique email

try:
    # Returns the searched messages of the user with user_email
    api_response = api_instance.mib_resources_messages_search_message(body, user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->mib_resources_messages_search_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Search**](Search.md)| Fields to search in the messages | 
 **user_email** | **str**| User requester unique email | 

### Return type

[**FilteredMessages**](FilteredMessages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

