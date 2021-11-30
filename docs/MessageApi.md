# swagger_client.MessageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mib_resources_messages_create_message**](MessageApi.md#mib_resources_messages_create_message) | **POST** /message/{user_email} | Add a new message with sender &#x3D; user_email
[**mib_resources_messages_delete_message_by_id**](MessageApi.md#mib_resources_messages_delete_message_by_id) | **DELETE** /message/{message_id} | Delete the message with id &#x3D; message_id
[**mib_resources_messages_get_message_by_id**](MessageApi.md#mib_resources_messages_get_message_by_id) | **GET** /message/{message_id} | Get the message with id &#x3D; message_id
[**mib_resources_messages_update_message**](MessageApi.md#mib_resources_messages_update_message) | **PUT** /message/{user_email} | Update the message with sender &#x3D; user_email

# **mib_resources_messages_create_message**
> Message mib_resources_messages_create_message(body, user_email)

Add a new message with sender = user_email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
body = swagger_client.MessageFields() # MessageFields | Create a new message inside microservice app
user_email = 'user_email_example' # str | User unique email

try:
    # Add a new message with sender = user_email
    api_response = api_instance.mib_resources_messages_create_message(body, user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->mib_resources_messages_create_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageFields**](MessageFields.md)| Create a new message inside microservice app | 
 **user_email** | **str**| User unique email | 

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mib_resources_messages_delete_message_by_id**
> InlineResponse202 mib_resources_messages_delete_message_by_id(message_id)

Delete the message with id = message_id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
message_id = 56 # int | Message unique id

try:
    # Delete the message with id = message_id
    api_response = api_instance.mib_resources_messages_delete_message_by_id(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->mib_resources_messages_delete_message_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**| Message unique id | 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mib_resources_messages_get_message_by_id**
> Message mib_resources_messages_get_message_by_id(message_id)

Get the message with id = message_id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
message_id = 56 # int | Message unique id

try:
    # Get the message with id = message_id
    api_response = api_instance.mib_resources_messages_get_message_by_id(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->mib_resources_messages_get_message_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**| Message unique id | 

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mib_resources_messages_update_message**
> Message mib_resources_messages_update_message(body, user_email)

Update the message with sender = user_email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
body = swagger_client.MessageFields() # MessageFields | Update the message inside microservice app
user_email = 'user_email_example' # str | User unique email

try:
    # Update the message with sender = user_email
    api_response = api_instance.mib_resources_messages_update_message(body, user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->mib_resources_messages_update_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageFields**](MessageFields.md)| Update the message inside microservice app | 
 **user_email** | **str**| User unique email | 

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

