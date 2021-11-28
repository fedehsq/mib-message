# swagger_client.MailboxApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mib_resources_messages_get_draft_messages**](MailboxApi.md#mib_resources_messages_get_draft_messages) | **GET** /draft/{user_email} | Get the draft messages of the user with user_email
[**mib_resources_messages_get_inbox_messages**](MailboxApi.md#mib_resources_messages_get_inbox_messages) | **GET** /inbox/{user_email} | Get the inbox messages of the user with user_email
[**mib_resources_messages_get_scheduled_messages**](MailboxApi.md#mib_resources_messages_get_scheduled_messages) | **GET** /scheduled/{user_email} | get the scheduled messages of the user with user_email
[**mib_resources_messages_get_sent_messages**](MailboxApi.md#mib_resources_messages_get_sent_messages) | **GET** /sent/{user_email} | Get the sent messages of the user with user_email

# **mib_resources_messages_get_draft_messages**
> Messages mib_resources_messages_get_draft_messages(user_email)

Get the draft messages of the user with user_email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MailboxApi()
user_email = 'user_email_example' # str | User unique email

try:
    # Get the draft messages of the user with user_email
    api_response = api_instance.mib_resources_messages_get_draft_messages(user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailboxApi->mib_resources_messages_get_draft_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**| User unique email | 

### Return type

[**Messages**](Messages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mib_resources_messages_get_inbox_messages**
> Messages mib_resources_messages_get_inbox_messages(user_email)

Get the inbox messages of the user with user_email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MailboxApi()
user_email = 'user_email_example' # str | User unique email

try:
    # Get the inbox messages of the user with user_email
    api_response = api_instance.mib_resources_messages_get_inbox_messages(user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailboxApi->mib_resources_messages_get_inbox_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**| User unique email | 

### Return type

[**Messages**](Messages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mib_resources_messages_get_scheduled_messages**
> Messages mib_resources_messages_get_scheduled_messages(user_email)

get the scheduled messages of the user with user_email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MailboxApi()
user_email = 'user_email_example' # str | User unique email

try:
    # get the scheduled messages of the user with user_email
    api_response = api_instance.mib_resources_messages_get_scheduled_messages(user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailboxApi->mib_resources_messages_get_scheduled_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**| User unique email | 

### Return type

[**Messages**](Messages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mib_resources_messages_get_sent_messages**
> Messages mib_resources_messages_get_sent_messages(user_email)

Get the sent messages of the user with user_email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MailboxApi()
user_email = 'user_email_example' # str | User unique email

try:
    # Get the sent messages of the user with user_email
    api_response = api_instance.mib_resources_messages_get_sent_messages(user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailboxApi->mib_resources_messages_get_sent_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**| User unique email | 

### Return type

[**Messages**](Messages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

